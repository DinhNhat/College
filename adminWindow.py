import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QMessageBox

from adminDialog import AdminDialog
from professorDialog import ProfessorDialog
from studentDialog import StudentDialog
from dialogCourse import DialogCourse
from dialogClassroom import DialogClassroom
from dialogAcaProgram import DialogAcaProgram
from dialogProDegree import DialogProDegree
from dialogStEnrolment import DialogStEnrolment
from Schedule import DialogSchedule
from dialogAdUpdatePass import DialogAdminUpdatePass

admin_ui = "adminWindow.ui"
Ui_AdminWindow, QtBaseClass = uic.loadUiType(admin_ui)


class AdminWindow(QtWidgets.QMainWindow, Ui_AdminWindow):
    def __init__(self, currentUser):
        QtWidgets.QMainWindow.__init__(self)
        Ui_AdminWindow.__init__(self)
        self.setupUi(self)
        # set resource dialogs
        self.__currentAdmin = currentUser
        self.__dialogAdmin = AdminDialog()
        self.__dialogProfessor = ProfessorDialog()
        self.__dialogStudent = StudentDialog()
        self.__dialogCourse = DialogCourse()
        self.__dialogClassroom = DialogClassroom()
        self.__dialogAcaProgram = DialogAcaProgram()
        self.__dialogProDegree = DialogProDegree()
        self.__dialogEnrolment = None
        self.__dialogSchedule = DialogSchedule()
        self.__dialogAdUpdatePass = None
        self.SetActionMenubars()
        self.__parentMainWindow = QtWidgets.QMainWindow()

    def SetActionMenubars(self):
        self.actionAdmin.triggered.connect(self.triggerDialogAdmin)
        self.actionProfessor.triggered.connect(self.triggerDialogProfessor)
        self.actionStudent.triggered.connect(self.triggerDialogStudent)
        self.actionStaff.triggered.connect(self.triggerDialogStaff)
        self.actionAcademic_Program.triggered.connect(self.triggerDialogAcaProgram)
        self.actionCourse.triggered.connect(self.triggerDialogCourse)
        self.actionProfessor_Degree.triggered.connect(self.triggerDialogProDegree)
        self.actionClassroom.triggered.connect(self.triggerDialogClassroom)
        self.actionStudentEnrolment.triggered.connect(self.triggerDialogStEnrolment)
        self.actionSchedule.triggered.connect(self.triggerDialogSchedule)
        self.actionClose.triggered.connect(self.closeEvent)
        self.actionChange_password.triggered.connect(self.triggerDialogAdUpdatePass)

    def closeEvent(self, event):
        self.reOpenParentWindow()
        self.__parentMainWindow.show()

    def reOpenParentWindow(self):
        self.__parentMainWindow.show()
        print('You just closed admin window')

    def setParentMainWin(self, parent):
        self.__parentMainWindow = parent

    def triggerDialogAdmin(self):
        print('you just open admin dialog')
        self.__dialogAdmin.exec_()
        # self.mdiAreaAdmin.setActiveSubWindow(self.subwindowAdmin)

    def triggerDialogProfessor(self):
        print('you just open dialog professor')
        self.__dialogProfessor.exec_()

    def triggerDialogStudent(self):
        print('you just open dialog student')
        self.__dialogStudent.exec_()

    def triggerDialogStaff(self):
        print('you just open dialog staff')

    def triggerDialogAcaProgram(self):
        print('you just open dialog academic program')
        self.__dialogAcaProgram.exec_()

    def triggerDialogCourse(self):
        print('you just open dialog course')
        self.__dialogCourse.exec_()

    def triggerDialogProDegree(self):
        print('you just open dialog professor degree')
        self.__dialogProDegree.exec_()

    def triggerDialogClassroom(self):
        print('you just open dialog classroom')
        self.__dialogClassroom.exec_()

    def triggerDialogStEnrolment(self):
        print('you just open dialog student enrolment')
        self.__dialogEnrolment = DialogStEnrolment()
        self.__dialogEnrolment.exec_()

    def triggerDialogSchedule(self):
        print('you just open dialog Schedule')
        self.__dialogSchedule.exec_()

    def triggerDialogAdUpdatePass(self):
        print('You just opened dialog admin update password')
        self.__dialogAdUpdatePass = DialogAdminUpdatePass(self.__currentAdmin)
        self.__dialogAdUpdatePass.exec_()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     admin = AdminWindow()
#     admin.show()
#     sys.exit(app.exec_())
