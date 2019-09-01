from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QLCDNumber
from ui2py.server import Ui_Dialog
from PyQt5.QtCore import QTimer
import time
import threading
import socket
import json


class Server(QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.start_btn.clicked.connect(self.start)
        self.flag = False  # 控制子线程循环
        self.socket = None
        self.dic = {}  # key是用户名，values = (password, ip, port)
        self.online_member = []  # 在线用户列表
        self.tableWidget.setRowCount(3)
        self.ip_address = socket.gethostbyname(socket.gethostname())

        self.lcdNumber.setDigitCount(10)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lcd_time_show)

        self.stop_btn.clicked.connect(self.stop)

        self.dialogue = {}
        self.CLRF = "\r\n"

    def start(self):
        self.timer.start(1000)  # 每秒触发一次timeout
        newthread = threading.Thread(target=self.listen_reply, args={})
        self.flag = True
        newthread.start()
        current_time = time.strftime("%Hh %Mm %Ss", time.localtime(time.time()))  # 日志信息
        self.chat_record.append(current_time + ": 服务器已启动" + self.CLRF)

    def lcd_time_show(self):
        current_time = time.strftime("%H:%M:%S", time.localtime(time.time()))  # 日志信息
        self.lcdNumber.display(current_time)

    def listen_reply(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip_address, 8080))
        while self.flag:
            recv_data, addr = self.socket.recvfrom(1024)  # 接受1KB的数据
            self.parse_data(recv_data, addr)

    def parse_data(self, data, addr):
        print("客户端向服务器发送数据：" + data.decode())
        print("客户端的ip地址和端口号为：" + str(addr))

        current_time = time.strftime("%Hh %Mm %Ss", time.localtime(time.time()))  # 日志信息
        data = data.decode()

        # 客户端请求获取当前在线用户列表--------------------------------------------
        if data and data == "GET":
            online_list = self.online_member
            send_data = json.dumps(online_list)  # list to json
            self.socket.sendto(send_data.encode(), addr)
            return
        # 客户端请求获取当前在线用户列表--------------------------------------------

        # 客户端请求来自其当前聊天对象的信息----------------------------------------
        if data and data.startswith("GET"):
            templist = data.split("&")  # [GET, target_user, from_user]
            from_username = templist[1]
            target_username = templist[2]
            key = from_username + "_" + target_username
            if key in self.dialogue.keys():
                count = len(self.dialogue[key])
            else:
                count = 0
            if count == 0:
                self.reply("0", addr)  # 不存在该信息
            else:
                remove_data = self.dialogue[key][0]
                send_data = remove_data + "&" + str(count-1)
                self.dialogue[key].remove(remove_data)
                self.socket.sendto(send_data.encode(), addr)
        # 客户端请求来自其当前聊天对象的信息----------------------------------------

        # 登录请求-----------------------------------------------------------------
        if data and data.startswith("100"):  # “100”代表客户端请求登陆
            templist = data.split("&")  # [flag, username, password]
            username = templist[1]
            password = templist[2]
            # 如果username存在且username对应的记录密码与用户输入的密码相等
            if username in self.dic.keys() and password == self.dic[username][0]:
                self.reply("1", addr)  # 登陆成功
                if self.listen() == "1":  # 客户端需要再次发送确认登陆包
                    if username in self.online_member:
                        return
                    self.online_member.append(username)
                    current_time = time.strftime("%Hh %Mm %Ss", time.localtime(time.time()))  # 日志信息
                    self.chat_record.append(current_time + ": " + username + "已上线" + self.CLRF)

                    #  刷新在线用户列表
                    self.update_table()
                    return
                else:
                    print("登陆请求中断")
                    return
            else:
                self.reply("0", addr)
                return
        # 登录请求-----------------------------------------------------------------

        # 注册请求-----------------------------------------------------------------
        if data and data.startswith("200"):  # “200”代表客户端请求注册
            templist = data.split("&")  # [flag, username, password]
            username = templist[1]
            password = templist[2]
            ip = addr[0]
            port = addr[1]
            if username and password:  # 用户名与密码不为空
                if username in self.dic.keys():  # 用户名重复
                    self.reply("0", addr)
                    return
                else:
                    self.reply("1", addr)
                    if self.listen() == "1":
                        current_time = time.strftime("%Hh %Mm %Ss", time.localtime(time.time()))  # 日志信息
                        self.chat_record.append(current_time + ": " + "新用户" + username + "注册成功" + self.CLRF)
                        self.dic[username] = (password, ip, port)
                        return
                    else:
                        print("注册请求中断")
                        return
            else:  # 用户名或密码为空
                self.reply("0", addr)
                return
        # 注册请求-----------------------------------------------------------------

        # 注销请求-----------------------------------------------------------------
        if data and data.startswith("300"):
            templist = data.split("&")
            self.reply("1", addr)
            self.online_member.remove(templist[1])
            self.update_table()
            self.chat_record.append(current_time + "：" + "用户" + templist[1] + "已注销" + self.CLRF)
            return
        # 注销请求-----------------------------------------------------------------

        # 对话请求-----------------------------------------------------------------
        if data and data.startswith("400"):
            templist = data.split("&")
            from_username = templist[1]
            target_username = templist[2]
            words = templist[3]
            key = from_username + "_" + target_username

            #  将对话内容放在内存中
            if key in self.dic.keys():
                self.dialogue[key].append(words)
            else:
                self.dialogue[key] = [words]
            self.reply("1", addr)
            self.chat_record.append(current_time + "：" + "用户" + from_username + "向" + target_username +
                                    "发送了一段话" + self.CLRF)
            return
        # 对话请求-----------------------------------------------------------------

        # 群发消息请求-------------------------------------------------------------
        if data and data.startswith("500"):
            templist = data.split("&")
            from_username = templist[1]
            words = templist[2]

            for target_username in self.online_member:
                key = from_username + "_" + target_username

                #  将对话内容放在内存中
                if key in self.dic.keys():
                    self.dialogue[key].append(words)
                else:
                    self.dialogue[key] = [words]

            self.reply("1", addr)
            self.chat_record.append(current_time + "：" + "用户 " + from_username + " 群发了一条消息" + self.CLRF)

        # 群发消息请求-------------------------------------------------------------

    def listen(self):
        data, temp = self.socket.recvfrom(1024)
        data = data.decode()
        return data

    def reply(self, flag, addr):  # 向客户端回复
        self.socket.sendto(flag.encode(), addr)

    def update_table(self):
        length = len(self.online_member)
        if length >= 0:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(len(self.online_member))
            i = 0
            for user in self.online_member:
                item = QTableWidgetItem(user)
                self.tableWidget.setItem(i, 0, item)
                i += 1
        self.tableWidget.viewport().update()

    def stop(self):
        self.flag = False
        self.close()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    server = Server()
    server.exec_()
    sys.exit()
