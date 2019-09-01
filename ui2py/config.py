# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui2py import images_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(355, 238)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 44, 91))
        self.label.setStyleSheet("background-color: rgb(60,78,173);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(311, 41, 44, 50))
        self.label_3.setStyleSheet("background-color: rgb(60,78,173);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.ipInput = QtWidgets.QLineEdit(Dialog)
        self.ipInput.setGeometry(QtCore.QRect(90, 114, 178, 35))
        self.ipInput.setStyleSheet("border:2px groove rgb(209,209,209);\n"
"border-radius:10px;\n"
"padding:2px 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft New Tai Lue\";")
        self.ipInput.setClearButtonEnabled(False)
        self.ipInput.setObjectName("ipInput")
        self.portInput = QtWidgets.QLineEdit(Dialog)
        self.portInput.setGeometry(QtCore.QRect(90, 147, 178, 35))
        self.portInput.setStyleSheet("border:2px groove rgb(209,209,209);\n"
"border-radius:10px;\n"
"padding:2px 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft New Tai Lue\";")
        self.portInput.setClearButtonEnabled(True)
        self.portInput.setObjectName("portInput")
        self.config_btn = QtWidgets.QPushButton(Dialog)
        self.config_btn.setGeometry(QtCore.QRect(90, 190, 171, 30))
        self.config_btn.setStyleSheet("QPushButton{\n"
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
        self.config_btn.setObjectName("config_btn")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(44, 0, 267, 91))
        self.label_4.setStyleSheet("background-color: rgb(60,78,173);\n"
"font: 75 24pt \"Microsoft PhagsPa\";\n"
"color: rgb(0, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.close_btn = QtWidgets.QPushButton(Dialog)
        self.close_btn.setGeometry(QtCore.QRect(311, 0, 44, 41))
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

        self.retranslateUi(Dialog)
        self.close_btn.clicked.connect(Dialog.on_button_close_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "配置"))
        self.ipInput.setPlaceholderText(_translate("Dialog", "服务器IP地址"))
        self.portInput.setPlaceholderText(_translate("Dialog", "服务器端口号"))
        self.config_btn.setText(_translate("Dialog", "配置"))
        self.label_4.setText(_translate("Dialog", "Config"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

