from ui2py.config import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore


class ConfigWin(QDialog, Ui_Dialog):
    # 发送给主窗口的两个参数
    TwoParameter = QtCore.pyqtSignal(str, int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.config_btn.clicked.connect(self.config)

    def on_button_close_clicked(self):
        self.reject()  # QDialog关闭

    def config(self):
        ip_addr = self.ipInput.text()
        port = int(self.portInput.text())
        self.TwoParameter.emit(ip_addr, port)
        self.close()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    config = ConfigWin()
    config.exec_()
    sys.exit(app.exec_())
