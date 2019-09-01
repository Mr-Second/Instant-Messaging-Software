# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(584, 467)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/images/chatting.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color:rgb(40,50,50);")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 571, 451))
        self.widget.setStyleSheet("QFrame\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"    border:none;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::hover,QToolButton::hover{  \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  \n"
"                                 stop: 0 #758385, stop: 0.5 #122C39,  \n"
"                                 stop: 1.0 #0E7788);  \n"
"    border-color: #11505C;  \n"
"\n"
"}  \n"
"QPushButton::pressed,QToolButton::pressed{  \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  \n"
"                                 stop: 0 #969B9C, stop: 0.5 #16354B,  \n"
"                                 stop: 1.0 #244F76);  \n"
"    border-color: #11505C;\n"
"\n"
"} ")
        self.widget.setObjectName("widget")
        self.tip_Label = QtWidgets.QLabel(self.widget)
        self.tip_Label.setGeometry(QtCore.QRect(440, 0, 131, 31))
        self.tip_Label.setStyleSheet("font: 14pt \"华文楷体\";\n"
"color: rgb(255, 85, 0);")
        self.tip_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.tip_Label.setObjectName("tip_Label")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(436, 340, 135, 109))
        self.groupBox.setStyleSheet("font: 14pt \"华文楷体\";\n"
"color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(40, 20, 61, 81))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.start_btn = QtWidgets.QPushButton(self.splitter)
        self.start_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.splitter)
        self.stop_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.stop_btn.setObjectName("stop_btn")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 0, 421, 31))
        self.label.setStyleSheet("font: 14pt \"华文楷体\";\n"
"color: rgb(255, 85, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(436, 40, 135, 191))
        self.tableWidget.setStyleSheet("font: 11pt \"华文楷体\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.chat_record = QtWidgets.QTextEdit(self.widget)
        self.chat_record.setEnabled(True)
        self.chat_record.setGeometry(QtCore.QRect(10, 40, 421, 407))
        self.chat_record.setMinimumSize(QtCore.QSize(421, 0))
        self.chat_record.setObjectName("chat_record")
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setGeometry(QtCore.QRect(436, 240, 135, 91))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setStyleSheet("font: 14pt \"华文楷体\";\n"
"color: rgb(255, 85, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Server"))
        self.tip_Label.setText(_translate("Dialog", "实时在线用户"))
        self.groupBox.setTitle(_translate("Dialog", "Action"))
        self.start_btn.setText(_translate("Dialog", "Start"))
        self.stop_btn.setText(_translate("Dialog", "Stop"))
        self.label.setText(_translate("Dialog", "实时日志记录"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "UserName"))
        self.label_2.setText(_translate("Dialog", "Date_Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

