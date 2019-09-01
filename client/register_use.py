from ui2py.register import Ui_Register
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5 import QtCore
import socket


class Register(QDialog, Ui_Register):

    # 发送给主窗口的两个参数
    TwoParameter = QtCore.pyqtSignal(str, str)

    def __init__(self, addr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(addr)
        self.setupUi(self)
        self.socket = None
        self.register_2.clicked.connect(self.myregister)
        self.server_addr = addr

    def myregister(self):
        if self.input_check():
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            send_data = "200&" + self.username_input.text() + "&" + self.password_input.text()
            self.socket.sendto(send_data.encode(), self.server_addr)
            flag, temp = self.socket.recvfrom(1024)
            flag = flag.decode()
            if flag == "1":
                self.socket.sendto("1".encode(), self.server_addr)
                QMessageBox.information(self, "Information", "注册成功,请登录", QMessageBox.Ok)
                self.TwoParameter.emit(self.username_input.text(), self.password_input.text())
                self.close()
            elif flag == "0":
                QMessageBox.warning(self, "Warning", "注册失败，请重新注册", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Warning", "服务器错误，请稍后再次尝试", QMessageBox.Ok)

    def input_check(self):  # 昵称密码不为空且密码与确认密码相等
        print()
        if self.username_input.text() and self.password_input.text() and self.password_input.text() == \
                self.confirm_psd_input.text():
            return True
        else:
            return False


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    register = Register(("203.195.137.94", 8080))
    register.exec_()
    sys.exit(app.exec_())