import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
import pandas as pd

from Views.Global import GlobalConst
from BUS.Course_BUS import Course_BUS
from BUS.AcademicProgram_BUS import AcaProgram_BUS
from DTO.Course import Course
from model.pandas_model_source import PandasModelSourse

course_ui = "dialogCourse.ui"
Ui_DialogCourse, QtBaseClass = uic.loadUiType(course_ui)

myGloabal = GlobalConst()

ADD = myGloabal.getImage('Add')
UPDATE = myGloabal.getImage('Update')
DELETE = myGloabal.getImage('Delete')


class DialogCourse(QtWidgets.QDialog, Ui_DialogCourse):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_DialogCourse.__init__(self)
        self.setupUi(self)
        self.ACTION_TYPE_COURSE = ADD
        self.__course_bus = Course_BUS()
        self.__program_bus = AcaProgram_BUS()
        self.__course = Course()
        self.__cbProgramName = ''
        self.cbCourseAcaProgram.addItems(self.__program_bus.GetAllAcaProgramName())
        self.cbCourseAcaProgram.currentIndexChanged.connect(self.selectionchangecbCourseAcaProgram)
        # Set events
        self.SetEvents()
        self.DialogCourseLoad()

    def SetEvents(self):
        # Event handling
        self.rdbtnAddCourse.toggled.connect(self.processRbDialogCourse)
        self.rdbtnUpdateCourse.toggled.connect(self.processRbDialogCourse)
        self.rdbtnDeleteCourse.toggled.connect(self.processRbDialogCourse)
        self.pushBtnCourse.clicked.connect(self.ProcessData)

    def ProcessData(self):
        # Check if the button is ready to take action
        # (other widgets info are emtpy or rdbtn not checked)
        if self.ACTION_TYPE_COURSE == ADD:
            self.CourseInsert()
        elif self.ACTION_TYPE_COURSE == UPDATE:
            self.CourseUpdate()
        elif self.ACTION_TYPE_COURSE == DELETE:
            self.CourseDelete()

    def CourseInsert(self):
        code = self.txtCourseNumber.text()
        desc = self.txtCourseDesc.text()
        credit = self.spbCourseCredit.value()
        outline = self.txtCourseOutline.text()
        programCode = self.__program_bus.GetProgramCodeByName(self.__cbProgramName)

        self.__course.Code = code
        self.__course.Description = desc
        self.__course.Credit = credit
        self.__course.Outline = outline
        self.__course.ProgramCode = programCode
        # print(self.__course.Code)
        # print(self.__course.Description)
        # print(self.__course.Credit)
        # print(self.__course.Outline)
        # print(self.__course.ProgramCode)

        if self.__course_bus.Course_Insert(self.__course):
            print("True")
            self.ShowSuccessMessageBox(self.__course_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__course_bus.GetExceptType())
            self.ResetControls()

    def CourseUpdate(self):
        code = self.txtCourseNumber.text()
        desc = self.txtCourseDesc.text()
        credit = self.spbCourseCredit.value()
        outline = self.txtCourseOutline.text()
        programCode = self.__program_bus.GetProgramCodeByName(self.__cbProgramName)

        self.__course.Code = code
        self.__course.Description = desc
        self.__course.Credit = credit
        self.__course.Outline = outline
        self.__course.ProgramCode = programCode
        print(self.__course.Code)
        print(self.__course.Description)
        print(self.__course.Credit)
        print(self.__course.Outline)
        print(self.__course.ProgramCode)

        if self.__course_bus.Course_Update(self.__course):
            print("True")
            self.ShowSuccessMessageBox(self.__course_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__course_bus.GetExceptType())
            self.ResetControls()

    def CourseDelete(self):
        code = self.txtCourseNumber.text()
        self.__course.Code = code
        print(self.__course.Code)

        if self.__course_bus.Course_Delete(self.__course):
            print("True")
            self.ShowSuccessMessageBox(self.__course_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__course_bus.GetExceptType())
            self.ResetControls()

    def processRbDialogCourse(self):
        if self.rdbtnAddCourse.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnAddCourse.text()
            print(pushBtnText)
            self.pushBtnCourse.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword readOnly FALSE
            self.txtCourseNumber.setEnabled(True)
            self.txtCourseDesc.setEnabled(True)
            self.spbCourseCredit.setEnabled(True)
            self.cbCourseAcaProgram.setEnabled(True)
            self.txtCourseOutline.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_COURSE = ADD
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnUpdateCourse.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnUpdateCourse.text()
            print(pushBtnText)
            self.pushBtnCourse.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword to readOnly
            self.txtCourseNumber.setEnabled(True)
            self.txtCourseDesc.setEnabled(True)
            self.spbCourseCredit.setEnabled(True)
            self.cbCourseAcaProgram.setEnabled(True)
            self.txtCourseOutline.setEnabled(True)
            # self.txtAdminName.setReadOnly(False)
            # self.txtAdminPassword.setReadOnly(True)
            # self.ckbActiveAdmin.setCheckable(True)
            # Add Image to the button
            self.ACTION_TYPE_COURSE = UPDATE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnDeleteCourse.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnDeleteCourse.text()
            print(pushBtnText)
            self.pushBtnCourse.setText(pushBtnText)
            # Set all info widgets disable
            self.txtCourseNumber.setEnabled(True)
            self.txtCourseDesc.setEnabled(False)
            self.spbCourseCredit.setEnabled(False)
            self.cbCourseAcaProgram.setEnabled(False)
            self.txtCourseOutline.setEnabled(False)
            # Add Image to the button
            self.ACTION_TYPE_COURSE = DELETE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)

    def ResetControls(self):
        # reset controls
        self.txtCourseNumber.setText("")
        self.txtCourseDesc.setText("")
        self.spbCourseCredit.setValue(0)
        self.cbCourseAcaProgram.setCurrentIndex(-1)
        self.txtCourseOutline.setText("")

    def selectionchangecbCourseAcaProgram(self, index):
        self.__cbProgramName = self.cbCourseAcaProgram.currentText()
        print("Current index", index, "selection changed ", self.cbCourseAcaProgram.currentText())

    def ShowSuccessMessageBox(self, info):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(info)
        msgBox.setWindowTitle("Success")
        msgBox.setStandardButtons(QMessageBox.Ok)
        x = msgBox.exec_()

    def ShowFailedMessageBox(self, error):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setWindowTitle("Error")
        msgBox.setText(error)
        msgBox.setStandardButtons(QMessageBox.Retry)
        x = msgBox.exec_()

    def DialogCourseLoad(self):
        self.processRbDialogCourse()
        self.LoadDataSource()

    def LoadDataSource(self):
        data = self.__course_bus.GetDataSource()
        dataSource = pd.DataFrame(data, columns=self.__course_bus.GetColumnHeaders())
        self.model = PandasModelSourse(dataSource)
        self.tvCourse.setModel(self.model)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     course = DialogCourse()
#     course.exec_()
#     sys.exit(app.exec_())