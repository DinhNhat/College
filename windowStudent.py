import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QMessageBox
import pandas as pd

from Views.Global import GlobalConst
from BUS.Student_BUS import Student_BUS
from BUS.AcademicProgram_BUS import AcaProgram_BUS
from BUS.Schedule_BUS import Schedule_BUS
from DTO.Student import Student
from model.pandas_model_source import PandasModelSourse

student_ui = "windowStudent.ui"
Ui_WindowStudent, QtBaseClass = uic.loadUiType(student_ui)

myGloabal = GlobalConst()

ADD = myGloabal.getImage('Add')
UPDATE = myGloabal.getImage('Update')
DELETE = myGloabal.getImage('Delete')


class WindowStudent(QtWidgets.QMainWindow, Ui_WindowStudent):
    def __init__(self, currentUser):
        QtWidgets.QMainWindow.__init__(self)
        Ui_WindowStudent.__init__(self)
        self.setupUi(self)
        self.__student_bus = Student_BUS()
        self.__acaProgram_bus = AcaProgram_BUS()
        self.__stSchedule_bus = Schedule_BUS()
        self.__currentUser = currentUser
        self.__parentMainWindow = QtWidgets.QMainWindow()
        self.SetupInfoProfileTab()

    def closeEvent(self, event):
        self.__parentMainWindow.show()

    def setParentMainWin(self, parent):
        self.__parentMainWindow = parent

    def SetupInfoProfileTab(self):
        print("this is inside Set up info Professor Profile")
        # self.__currentUser
        self.labelStudentId.setText(self.__currentUser.StId)
        self.lbStudentFullName.setText(self.__currentUser.StFullname)
        self.lbStudentGender.setText(self.__currentUser.StGender)
        dateOfBirth = str(self.__currentUser.StDateOfBirth)
        self.lbStudentDateOfBirth.setText(dateOfBirth)
        self.lbStudentCountry.setText(self.__currentUser.StCountry)
        self.lbStudentAddress.setText(self.__currentUser.StCurrentAddress)
        self.lbStudentEmail.setText(self.__currentUser.StEmail)
        registeredDate = str(self.__currentUser.StRegisteredDate)
        self.lbStudentRegisteredDate.setText(registeredDate)
        academic_name = self.__acaProgram_bus.getProgramNameByCode(self.__currentUser.StProgramCode)
        if academic_name is not False:
            self.lbStudentAcaProgram.setText(academic_name)
        else:
            self.lbStudentAcaProgram.setText("NOT AVAILABLE")

        self.labelErrorOldPass.setVisible(False)
        self.labelError.setVisible(False)
        self.LoadDataSource()
        self.setEvents()

    def setEvents(self):
        # Event handling
        self.lineEditOldPass.installEventFilter(self)
        self.lineEditNewPassRepeat.installEventFilter(self)
        self.btnUpdatePasswd.clicked.connect(self.updatePassword)

    # Related actions in tab update password
    def eventFilter(self, source, event):  # Check condition of creating new password
        if source is self.lineEditOldPass:
            if event.type() == QEvent.KeyRelease:
                if self.lineEditOldPass.text() == self.__currentUser.StPassword:
                    self.labelErrorOldPass.setAutoFillBackground(True)
                    self.labelErrorOldPass.setVisible(True)
                    self.labelErrorOldPass.setText("Old password correct")
                    self.labelErrorOldPass.setStyleSheet("QLabel { background-color: rgb(0,255,0); }")
                else:
                    self.labelErrorOldPass.setAutoFillBackground(True)
                    self.labelErrorOldPass.setVisible(True)
                    self.labelErrorOldPass.setText("Old password Incorrect")
                    self.labelErrorOldPass.setStyleSheet("QLabel { background-color: rgb(255,0,0); }")
                    print('Old password incorrect')
        elif source is self.lineEditNewPassRepeat:
            if event.type() == QEvent.KeyRelease:
                if self.lineEditNewPassRepeat.text() == self.lineEditNewPass.text():
                    self.labelError.setAutoFillBackground(True)
                    self.labelError.setVisible(True)
                    self.labelError.setText("Password repeat correctly")
                    self.labelError.setStyleSheet("QLabel { background-color: rgb(0,255,0); }")
                else:
                    self.labelError.setAutoFillBackground(True)
                    self.labelError.setVisible(True)
                    self.labelError.setText("Password repeat Incorrectly")
                    self.labelError.setStyleSheet("QLabel { background-color: rgb(255,0,0); }")
        return super(WindowStudent, self).eventFilter(source, event)

    def updatePassword(self):
        if self.checkIsPasswordMatch():
            # update password by is
            print('You are able to update password by professor id')
            if self.__student_bus.updatePasswordById(self.lineEditNewPassRepeat.text(),
                                                     self.__currentUser.StId):
                # showSuccess message box
                message = "Update password successfully"
                self.showSuccessMessageBox(message)
                stId = self.__currentUser.StId
                stPassword = self.lineEditNewPassRepeat.text()
                self.__currentUser = self.__student_bus.getStudentInfoByIdAndPassword(stId, stPassword)
                self.resetWidgetTabUpdatePasswd()
            else:
                # show unsuccess message box
                message = "Failed to update password"
                self.showFailedMessageBox(message)
                self.resetWidgetTabUpdatePasswd()
        else:
            print('You are NOT able to update password by professor id')
            # show unsuccess message box
            message = "Failed to update password"
            self.showFailedMessageBox(message)
            self.resetWidgetTabUpdatePasswd()

    def checkIsPasswordMatch(self):
        if self.lineEditOldPass.text() != "" and self.lineEditNewPass.text() != "" \
                and self.lineEditNewPassRepeat.text() != "":
            if self.labelErrorOldPass.text() == "Old password correct" and self.labelError.text() == "Password repeat " \
                                                                                                     "correctly":
                return True
        return False

    def resetWidgetTabUpdatePasswd(self):
        self.lineEditOldPass.setText("")
        self.lineEditNewPass.setText("")
        self.lineEditNewPassRepeat.setText("")
        self.labelErrorOldPass.setVisible(False)
        self.labelError.setVisible(False)

    def showSuccessMessageBox(self, info):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(info)
        msgBox.setWindowTitle("Success")
        msgBox.setStandardButtons(QMessageBox.Ok)
        x = msgBox.exec_()

    def showFailedMessageBox(self, error):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setWindowTitle("Error")
        msgBox.setText(error)
        msgBox.setStandardButtons(QMessageBox.Retry)
        x = msgBox.exec_()

    def LoadDataSource(self):
        # print(type(self.__student_bus.GetActive()[0][0]))
        # Load schedule view
        dataSchedule = self.__student_bus.getRead_Only_StudentSchedule(self.__currentUser.StId)
        dataSourceSchedule = pd.DataFrame(dataSchedule, columns=self.__student_bus.getColumnHeadersForScheduleTb())
        modelSchedule = PandasModelSourse(dataSourceSchedule)
        self.tvStudentSchedule.setModel(modelSchedule)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     student_bus = Student_BUS()
#     current = Student()
#     current.StId = 'st1'
#     current.StPassword = 'nathan'
#     current = student_bus.getStudentInfoByIdAndPassword(current.StId, current.StPassword)
#     print(current)
#     student = WindowStudent(current)
#     student.show()
#     sys.exit(app.exec_())
