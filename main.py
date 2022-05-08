import sys

from PyQt5 import QtWidgets, uic


class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi('ui/main.ui', self)
        self.submit_button.clicked.connect(self.submit_click)

    def submit_click(self):
        print("OK")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec_())
