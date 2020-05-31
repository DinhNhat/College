import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QEvent, QModelIndex
from PyQt5.QtWidgets import QApplication, QMessageBox
import pandas as pd
import datetime

from Views.Global import GlobalConst
from BUS.ProDegree_BUS import ProDegree_BUS
from BUS.Professor_BUS import Professor_BUS
from BUS.StEnrolment_BUS import Enrolment_BUS
from DTO.Professor import Professor
from model.pandas_model_source import PandasModelSourse

professor_ui = "windowProfessor.ui"
Ui_WindowProfessor, QtBaseClass = uic.loadUiType(professor_ui)

myGloabal = GlobalConst()

ADD = myGloabal.getImage('Add')
UPDATE = myGloabal.getImage('Update')
DELETE = myGloabal.getImage('Delete')


def isGPAUpdateEmpty(course, stId, proId, semester, term):
    if course == "" and stId == "" and proId == "" and semester == "" and term == "":
        return True
    else:
        return False


def showSuccessMessageBox(info):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(info)
    msgBox.setWindowTitle("Success")
    msgBox.setStandardButtons(QMessageBox.Ok)
    x = msgBox.exec_()


def showFailedMessageBox(error):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setWindowTitle("Error")
    msgBox.setText(error)
    msgBox.setStandardButtons(QMessageBox.Retry)
    x = msgBox.exec_()


