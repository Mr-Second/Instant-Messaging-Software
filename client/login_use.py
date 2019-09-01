from ui2py.login import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui
import socket
from client.config_use import ConfigWin
from client.register_use import Register
import time
import os
from client.chat_use import ChatWin


class Login(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.close_btn.clicked.connect(self.on_button_close_clicked)
        self.m_flag = None
        self.m_Position = None
        self.socket = None
        self.server_ip = None
        self.server_port = None
        self.username = None
        self.password = None
        self.init()

    # 配置服务器的IP地址和端口号,如果不是第一次配置就直接读取配置文件，反之则进行配置并写入文件
    def init(self):
        account_psd_path = os.path.abspath(os.path.dirname(os.getcwd()))+"/resource/account.ini"
        if os.path.exists(account_psd_path):
            temp = []
            with open(account_psd_path) as f:
                lines = f.readlines()
                for line in lines:
                    temp.append(line.strip())
            self.accountInput.setText(temp[0])
            self.psdInput.setText(temp[1])

        path = os.path.dirname(os.getcwd()) + "\\resource/config.ini"
        print(path)
        if os.path.exists(path):
            with open(path, "r") as f:
                text = f.readlines()
                self.server_ip = text[0].strip()
                self.server_port = int(text[1].strip())
                print(self.server_ip + " " + str(self.server_port))
        else:
            configwin = ConfigWin()
            configwin.TwoParameter.connect(self.deal_configwin_emit_slot)
            configwin.exec_()

            with open(path, "w", encoding="utf-8") as f:
                f.write(self.server_ip+"\n"+str(self.server_port))

            print(self.server_port, self.server_ip)

    # 槽函数接受来自配置子窗口的数据
    def deal_configwin_emit_slot(self, ip, port):
        self.server_ip = ip
        self.server_port = port

    def deal_registerwin_emit_slot(self, username, password):
        self.username = username
        self.password = password

    # 窗口关闭槽函数
    def on_button_close_clicked(self):
        i = 1
        while i <= 10:
            self.setWindowOpacity(1-i/10)
            time.sleep(0.05)
            i += 1
        self.close()

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

    def login(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if self.rememberPsd.isChecked():
            # 如果勾选了记住密码，则将账号和密码写入文本，下次再打开窗口时直接回读取文本不用再次输入
            account_psd_path = os.path.abspath(os.path.dirname(os.getcwd()))+"/resource/account.ini"
            with open(account_psd_path,"w") as f:
                f.write(self.accountInput.text()+"\n"+self.psdInput.text())

        send_data = "100&" + self.accountInput.text() + "&" + self.psdInput.text()
        print("客户端向服务器端发送数据：" + send_data)
        send_data = send_data.encode()
        addr = (self.server_ip, self.server_port)
        self.socket.sendto(send_data, addr)
        recv_data, tmp = self.socket.recvfrom(1024)
        recv_data = recv_data.decode()
        print(recv_data)
        if recv_data == "1":  # 登陆成功将转到用户列表
            self.socket.sendto("1".encode(), addr)  # 再次确认登陆
            print("登陆成功！")
            if self.username is None:
                self.username = self.accountInput.text()
            chatwin = ChatWin([self.username, self.server_ip, self.server_port])
            self.hide()
            chatwin.exec_()
        elif recv_data == "0":
            print("登陆失败，用户名或密码错误！")
        elif recv_data is None:
            print("服务器错误，请重新尝试登陆！")

    def register(self):
        addr = (self.server_ip, self.server_port)
        myregister = Register(addr)
        myregister.TwoParameter.connect(self.deal_registerwin_emit_slot)
        self.hide()
        myregister.exec_()
        self.show()

    # 在本地先验证密码或账号不为空
    def enable_login_btn(self):
        if len(self.accountInput.text()) == 0 or len(self.psdInput.text()) == 0:
            self.login_btn.setEnabled(False)
        else:
            self.login_btn.setEnabled(True)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())

