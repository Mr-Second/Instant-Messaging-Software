from ui2py.emoji_choose import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QApplication


class Emoji(QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.emoji_group.buttonClicked.connect(self.set_current_emoji)
        self.emoji = None

    def set_current_emoji(self, button):
        print(button.text())
        self.emoji = button.text()
        self.close()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    emoji = Emoji()
    emoji.exec_()
    sys.exit(app.exec_())