class WindowProfessor(QtWidgets.QMainWindow, Ui_WindowProfessor):
    def __init__(self, currentUser):
        QtWidgets.QMainWindow.__init__(self)
        Ui_WindowProfessor.__init__(self)
        self.setupUi(self)
        self.__professor_bus = Professor_BUS()
        self.__degree_bus = ProDegree_BUS()
        self.__enrolment_bus = Enrolment_BUS()
        self.__currentUser = currentUser
        self.__parentMainWindow = QtWidgets.QMainWindow()
        self.SetupInfoProfileTab()

    def closeEvent(self, event):
        self.__parentMainWindow.show()

    def setParentMainWin(self, parent):
        self.__parentMainWindow = parent

    def SetupInfoProfileTab(self):
        # print("this is inside Set up info Professor Profile")
        self.lbID.setText(self.__currentUser.ProfessorId)
        self.lbFullName.setText(self.__currentUser.FullName)
        self.lbGender.setText(self.__currentUser.Gender)
        degreeCode = self.__currentUser.DegreeCode
        self.lbDegree.setText(self.__degree_bus.GetDegreeNameByCode(degreeCode))
        self.lineEditEmail.setText(self.__currentUser.Email)
        self.lineEditAddress.setText(self.__currentUser.Address)
        self.lineEditPhone.setText(self.__currentUser.Phone)
        self.labelErrorOldPass.setVisible(False)
        self.labelError.setVisible(False)
        self.LoadDataSource()
        self.setEvents()

    def setEvents(self):
        # Set default widget signals
        self.tvStudentGrade.selectRow(-1)
        # print(self.tvStudentGrade.currentIndex())
        # self.fillOutStudentGPAInfo_TabGPA(self.tvStudentGrade.currentIndex())
        # Event handling
        self.tvStudentGrade.clicked.connect(self.onTableClicked)
        self.btnUpdateGrade.clicked.connect(self.updateStudentGPA)
        # self.lineEditOldPass.editingFinished.connect(self.chekOldPassword)
        # self.lineEditOldPass.keyReleaseEvent.connect(self.chekOldPassword)
        self.lineEditOldPass.installEventFilter(self)
        self.lineEditNewPassRepeat.installEventFilter(self)
        self.btnUpdatePasswd.clicked.connect(self.updatePassword)

    def eventFilter(self, source, event):  # Check condition of updating password
        if source is self.lineEditOldPass:
            if event.type() == QEvent.KeyRelease:
                if self.lineEditOldPass.text() == self.__currentUser.Password:
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
        return super(WindowProfessor, self).eventFilter(source, event)

    def onTableClicked(self, index):
        if index.isValid():
            print('You just click student with index: ', index)
            # st_data = index.row()
            # print(st_data)
            self.fillOutStudentGPAInfo_TabGPA(index)

    def fillOutStudentGPAInfo_TabGPA(self, indexSelected):
        st_data = self.__professor_bus.GetInfoByRowStGradeTable(self.__currentUser.ProfessorId, indexSelected.row())
        print("type of data index: ", type(st_data))
        print(st_data)
        if st_data is not False:
            self.labelCourseTabGrade.setText(st_data[0])
            self.lbStudentIdTabGrade.setText(st_data[1])
            self.labelStFullNameTabGrade.setText(st_data[2])
            self.lbSemesterTabGrade.setText(st_data[3])
            self.lbTermTabGrade.setText(str(st_data[4]))
            self.dsbStGrade.setValue(st_data[5])
        else:
            pass

    def updateStudentGPA(self):
        print("Current selected item index: ", self.tvStudentGrade.currentIndex())
        if self.tvStudentGrade.currentIndex().row() != -1:
            try:
                gpa = self.dsbStGrade.value()
                course = self.labelCourseTabGrade.text()
                stId = self.lbStudentIdTabGrade.text()
                proId = self.__currentUser.ProfessorId
                semester = self.lbSemesterTabGrade.text()
                term = self.lbTermTabGrade.text()
                if not isGPAUpdateEmpty(course, stId, proId, semester, term):
                    if self.__enrolment_bus.updateStudentGPAByConditions(gpa, course, stId, proId, semester, term):
                        self.LoadDataSource()
                        message = "Update GPA successfully"
                        showSuccessMessageBox(message)
                    else:
                        message = "Failed to update student GPA"
                        showFailedMessageBox(message)
                else:
                    message = "No information available to update"
                    showFailedMessageBox(message)
            except Exception as err:
                print("Error occurs in Update GPA")
                print(err)
        else:
            message = "Please choose a row in table below to update."
            showFailedMessageBox(message)

    def updatePassword(self):
        if self.checkIsPasswordMatch():
            # update password by is
            print('You are able to update password by professor id')
            if self.__professor_bus.updatePasswordById(self.lineEditNewPassRepeat.text(),
                                                       self.__currentUser.ProfessorId):
                # showSuccess message box
                message = "Update password successfully"
                showSuccessMessageBox(message)
                proId = self.__currentUser.ProfessorId
                proPasswd = self.lineEditNewPassRepeat.text()
                self.__currentUser = self.__professor_bus.GetProfessorInfoByIdAndPasswd(proId, proPasswd)
                self.resetWidgetTabUpdatePasswd()
            else:
                # show unsuccess message box
                message = "Failed to update password"
                showFailedMessageBox(message)
                self.resetWidgetTabUpdatePasswd()
        else:
            print('You are NOT able to update password by professor id')
            # show unsuccess message box
            message = "Failed to update password"
            showFailedMessageBox(message)
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

    def LoadDataSource(self):
        # load student GPA table
        data = self.__professor_bus.GetStudentGrade(self.__currentUser.ProfessorId)
        dataSource = pd.DataFrame(data, columns=self.__professor_bus.GetColumnHeadersForStudentGradeTb())
        model = PandasModelSourse(dataSource)
        self.tvStudentGrade.setModel(model)
        # print(type(self.__student_bus.GetActive()[0][0]))
        # Load schedule view
        dataSchedule = self.__professor_bus.getRead_Only_Schedule(self.__currentUser.ProfessorId)
        dataSourceSchedule = pd.DataFrame(dataSchedule, columns=self.__professor_bus.getColumnHeadersScheduleTb())
        modelSchedule = PandasModelSourse(dataSourceSchedule)
        self.tvProfessorSchedule.setModel(modelSchedule)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     professor = Professor()
#     professor.ProfessorId = 'p1'
#     professor.Password = '456'
#     pro_bus = Professor_BUS()
#     pro = pro_bus.GetProfessorInfoByIdAndPasswd(professor.ProfessorId, professor.Password)
#     proWin = WindowProfessor(pro)
#     proWin.show()
#     sys.exit(app.exec_())
