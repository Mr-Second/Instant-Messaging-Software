# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emoji_choose.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(506, 261)
        Dialog.setFixedSize(506, 261)
        Dialog.setStyleSheet("QPushButton{\n"
"    font: 14pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(199, 199, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(139, 139, 139);\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 482, 226))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.p9 = QtWidgets.QPushButton(self.layoutWidget)
        self.p9.setMinimumSize(QtCore.QSize(60, 40))
        self.p9.setMaximumSize(QtCore.QSize(60, 40))
        self.p9.setObjectName("p9")
        self.emoji_group = QtWidgets.QButtonGroup(Dialog)
        self.emoji_group.setObjectName("emoji_group")
        self.emoji_group.addButton(self.p9)
        self.gridLayout.addWidget(self.p9, 1, 2, 1, 1)
        self.p11 = QtWidgets.QPushButton(self.layoutWidget)
        self.p11.setMinimumSize(QtCore.QSize(60, 40))
        self.p11.setMaximumSize(QtCore.QSize(60, 40))
        self.p11.setObjectName("p11")
        self.emoji_group.addButton(self.p11)
        self.gridLayout.addWidget(self.p11, 1, 4, 1, 1)
        self.p10 = QtWidgets.QPushButton(self.layoutWidget)
        self.p10.setMinimumSize(QtCore.QSize(60, 40))
        self.p10.setMaximumSize(QtCore.QSize(60, 40))
        self.p10.setObjectName("p10")
        self.emoji_group.addButton(self.p10)
        self.gridLayout.addWidget(self.p10, 1, 3, 1, 1)
        self.p13 = QtWidgets.QPushButton(self.layoutWidget)
        self.p13.setMinimumSize(QtCore.QSize(60, 40))
        self.p13.setMaximumSize(QtCore.QSize(60, 40))
        self.p13.setObjectName("p13")
        self.emoji_group.addButton(self.p13)
        self.gridLayout.addWidget(self.p13, 2, 0, 1, 1)
        self.p3 = QtWidgets.QPushButton(self.layoutWidget)
        self.p3.setMinimumSize(QtCore.QSize(60, 40))
        self.p3.setMaximumSize(QtCore.QSize(60, 40))
        self.p3.setObjectName("p3")
        self.emoji_group.addButton(self.p3)
        self.gridLayout.addWidget(self.p3, 0, 2, 1, 1)
        self.p7 = QtWidgets.QPushButton(self.layoutWidget)
        self.p7.setMinimumSize(QtCore.QSize(60, 40))
        self.p7.setMaximumSize(QtCore.QSize(60, 40))
        self.p7.setObjectName("p7")
        self.emoji_group.addButton(self.p7)
        self.gridLayout.addWidget(self.p7, 1, 0, 1, 1)
        self.p5 = QtWidgets.QPushButton(self.layoutWidget)
        self.p5.setMinimumSize(QtCore.QSize(60, 40))
        self.p5.setMaximumSize(QtCore.QSize(60, 40))
        self.p5.setObjectName("p5")
        self.emoji_group.addButton(self.p5)
        self.gridLayout.addWidget(self.p5, 0, 4, 1, 1)
        self.p1 = QtWidgets.QPushButton(self.layoutWidget)
        self.p1.setMinimumSize(QtCore.QSize(60, 40))
        self.p1.setMaximumSize(QtCore.QSize(60, 16777215))
        self.p1.setStyleSheet("")
        self.p1.setObjectName("p1")
        self.emoji_group.addButton(self.p1)
        self.gridLayout.addWidget(self.p1, 0, 0, 1, 1)
        self.p2 = QtWidgets.QPushButton(self.layoutWidget)
        self.p2.setMinimumSize(QtCore.QSize(60, 40))
        self.p2.setMaximumSize(QtCore.QSize(60, 40))
        self.p2.setObjectName("p2")
        self.emoji_group.addButton(self.p2)
        self.gridLayout.addWidget(self.p2, 0, 1, 1, 1)
        self.p4 = QtWidgets.QPushButton(self.layoutWidget)
        self.p4.setMinimumSize(QtCore.QSize(60, 40))
        self.p4.setMaximumSize(QtCore.QSize(60, 40))
        self.p4.setObjectName("p4")
        self.emoji_group.addButton(self.p4)
        self.gridLayout.addWidget(self.p4, 0, 3, 1, 1)
        self.p6 = QtWidgets.QPushButton(self.layoutWidget)
        self.p6.setMinimumSize(QtCore.QSize(60, 40))
        self.p6.setMaximumSize(QtCore.QSize(60, 40))
        self.p6.setObjectName("p6")
        self.emoji_group.addButton(self.p6)
        self.gridLayout.addWidget(self.p6, 0, 5, 1, 1)
        self.p12 = QtWidgets.QPushButton(self.layoutWidget)
        self.p12.setMinimumSize(QtCore.QSize(60, 40))
        self.p12.setMaximumSize(QtCore.QSize(60, 40))
        self.p12.setObjectName("p12")
        self.emoji_group.addButton(self.p12)
        self.gridLayout.addWidget(self.p12, 1, 5, 1, 1)
        self.p14 = QtWidgets.QPushButton(self.layoutWidget)
        self.p14.setMinimumSize(QtCore.QSize(60, 40))
        self.p14.setMaximumSize(QtCore.QSize(60, 40))
        self.p14.setObjectName("p14")
        self.emoji_group.addButton(self.p14)
        self.gridLayout.addWidget(self.p14, 2, 1, 1, 1)
        self.p20 = QtWidgets.QPushButton(self.layoutWidget)
        self.p20.setMinimumSize(QtCore.QSize(60, 40))
        self.p20.setMaximumSize(QtCore.QSize(60, 40))
        self.p20.setObjectName("p20")
        self.emoji_group.addButton(self.p20)
        self.gridLayout.addWidget(self.p20, 3, 1, 1, 1)
        self.p15 = QtWidgets.QPushButton(self.layoutWidget)
        self.p15.setMinimumSize(QtCore.QSize(60, 40))
        self.p15.setMaximumSize(QtCore.QSize(60, 40))
        self.p15.setObjectName("p15")
        self.emoji_group.addButton(self.p15)
        self.gridLayout.addWidget(self.p15, 2, 2, 1, 1)
        self.p21 = QtWidgets.QPushButton(self.layoutWidget)
        self.p21.setMinimumSize(QtCore.QSize(60, 40))
        self.p21.setMaximumSize(QtCore.QSize(60, 40))
        self.p21.setObjectName("p21")
        self.emoji_group.addButton(self.p21)
        self.gridLayout.addWidget(self.p21, 3, 2, 1, 1)
        self.p16 = QtWidgets.QPushButton(self.layoutWidget)
        self.p16.setMinimumSize(QtCore.QSize(60, 40))
        self.p16.setMaximumSize(QtCore.QSize(60, 40))
        self.p16.setObjectName("p16")
        self.emoji_group.addButton(self.p16)
        self.gridLayout.addWidget(self.p16, 2, 3, 1, 1)
        self.p22 = QtWidgets.QPushButton(self.layoutWidget)
        self.p22.setMinimumSize(QtCore.QSize(60, 40))
        self.p22.setMaximumSize(QtCore.QSize(60, 40))
        self.p22.setObjectName("p22")
        self.emoji_group.addButton(self.p22)
        self.gridLayout.addWidget(self.p22, 3, 3, 1, 1)
        self.p17 = QtWidgets.QPushButton(self.layoutWidget)
        self.p17.setMinimumSize(QtCore.QSize(60, 40))
        self.p17.setMaximumSize(QtCore.QSize(60, 40))
        self.p17.setObjectName("p17")
        self.emoji_group.addButton(self.p17)
        self.gridLayout.addWidget(self.p17, 2, 4, 1, 1)
        self.p18 = QtWidgets.QPushButton(self.layoutWidget)
        self.p18.setMinimumSize(QtCore.QSize(60, 40))
        self.p18.setMaximumSize(QtCore.QSize(60, 40))
        self.p18.setObjectName("p18")
        self.emoji_group.addButton(self.p18)
        self.gridLayout.addWidget(self.p18, 2, 5, 1, 1)
        self.p23 = QtWidgets.QPushButton(self.layoutWidget)
        self.p23.setMinimumSize(QtCore.QSize(60, 40))
        self.p23.setMaximumSize(QtCore.QSize(60, 40))
        self.p23.setObjectName("p23")
        self.emoji_group.addButton(self.p23)
        self.gridLayout.addWidget(self.p23, 3, 4, 1, 1)
        self.p24 = QtWidgets.QPushButton(self.layoutWidget)
        self.p24.setMinimumSize(QtCore.QSize(60, 40))
        self.p24.setMaximumSize(QtCore.QSize(60, 40))
        self.p24.setObjectName("p24")
        self.emoji_group.addButton(self.p24)
        self.gridLayout.addWidget(self.p24, 3, 5, 1, 1)
        self.p19 = QtWidgets.QPushButton(self.layoutWidget)
        self.p19.setMinimumSize(QtCore.QSize(60, 40))
        self.p19.setMaximumSize(QtCore.QSize(60, 40))
        self.p19.setObjectName("p19")
        self.emoji_group.addButton(self.p19)
        self.gridLayout.addWidget(self.p19, 3, 0, 1, 1)
        self.p8 = QtWidgets.QPushButton(self.layoutWidget)
        self.p8.setMinimumSize(QtCore.QSize(60, 40))
        self.p8.setMaximumSize(QtCore.QSize(60, 40))
        self.p8.setObjectName("p8")
        self.emoji_group.addButton(self.p8)
        self.gridLayout.addWidget(self.p8, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Choose Emoji"))
        self.p9.setText(_translate("Dialog", "😄"))
        self.p11.setText(_translate("Dialog", "😀"))
        self.p10.setText(_translate("Dialog", "😡"))
        self.p13.setText(_translate("Dialog", "🙃"))
        self.p3.setText(_translate("Dialog", "😍"))
        self.p7.setText(_translate("Dialog", "😜"))
        self.p5.setText(_translate("Dialog", "😁"))
        self.p1.setText(_translate("Dialog", "😂"))
        self.p2.setText(_translate("Dialog", "😘"))
        self.p4.setText(_translate("Dialog", "😊"))
        self.p6.setText(_translate("Dialog", "😭"))
        self.p12.setText(_translate("Dialog", "😥"))
        self.p14.setText(_translate("Dialog", "😋"))
        self.p20.setText(_translate("Dialog", "😨"))
        self.p15.setText(_translate("Dialog", "👍"))
        self.p21.setText(_translate("Dialog", "🤪"))
        self.p16.setText(_translate("Dialog", "👌"))
        self.p22.setText(_translate("Dialog", "😒"))
        self.p17.setText(_translate("Dialog", "❤"))
        self.p18.setText(_translate("Dialog", "😱"))
        self.p23.setText(_translate("Dialog", "😫"))
        self.p24.setText(_translate("Dialog", "🙂"))
        self.p19.setText(_translate("Dialog", "🐷"))
        self.p8.setText(_translate("Dialog", "😝"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

