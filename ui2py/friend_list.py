# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'friend_list.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui2py import images_rc


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(805, 602)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 0, 201, 58))
        self.label.setStyleSheet("background-color: rgb(22, 144, 237);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(261, 17, 282, 41))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setStyleSheet("background-color: rgb(22, 144, 237);\n"
"font: 14pt \"华文行楷\";\n"
"color: rgb(0, 0, 0);")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 0, 283, 17))
        self.label_3.setStyleSheet("background-color: rgb(22, 144, 237);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(543, 0, 200, 58))
        self.label_4.setStyleSheet("background-color: rgb(22, 144, 237);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 61, 58))
        self.label_7.setStyleSheet("border-image: url(:/Prefix/head2.png);\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(743, 29, 61, 29))
        self.label_8.setStyleSheet("background-color: rgb(22, 144, 237);\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.close_btn = QtWidgets.QPushButton(Dialog)
        self.close_btn.setGeometry(QtCore.QRect(742, -2, 63, 32))
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
        self.friendlist = QtWidgets.QListWidget(Dialog)
        self.friendlist.setGeometry(QtCore.QRect(0, 58, 261, 544))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.friendlist.setFont(font)
        self.friendlist.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 20pt \"华文楷体\";")
        self.friendlist.setFlow(QtWidgets.QListView.TopToBottom)
        self.friendlist.setResizeMode(QtWidgets.QListView.Adjust)
        self.friendlist.setObjectName("friendlist")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.friendlist.addItem(item)
        self.chat_area = QtWidgets.QTextEdit(Dialog)
        self.chat_area.setEnabled(True)
        self.chat_area.setGeometry(QtCore.QRect(260, 58, 544, 401))
        self.chat_area.setStyleSheet("")
        self.chat_area.setObjectName("chat_area")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(260, 489, 544, 81))
        self.textEdit.setStyleSheet("background:transparent;\n"
"border-width:0;\n"
"border-style:outset;\n"
"font: 12pt \"华文楷体\";\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.choose_emoji_btn = QtWidgets.QPushButton(Dialog)
        self.choose_emoji_btn.setGeometry(QtCore.QRect(260, 459, 30, 30))
        self.choose_emoji_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255,0);\n"
"    border-image: url(:/Prefix/emoji.png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(225, 225, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(185, 185, 185);\n"
"}")
        self.choose_emoji_btn.setText("")
        self.choose_emoji_btn.setObjectName("choose_emoji_btn")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(293, 459, 381, 30))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.send_btn = QtWidgets.QPushButton(Dialog)
        self.send_btn.setGeometry(QtCore.QRect(720, 570, 84, 32))
        self.send_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(1, 136, 251);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 14pt \"幼圆\";\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(40,156,255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 129, 239);\n"
"}")
        self.send_btn.setObjectName("send_btn")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(680, 460, 121, 30))
        self.checkBox.setStyleSheet("font: 14pt \"华文楷体\";")
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Dialog)
        self.close_btn.clicked.connect(Dialog.on_close_button_clicked)
        self.choose_emoji_btn.clicked.connect(Dialog.choose_emoji)
        self.send_btn.clicked.connect(Dialog.send_words)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.friendlist.isSortingEnabled()
        self.friendlist.setSortingEnabled(False)
        item = self.friendlist.item(0)
        item.setText(_translate("Dialog", "好友列表"))
        self.friendlist.setSortingEnabled(__sortingEnabled)
        self.send_btn.setText(_translate("Dialog", "发送"))
        self.checkBox.setText(_translate("Dialog", "To everyone"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

