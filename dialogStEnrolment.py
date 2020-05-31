import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox
import pandas as pd

from Views.Global import GlobalConst
from BUS.StEnrolment_BUS import Enrolment_BUS
from BUS.Course_BUS import Course_BUS
from DTO.StEnrolment import Enrolment
from model.pandas_model_source import PandasModelSourse

enrolment_ui = "dialogStEnrolment.ui"
Ui_DialogStEnrolment, QtBaseClass = uic.loadUiType(enrolment_ui)

myGloabal = GlobalConst()

ADD = myGloabal.getImage('Add')
UPDATE = myGloabal.getImage('Update')
DELETE = myGloabal.getImage('Delete')


def showFailedMessageBox(error):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setWindowTitle("Error")
    msgBox.setText(error)
    msgBox.setStandardButtons(QMessageBox.Retry)
    x = msgBox.exec_()


def showSuccessMessageBox(info):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(info)
    msgBox.setWindowTitle("Success")
    msgBox.setStandardButtons(QMessageBox.Ok)
    x = msgBox.exec_()


class DialogStEnrolment(QtWidgets.QDialog, Ui_DialogStEnrolment):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_DialogStEnrolment.__init__(self)
        self.setupUi(self)
        self.ACTION_TYPE_ENROLMENT = ADD
        self.__enrolment_bus = Enrolment_BUS()
        self.__course_bus = Course_BUS()
        self.__course_code = ''
        self.__enrolDeleteEmit = Enrolment()
        self.__selectedRowDeleteEmit = False
        self.cbEnrolCourseCode.addItems(self.__course_bus.GetCourseCode())
        self.cbEnrolCourseCode.currentIndexChanged.connect(self.selectionchangeCbCourseCode)
        # Set events
        self.DialogEnrolmentLoad()
        self.SetEvents()

    def SetEvents(self):
        self.tvStEnrolment.selectRow(-1)
        # print("Returns the row this model index refers to: ", self.tvStEnrolment.currentIndex().row())
        # Event handling
        self.rbEnrolAdd.toggled.connect(self.processRbDialogEnrolment)
        self.rbEnrolUpdate.toggled.connect(self.processRbDialogEnrolment)
        self.rbEnrolDelete.toggled.connect(self.processRbDialogEnrolment)
        self.pushButtonEnrol.clicked.connect(self.ProcessData)
        self.tvStEnrolment.clicked.connect(self.onTableClicked)

    def ProcessData(self):
        # Check if the button is ready to take action
        # (other widgets info are emtpy or rdbtn not checked)
        if self.ACTION_TYPE_ENROLMENT == ADD:
            self.EnrolmentInsert()
        elif self.ACTION_TYPE_ENROLMENT == UPDATE:
            self.EnrolmentUpdate()
        elif self.ACTION_TYPE_ENROLMENT == DELETE:
            self.EnrolmentDelete()

    def EnrolmentInsert(self):
        course_code = self.__course_code
        student_id = self.txtEnrolStId.text()
        professor_id = self.txtEnrolProfessorId.text()
        semester = self.txtEnrolSemester.text()
        term = self.spinBoxEnrolTerm.value()
        enrol_date = self.dateEditEnrolmentDate.date().toString("yyyy-MM-dd")
        enrolment = Enrolment(course_code, student_id, professor_id, semester, term, enrol_date)
        # print(enrolment.CourseCode)
        # print(enrolment.StudentId)
        # print(enrolment.ProfessorId)
        # print(enrolment.Semester)
        # print(enrolment.Term)
        # print(enrolment.EnrolmentDate)

        if self.__enrolment_bus.Enrolement_Insert(enrolment):
            print("True")
            showSuccessMessageBox(self.__enrolment_bus.GetExceptType())
            self.LoadDataSource()
            self.resetControls()
        else:
            print("False")
            showFailedMessageBox(self.__enrolment_bus.GetExceptType())
            self.resetControls()

    def EnrolmentUpdate(self):
        pass

    def EnrolmentDelete(self):
        # Check selected row index of table
        if self.tvStEnrolment.currentIndex().row() != -1:
            print(self.__selectedRowDeleteEmit)
            if self.__enrolment_bus.Enrolement_DeleteByKeyCode(self.__enrolDeleteEmit):
                print("True")
                showSuccessMessageBox(self.__enrolment_bus.GetExceptType())
                self.LoadDataSource()
                self.resetControls()
            else:
                print("False")
                showFailedMessageBox(self.__enrolment_bus.GetExceptType())
                self.resetControls()
        else:
            message = "Please select a row in table source to delete"
            showFailedMessageBox(message)

    def processRbDialogEnrolment(self):
        if self.rbEnrolAdd.isChecked():
            # self.ResetControls()
            pushBtnText = self.rbEnrolAdd.text()
            print(pushBtnText)
            self.pushButtonEnrol.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword readOnly FALSE
            self.cbEnrolCourseCode.setEnabled(True)
            self.txtEnrolStId.setEnabled(True)
            self.txtEnrolProfessorId.setEnabled(True)
            self.txtEnrolSemester.setEnabled(True)
            self.spinBoxEnrolTerm.setEnabled(True)
            self.dateEditEnrolmentDate.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_ENROLMENT = ADD
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rbEnrolUpdate.isChecked():
            # self.ResetControls()
            pushBtnText = self.rbEnrolUpdate.text()
            print(pushBtnText)
            self.pushButtonEnrol.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword to readOnly
            self.cbEnrolCourseCode.setEnabled(True)
            self.txtEnrolStId.setEnabled(True)
            self.txtEnrolProfessorId.setEnabled(True)
            self.txtEnrolSemester.setEnabled(True)
            self.spinBoxEnrolTerm.setEnabled(True)
            self.dateEditEnrolmentDate.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_ENROLMENT = UPDATE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rbEnrolDelete.isChecked():
            # self.ResetControls()
            pushBtnText = self.rbEnrolDelete.text()
            print(pushBtnText)
            self.pushButtonEnrol.setText(pushBtnText)
            # Set all info widgets disable
            self.cbEnrolCourseCode.setEnabled(True)
            self.txtEnrolStId.setEnabled(True)
            self.txtEnrolProfessorId.setEnabled(True)
            self.txtEnrolSemester.setEnabled(False)
            self.spinBoxEnrolTerm.setEnabled(False)
            self.dateEditEnrolmentDate.setEnabled(False)
            # Add Image to the button
            self.ACTION_TYPE_ENROLMENT = DELETE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)

    def resetControls(self):
        # reset controls
        self.cbEnrolCourseCode.setCurrentIndex(-1)
        self.txtEnrolStId.setText("")
        self.txtEnrolProfessorId.setText("")
        self.txtEnrolSemester.setText("")
        self.spinBoxEnrolTerm.setValue(0)
        self.__enrolDeleteEmit = Enrolment()
        # self.tvStEnrolment.currentIndex().row()
        self.tvStEnrolment.selectRow(-1)
        # self.dateEditEnrolmentDate.date("000-00-00")

    def DialogEnrolmentLoad(self):
        self.processRbDialogEnrolment()
        self.LoadDataSource()

    # def LoadDataSource(self):
    #     dataSource = self.___proDegree_bus.SelectAllDegree()
    #     self.model = DegreeModel(dataSource)
    #     self.tvProfessorDegree.setModel(self.model)

    def LoadDataSource(self):
        data = self.__enrolment_bus.GetDataSource()
        dataSource = pd.DataFrame(data, columns=self.__enrolment_bus.GetColumnHeaders())
        model = PandasModelSourse(dataSource)
        self.tvStEnrolment.setModel(model)

    def selectionchangeCbCourseCode(self, index):
        self.__course_code = self.cbEnrolCourseCode.currentText()
        print("Current index", index, "selection changed ", self.cbEnrolCourseCode.currentText())

    def onTableClicked(self, index):
        if index.isValid():
            self.getDeleteRow(index)

    def getDeleteRow(self, indexSelected):
        self.__selectedRowDeleteEmit = True
        records = self.__enrolment_bus.SelectAllEnrolment()
        selectedItem = records[indexSelected.row()]
        self.__enrolDeleteEmit.CourseCode = selectedItem[0]
        self.__enrolDeleteEmit.StudentId = selectedItem[1]
        self.__enrolDeleteEmit.ProfessorId = selectedItem[2]
        # print(self.__enrolDeleteEmit.CourseCode)
        # print(self.__enrolDeleteEmit.StudentId)
        # print(self.__enrolDeleteEmit.ProfessorId)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     enrol = DialogStEnrolment()
#     enrol.exec_()
#     sys.exit(app.exec_())
