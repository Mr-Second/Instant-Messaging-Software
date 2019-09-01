from ui2py.friend_list import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QApplication, QListWidgetItem
from PyQt5 import QtCore, QtGui
import time
import socket
from client.emoji_use import Emoji
import json
import threading

"""
不同客户端之间的对话
消息的监听
"""


class ChatWin(QDialog, Ui_Dialog):
    def __init__(self, para_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.username = para_list[0]
        self.server_ip = para_list[1]
        self.server_port = para_list[2]

        self.m_flag = None
        self.control_flag = False
        self.m_Position = None
        self.chat_person = None

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.friendlist.itemClicked.connect(self.current_chat_person)

        self.init()

    # 初始化配置
    def init(self):
        self.control_flag = True
        tempthread = threading.Thread(target=self.get_friendlist, args={})
        tempthread.start()
        newthread = threading.Thread(target=self.get_words_frow_current_chat_person, args={})
        newthread.start()

    # 关闭按钮的槽函数
    def on_close_button_clicked(self):
        i = 1
        send_data = "300&" + self.username
        addr = (self.server_ip, self.server_port)
        self.socket.sendto(send_data.encode(), addr)
        recv_data, temp = self.socket.recvfrom(1024)
        recv_data = recv_data.decode()
        if recv_data == "1":
            while i <= 10:
                self.setWindowOpacity(1-i/10)
                time.sleep(0.05)
                i += 1
            self.close()
        else:
            print("第59行，在关闭按钮函数内"+"退出失败，请重新点击退出")

    # 选取表情的函数
    def choose_emoji(self):
        emoji_choose = Emoji()
        emoji_choose.exec_()
        emoji = emoji_choose.emoji
        self.textEdit.append(emoji)

    # 点击右边的某一行，获取聊天对象
    def current_chat_person(self, item):
        self.chat_person = item.text()
        self.label_2.setText("正在跟 \"" + self.chat_person+"\" 对话")

    # send按钮的槽函数，用于发送消息
    def send_words(self):
        current_time = time.strftime("%Hh %Mm %Ss", time.localtime(time.time()))
        words = self.textEdit.toPlainText()

        if self.checkBox.isChecked():   # 群发消息
            send_data = "500&" + self.username + "&" + words
            self.socket.sendto(send_data.encode(), (self.server_ip, self.server_port))
            flag, temp = self.socket.recvfrom(1024)
            flag = flag.decode()
            if flag == "1":
                self.chat_area.append("(" + current_time + ") " + self.username + " to Everyone " + ": " + words + "\n")
                self.textEdit.clear()
            else:
                print("第83行，在发送对话函数内 " + "目标不存在或服务器错误")

        else:   # 单独对指定的用户发消息
            send_data = "400&" + self.username + "&" + self.chat_person + "&" + words
            self.socket.sendto(send_data.encode(), (self.server_ip, self.server_port))
            flag, temp = self.socket.recvfrom(1024)
            flag = flag.decode()

            if flag == "1":
                self.chat_area.append("(" + current_time + ") " + "from " + self.username + " to " + self.chat_person
                                      + ": " + words + "\n")
                self.textEdit.clear()
            else:
                print("第111行，在发送对话函数内 " + "目标不存在或服务器错误")

    # 在子线程中不断向服务器请求在线用户
    def get_friendlist(self):
        addr = (self.server_ip, self.server_port)
        send_data = "GET"
        while self.control_flag:
            self.socket.sendto(send_data.encode(), addr)
            data, temp = self.socket.recvfrom(1024)
            print("第120行，在获取在线用户列表函数内 " + data.decode())
            friendlist = json.loads(data.decode())

            self.friendlist.clear()
            self.friendlist.addItems(friendlist)

            time.sleep(10.0)

    # 获取聊天对象发送给自己的信息
    def get_words_frow_current_chat_person(self):
        while self.chat_person is None:
            time.sleep(0.5)  # 如果当前聊天对象是空，则一直等待
        while self.control_flag:
            print("当前聊天对象为" + self.chat_person)
            send_data = "GET&" + self.chat_person + "&" + self.username  # 获取来自我的聊天的对象的来话
            self.socket.sendto(send_data.encode(), (self.server_ip, self.server_port))
            data, temp = self.socket.recvfrom(1024)
            data = data.decode()
            if data == "0":
                time.sleep(5.0)  # 如果没有数据来自聊天对象则先睡眠5.0s
            else:
                info = data.split("&")
                count = int(info[1])  # 表示此人发送给自己信息的条数
                print("此人发送给我信息条数剩余：" + str(count))

                current_time = time.strftime("%Hh %Mm %Ss", time.localtime(time.time()))
                content = "(" + current_time + ") " + "from " + self.chat_person + " to " + self.username \
                          + "：" + info[0]
                self.chat_area.append(content+"\n")
                if count == 0:
                    time.sleep(5.0)
                else:
                    time.sleep(1.0)

    # 以下三个函数用于控制无边框的窗口移动
    # --------------------------------------------------------------------------------
    # 重载鼠标按压事件
    def mousePressEvent(self, *args, **kwargs):
        event = args[0]
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    # 重载鼠标移动事件
    def mouseMoveEvent(self, *args, **kwargs):
        QMouseEvent = args[0]
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    # 重载鼠标释放事件
    def mouseReleaseEvent(self, *args, **kwargs):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    # --------------------------------------------------------------------------------


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    chat = ChatWin(['a', '203.195.137.94', 8080])
    chat.exec_()
    sys.exit(app.exec_())
