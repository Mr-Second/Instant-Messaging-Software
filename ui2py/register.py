# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui2py import images_rc


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.setFixedSize(320, 405)
        Register.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"")
        self.top_label = QtWidgets.QLabel(Register)
        self.top_label.setGeometry(QtCore.QRect(0, 0, 320, 171))
        self.top_label.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"border-image: url(:/Prefix/register.png);\n"
"")
        self.top_label.setText("")
        self.top_label.setObjectName("top_label")
        self.register_2 = QtWidgets.QPushButton(Register)
        self.register_2.setGeometry(QtCore.QRect(40, 350, 231, 31))
        self.register_2.setStyleSheet("QPushButton{\n"
"    border-radius:8px;\n"
"    font: 18pt \"宋体\";\n"
"    background-color: rgb(54, 136, 255);\n"
"}\n"
"QPushButton::hover{  \n"
"      font: 18pt \"宋体\";\n"
"    background-color: rgb(48, 124, 235);\n"
"}  \n"
"QPushButton::pressed{  \n"
"    font: 18pt \"宋体\";\n"
"    background-color: rgb(39, 101, 188);\n"
"} ")
        self.register_2.setObjectName("register_2")
        self.layoutWidget = QtWidgets.QWidget(Register)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 190, 233, 143))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.username_input.setMinimumSize(QtCore.QSize(231, 41))
        self.username_input.setStyleSheet("font: 16pt \"Calibri\";\n"
"border-radius:8px;\n"
"background-color: rgb(255, 255, 255);")
        self.username_input.setObjectName("username_input")
        self.verticalLayout.addWidget(self.username_input)
        self.password_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_input.setMinimumSize(QtCore.QSize(231, 41))
        self.password_input.setStyleSheet("font: 16pt \"Calibri\";\n"
"border-radius:8px;\n"
"background-color: rgb(255, 255, 255);")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setClearButtonEnabled(True)
        self.password_input.setObjectName("password_input")
        self.verticalLayout.addWidget(self.password_input)
        self.confirm_psd_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.confirm_psd_input.setMinimumSize(QtCore.QSize(231, 41))
        self.confirm_psd_input.setStyleSheet("font: 16pt \"Calibri\";\n"
"border-radius:8px;\n"
"background-color: rgb(255, 255, 255);")
        self.confirm_psd_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_psd_input.setClearButtonEnabled(True)
        self.confirm_psd_input.setObjectName("confirm_psd_input")
        self.verticalLayout.addWidget(self.confirm_psd_input)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.register_2.setText(_translate("Register", "立即注册"))
        self.username_input.setPlaceholderText(_translate("Register", "昵称"))
        self.password_input.setPlaceholderText(_translate("Register", "密码"))
        self.confirm_psd_input.setPlaceholderText(_translate("Register", "确认密码"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())

