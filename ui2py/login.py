# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui2py import images_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(434, 330)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Prefix/titleIco.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(235,242,249);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.top_label = QtWidgets.QLabel(self.centralwidget)
        self.top_label.setGeometry(QtCore.QRect(40, 0, 352, 31))
        self.top_label.setStyleSheet("background-color: rgb(60,78,173);")
        self.top_label.setText("")
        self.top_label.setObjectName("top_label")
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(392, 0, 42, 33))
        self.close_btn.setStyleSheet("QPushButton{\n"
"    border-image: url(:/Prefix/myClose.png);\n"
"    background-color: rgb(60,78,173);\n"
"}\n"
"QPushButton:hover{\n"
"    border-image: url(:/Prefix/myClose.png);\n"
"    background-color: rgb(255, 0, 0);\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"    border-image: url(:/Prefix/myClose.png);\n"
"    \n"
"    background-color: rgb(118, 0, 0);\n"
"}\n"
"\n"
"")
        self.close_btn.setText("")
        self.close_btn.setObjectName("close_btn")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(0, 0, 41, 31))
        self.title_label.setStyleSheet("border-image: url(:/Prefix/titleIco.ico);\n"
"background-color: rgb(60,78,173);")
        self.title_label.setText("")
        self.title_label.setObjectName("title_label")
        self.middle_label = QtWidgets.QLabel(self.centralwidget)
        self.middle_label.setGeometry(QtCore.QRect(0, 29, 434, 152))
        self.middle_label.setStyleSheet("background-color: rgb(60,78,173);\n"
"border-image: url(:/Prefix/middle.png);")
        self.middle_label.setText("")
        self.middle_label.setObjectName("middle_label")
        self.accountInput = QtWidgets.QLineEdit(self.centralwidget)
        self.accountInput.setGeometry(QtCore.QRect(128, 190, 178, 35))
        self.accountInput.setStyleSheet("border:2px groove rgb(209,209,209);\n"
"border-radius:10px;\n"
"padding:2px 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft New Tai Lue\";")
        self.accountInput.setClearButtonEnabled(False)
        self.accountInput.setObjectName("accountInput")
        self.psdInput = QtWidgets.QLineEdit(self.centralwidget)
        self.psdInput.setGeometry(QtCore.QRect(128, 223, 178, 35))
        self.psdInput.setStyleSheet("border:2px groove rgb(209,209,209);\n"
"border-radius:10px;\n"
"padding:2px 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft New Tai Lue\";")
        self.psdInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.psdInput.setClearButtonEnabled(True)
        self.psdInput.setObjectName("psdInput")
        self.register_btn = QtWidgets.QPushButton(self.centralwidget)
        self.register_btn.setGeometry(QtCore.QRect(310, 190, 71, 31))
        self.register_btn.setStyleSheet("QPushButton{\n"
"    color: rgb(62,128,195);\n"
"    font: 11pt \"华文楷体\";\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(81,168,255);\n"
"    font: 11pt \"华文楷体\";\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgb(54, 115, 172);\n"
"    font: 11pt \"华文楷体\";\n"
"    border:none;\n"
"}")
        self.register_btn.setObjectName("register_btn")
        self.rememberPsd = QtWidgets.QCheckBox(self.centralwidget)
        self.rememberPsd.setGeometry(QtCore.QRect(128, 267, 91, 16))
        self.rememberPsd.setStyleSheet("font: 11pt \"华文楷体\";\n"
"color: rgb(141, 145, 149);")
        self.rememberPsd.setObjectName("rememberPsd")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(128, 290, 171, 30))
        self.login_btn.setEnabled(False)
        self.login_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(47, 156, 195);\n"
"    border-radius:5px;\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(55, 191, 232);\n"
"    border-radius:5px;\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(61, 207, 255);\n"
"    border-radius:5px;\n"
"    border:none;\n"
"}")
        self.login_btn.setObjectName("login_btn")
        self.avatar_label = QtWidgets.QLabel(self.centralwidget)
        self.avatar_label.setGeometry(QtCore.QRect(15, 190, 100, 100))
        self.avatar_label.setStyleSheet("min-width:  100px;\n"
"max-width:  100px;\n"
"min-height: 100px;\n"
"max-height: 100px;\n"
"\n"
"border-radius: 50px;\n"
"border-width: 0 0 0 0;\n"
"    \n"
"border-image: url(:/Prefix/avatar.png);")
        self.avatar_label.setText("")
        self.avatar_label.setObjectName("avatar_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.login_btn.clicked.connect(MainWindow.login)
        self.register_btn.clicked.connect(MainWindow.register)
        self.accountInput.textChanged['QString'].connect(MainWindow.enable_login_btn)
        self.psdInput.textChanged['QString'].connect(MainWindow.enable_login_btn)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登陆"))
        self.accountInput.setPlaceholderText(_translate("MainWindow", "QQ号码/手机/邮箱"))
        self.psdInput.setPlaceholderText(_translate("MainWindow", "密码"))
        self.register_btn.setText(_translate("MainWindow", "注册账号"))
        self.rememberPsd.setText(_translate("MainWindow", "记住密码"))
        self.login_btn.setText(_translate("MainWindow", "登陆"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

