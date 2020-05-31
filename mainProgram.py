import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

# from Views.frmLogin import Ui_frmLogin
from syncUi import FormLogin


def main():
    app = QApplication(sys.argv)
    windowLogin = FormLogin()
    windowLogin.show()
    sys.exit(app.exec_())


main()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     windowLogin = FormLogin()
#     windowLogin.show()
#     sys.exit(app.exec_())