import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from PyQt5.QtWidgets import QMessageBox, QMainWindow
from Views.Global import GlobalConst
from professorDialog import ProfessorDialog
from studentDialog import StudentDialog
from adminWindow import AdminWindow
from windowProfessor import WindowProfessor
from windowStudent import WindowStudent
from DTO.Admin import Admin
from DTO.Professor import Professor
from DTO.Student import Student
from BUS.Admin_BUS import Admin_BUS
from BUS.Professor_BUS import Professor_BUS
from BUS.Student_BUS import Student_BUS


myGloabal = GlobalConst()

LOGIN = myGloabal.getImage('Login')
EXIT = myGloabal.getImage('Exit')

login_ui = "login.ui"
Ui_formLogin, QtBaseClass = uic.loadUiType(login_ui)


class FormLogin(QMainWindow, Ui_formLogin):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_formLogin.__init__(self)
        self.setupUi(self)
        self.__admin_bus = Admin_BUS()
        self.__professor_bus = Professor_BUS()
        self.__student_bus = Student_BUS()
        # Initialize an admin window
        self.__adminWinDow = None
        self.__professorWindow = None
        self.__studentWindow = None
        # Gloabl variables
        self.USER = ''
        self.SetDefaultWidgetsAndEvents()

    def SetDefaultWidgetsAndEvents(self):
        # Set default widgets
        self.labelPassword.adjustSize()
        self.cbUsers.setCurrentIndex(-1)
        # self.btnLogin.pressed.connect(self.showSomething)
        # Events handling
        self.btnLogin.clicked.connect(self.ShowUser)
        self.btnExit.clicked.connect(self.close)
        self.cbUsers.currentIndexChanged.connect(self.Selectionchange)

    def ShowUser(self):
        if self.__admin_bus.GetConnectionStatus():
            print("Connection works")
        else:
            print(self.__admin_bus.GetExceptType())

        if self.USER == 'Admin':
            adminId = self.lineEditUsername.text()
            adminPasswd = self.lineEditPassword.text()
            admin = Admin()
            admin.SetAdminId(adminId)
            admin.SetAdminPasswd(adminPasswd)
            if self.__admin_bus.ValidateAdmin(admin):
                self.ResetWidget()
                # Get admin info
                admin = self.__admin_bus.getAdminInfoByIdAndPassword(admin.GetAdminId(), admin.GetAdminPasswd())
                self.__adminWinDow = AdminWindow(admin)
                self.__adminWinDow.show()
                self.__adminWinDow.setParentMainWin(self)
                self.hide()
            else:
                invalid_admin = 'Invalid Admin. Login id or password wrong. Try again'
                self.ShowDialogErrorTypes(invalid_admin)
        elif self.USER == 'Professor':
           try:
               ID = self.lineEditUsername.text()
               password = self.lineEditPassword.text()
               professor = Professor()
               professor.ProfessorId = ID
               professor.Password = password
               if self.__professor_bus.ValidateProfessor(professor):
                   self.ResetWidget()
                   pro = self.__professor_bus.GetProfessorInfoByIdAndPasswd(professor.ProfessorId, professor.Password)
                   # print(pro)
                   self.__professorWindow = WindowProfessor(pro)
                   self.__professorWindow.show()
                   self.__professorWindow.setParentMainWin(self)
                   self.hide()
               else:
                   invalid_professor = 'Invalid Professor. Login id or password wrong. Try again'
                   self.ShowDialogErrorTypes(invalid_professor)
           except Exception as err:
               print(err)
        elif self.USER == 'Student':
            ID = self.lineEditUsername.text()
            password = self.lineEditPassword.text()
            student = Student()
            student.StId = ID
            student.StPassword = password
            if self.__student_bus.validateStudent(student):
                self.ResetWidget()
                stu = self.__student_bus.getStudentInfoByIdAndPassword(student.StId, student.StPassword)
                # print(pro)
                self.__studentWindow = WindowStudent(stu)
                self.__studentWindow.show()
                self.__studentWindow.setParentMainWin(self)
                self.hide()
            else:
                invalid_professor = 'Invalid Student. Login id or password wrong. Try again'
                self.ShowDialogErrorTypes(invalid_professor)
        elif self.USER == '':
            # Empty input will raise an ERROR by showing a warning dialog
            print('Empty input')
            empty = 'Empty input'
            self.ShowDialogErrorTypes(empty)
        elif self.USER == 'Staff':
            print('This role has NOT been created yet')
            unfinished = 'This role has NOT been created yet'
            self.ShowDialogErrorTypes(unfinished)

    def closeEvent(self, *args, **kwargs):
        sys.exit()

    def Selectionchange(self):
        print(self.cbUsers.currentText())
        self.USER = self.cbUsers.currentText()
        groupBoxTitle = self.USER + " Login"
        print(groupBoxTitle)
        self.ChangeUserLabelFont(groupBoxTitle)

    def ChangeUserLabelFont(self, gbTitle):
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setStrikeOut(False)
        self.groupBoxLogin.setFont(font)
        self.groupBoxLogin.setTitle(gbTitle)
        # self.labelPassword.adjustSize()

    def ResetWidget(self):
        self.lineEditUsername.setText("")
        self.lineEditPassword.setText("")
        self.cbUsers.setCurrentIndex(-1)

    def ShowDialogErrorTypes(self, type_err):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle("Error")
        msgBox.setText(type_err)
        # closeButton = msgBox.addButton(QMessageBox.Close)
        msgBox.exec_()
        # self.hide()  # Disable the parent form
        # msgBox.close()
        # self.show()


# app = QtWidgets.QApplication(sys.argv)
# try:
#     ui = FormLogin()
#     ui.show()
# except Exception as er:
#     print(er)
#     print("this is exception")
# app.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = FormLogin()
    ui.show()
    app.exec_()
    sys.exit(app.exec_())
