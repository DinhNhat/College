import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox
import pandas as pd
import datetime

from Views.Global import GlobalConst
from BUS.Student_BUS import Student_BUS
from BUS.AcademicProgram_BUS import AcaProgram_BUS
from DTO.Student import Student
from model.pandas_model_source import PandasModelSourse

student_ui = "dialogStudent.ui"
Ui_StudentDialog, QtBaseClass = uic.loadUiType(student_ui)

myGloabal = GlobalConst()

ADD = myGloabal.getImage('Add')
UPDATE = myGloabal.getImage('Update')
DELETE = myGloabal.getImage('Delete')


class StudentDialog(QtWidgets.QDialog, Ui_StudentDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_StudentDialog.__init__(self)
        self.setupUi(self)
        self.__student_bus = Student_BUS()
        self.__student = Student()
        self.__aca_program_bus = AcaProgram_BUS()
        self.__cbStCountries = ''
        self.cbStCountry.addItems(myGloabal.GetCountriesList())
        self.__cbStProgramName = ''
        self.cbStAcaProgram.addItems(self.__aca_program_bus.GetAllAcaProgramName())
        self.cbStAcaProgram.currentIndexChanged.connect(self.selectionchangeCbAcaProgram)
        self.cbStCountry.currentIndexChanged.connect(self.selectionchangeCbCountries)
        self.ACTION_TYPE_STUDENT = ADD
        self.rdbtnAddStudent.setChecked(True)
        self.setEvents()
        self.DialogStLoad()

    def setEvents(self):
        # Event handling
        self.rdbtnAddStudent.toggled.connect(self.processRbDialogStudent)
        self.rdbtnUpdateStudent.toggled.connect(self.processRbDialogStudent)
        self.rdbtnDeleteStudent.toggled.connect(self.processRbDialogStudent)
        # self.rdbtnAddProfessor.toggled.connect(self.processRdbtnProTab)
        # self.rdbtnUpdateProfessor.toggled.connect(self.processRdbtnProTab)
        # self.rdbtnDeleteProfessor.toggled.connect(self.processRdbtnProTab)
        # self.rdbtnAddStudent.toggled.connect(self.processRdbtnStudentTab)
        # self.rdbtnUpdateStudent.toggled.connect(self.processRdbtnStudentTab)
        # self.rdbtnDeleteStudent.toggled.connect(self.processRdbtnStudentTab)
        # self.rdbtnAddCourse.toggled.connect(self.processRdbtnCourseTab)
        # self.rdbtnUpdateCourse.toggled.connect(self.processRdbtnCourseTab)
        # self.rdbtnDeleteCourse.toggled.connect(self.processRdbtnCourseTab)
        self.pushBtnStudent.clicked.connect(self.ProcessData)

    def ProcessData(self):
        if self.ACTION_TYPE_STUDENT == ADD:
            self.StudentInsert()
        elif self.ACTION_TYPE_STUDENT == UPDATE:
            self.StudentUpdate()
        elif self.ACTION_TYPE_STUDENT == DELETE:
            self.StudentDelete()

    def StudentInsert(self):
        # print('You just clicked Add student')
        global gender
        id = self.txtStudentId.text()
        fullname = self.txtStudentName.text()
        if self.rdStGenderMale.isChecked() and not self.rdStGenderFemale.isChecked():
            gender = 'male'
        elif not self.rdStGenderMale.isChecked() and self.rdStGenderFemale.isChecked():
            gender = 'female'
        dateOfBirth = self.dateEditStDateOfBirth.date().toString("yyyy-MM-dd")
        country = self.__cbStCountries
        address = self.txtStAddress.text()
        email = self.txtStEmail.text()
        if self.rdStActiveYes.isChecked() and not self.rdStActiveNo.isChecked():
            active = 1
        elif not self.rdStActiveYes.isChecked() and self.rdStActiveNo.isChecked():
            active = 0
        registeredDate = self.dateStRegisterDate.date().toString("yyyy-MM-dd")
        programCode = self.__aca_program_bus.GetProgramCodeByName(self.__cbStProgramName)
        # print(id)
        # print(fullname)
        # print(gender)
        # print(type(dateOfBirth))
        # print(dateOfBirth)
        # print(country)
        # print(address)
        # print(email)
        # print(active)
        # print(registeredDate)
        # print(programCode)
        # print(degreeName)

        self.__student.StId = id
        self.__student.StFullname = fullname
        self.__student.StGender = gender
        self.__student.StDateOfBirth = dateOfBirth
        self.__student.StCountry = country
        self.__student.StCurrentAddress = address
        self.__student.StEmail = email
        self.__student.StActive = active
        self.__student.StRegisteredDate = registeredDate
        self.__student.StProgramCode = programCode

        print(self.__student.StId)
        print(self.__student.StFullname)
        print(self.__student.StGender)
        print(self.__student.StDateOfBirth)
        print(self.__student.StCountry)
        print(self.__student.StCurrentAddress)
        print(self.__student.StEmail)
        print(self.__student.StActive)
        print(self.__student.StRegisteredDate)
        print(self.__student.StProgramCode)

        if self.__student_bus.Student_Insert(self.__student):
            print("True")
            self.ShowSuccessMessageBox(self.__student_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__student_bus.GetExceptType())
            self.ResetControls()

    def StudentUpdate(self):
        global gender
        id = self.txtStudentId.text()
        fullname = self.txtStudentName.text()
        if self.rdStGenderMale.isChecked() and not self.rdStGenderFemale.isChecked():
            gender = 'male'
        elif not self.rdStGenderMale.isChecked() and self.rdStGenderFemale.isChecked():
            gender = 'female'
        dateOfBirth = self.dateEditStDateOfBirth.date().toString("yyyy-MM-dd")
        country = self.__cbStCountries
        address = self.txtStAddress.text()
        email = self.txtStEmail.text()
        if self.rdStActiveYes.isChecked() and not self.rdStActiveNo.isChecked():
            active = 1
        elif not self.rdStActiveYes.isChecked() and self.rdStActiveNo.isChecked():
            active = 0
        registeredDate = self.dateStRegisterDate.date().toString("yyyy-MM-dd")
        programCode = self.__aca_program_bus.GetProgramCodeByName(self.__cbStProgramName)
        # print(id)
        # print(fullname)
        # print(gender)
        # print(type(dateOfBirth))
        # print(dateOfBirth)
        # print(country)
        # print(address)
        # print(email)
        # print(active)
        # print(registeredDate)
        # print(programCode)
        # print(degreeName)
        self.__student.StId = id
        self.__student.StFullname = fullname
        self.__student.StGender = gender
        self.__student.StDateOfBirth = dateOfBirth
        self.__student.StCountry = country
        self.__student.StCurrentAddress = address
        self.__student.StEmail = email
        self.__student.StActive = active
        self.__student.StRegisteredDate = registeredDate
        self.__student.StProgramCode = programCode
        # print(self.__student.StId)
        # print(self.__student.StFullname)
        # print(self.__student.StGender)
        # print(self.__student.StDateOfBirth)
        # print(self.__student.StCountry)
        # print(self.__student.StCurrentAddress)
        # print(self.__student.StEmail)
        # print(self.__student.StActive)
        # print(self.__student.StRegisteredDate)
        # print(self.__student.StProgramCode)
        if self.__student_bus.Student_Update(self.__student):
            print("True")
            self.ShowSuccessMessageBox(self.__student_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__student_bus.GetExceptType())
            self.ResetControls()

    def StudentDelete(self):
        id = self.txtStudentId.text()
        # print(id)
        # print(fullname)
        # print(gender)
        # print(type(dateOfBirth))
        # print(dateOfBirth)
        # print(country)
        # print(address)
        # print(email)
        # print(active)
        # print(registeredDate)
        # print(programCode)
        # print(degreeName)
        self.__student.StId = id
        print(self.__student.StId)

        if self.__student_bus.Student_Delete(self.__student):
            print("True")
            self.ShowSuccessMessageBox(self.__student_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__student_bus.GetExceptType())
            self.ResetControls()

    def selectionchangeCbAcaProgram(self, index):
        self.__cbStProgramName = self.cbStAcaProgram.currentText()
        print("Current index", index, "selection changed ", self.cbStAcaProgram.currentText())

    def selectionchangeCbCountries(self, index):
        self.__cbStCountries = self.cbStCountry.currentText()
        print("Current index", index, "selection changed ", self.cbStCountry.currentText())

    def processRbDialogStudent(self):
        if self.rdbtnAddStudent.isChecked():
            pushBtnText = self.rdbtnAddStudent.text()
            print(pushBtnText)
            self.pushBtnStudent.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword readOnly FALSE
            self.txtStudentId.setEnabled(True)
            self.txtStudentName.setEnabled(True)
            self.rdStGenderMale.setEnabled(True)
            self.rdStGenderFemale.setEnabled(True)
            self.dateEditStDateOfBirth.setEnabled(True)
            self.cbStCountry.setEnabled(True)
            self.txtStAddress.setEnabled(True)
            self.txtStEmail.setEnabled(True)
            self.cbStAcaProgram.setEnabled(True)
            self.dateStRegisterDate.setEnabled(True)
            self.rdStActiveYes.setEnabled(True)
            self.rdStActiveNo.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_STUDENT = ADD
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnUpdateStudent.isChecked():
            pushBtnText = self.rdbtnUpdateStudent.text()
            print(pushBtnText)
            self.pushBtnStudent.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword to readOnly
            self.txtStudentId.setEnabled(True)
            self.txtStudentName.setEnabled(True)
            self.rdStGenderMale.setEnabled(True)
            self.rdStGenderFemale.setEnabled(True)
            self.dateEditStDateOfBirth.setEnabled(True)
            self.cbStCountry.setEnabled(True)
            self.txtStAddress.setEnabled(True)
            self.txtStEmail.setEnabled(True)
            self.cbStAcaProgram.setEnabled(True)
            self.dateStRegisterDate.setEnabled(True)
            self.rdStActiveYes.setEnabled(True)
            self.rdStActiveNo.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_STUDENT = UPDATE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnDeleteStudent.isChecked():
            pushBtnText = self.rdbtnDeleteStudent.text()
            print(pushBtnText)
            self.pushBtnStudent.setText(pushBtnText)
            # Set all info widgets disable
            self.txtStudentId.setEnabled(True)
            self.txtStudentName.setEnabled(False)
            self.rdStGenderMale.setEnabled(False)
            self.rdStGenderFemale.setEnabled(False)
            self.dateEditStDateOfBirth.setEnabled(False)
            self.cbStCountry.setEnabled(False)
            self.txtStAddress.setEnabled(False)
            self.txtStEmail.setEnabled(False)
            self.cbStAcaProgram.setEnabled(False)
            self.dateStRegisterDate.setEnabled(False)
            self.rdStActiveYes.setEnabled(False)
            self.rdStActiveNo.setEnabled(False)
            # Add Image to the button
            self.ACTION_TYPE_STUDENT = DELETE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)

    def ResetControls(self):
        # reset controls
        self.txtStudentId.setText("")
        self.txtStudentName.setText("")
        self.cbStCountry.setCurrentIndex(-1)
        self.cbStAcaProgram.setCurrentIndex(-1)
        self.rdStGenderMale.setChecked(True)
        self.rdStGenderFemale.setChecked(False)
        # self.dateEditStDateOfBirth.setDate('0000-00-00')
        # self.dateStRegisterDate.setDate('0000-00-00')
        self.txtStAddress.setText("")
        self.txtStEmail.setText("")
        # self.dateStRegisterDate.setDate('2000-01-01')
        self.rdStActiveYes.setChecked(True)
        self.rdStActiveNo.setChecked(False)

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

    def DialogStLoad(self):
        self.processRbDialogStudent()
        self.LoadDataSource()

    def LoadDataSource(self):
        data = self.__student_bus.GetDatSource()
        dataSource = pd.DataFrame(data, columns=self.__student_bus.GetColumnHeaders())
        self.model = PandasModelSourse(dataSource)
        self.tvStudent.setModel(self.model)
        # print(type(self.__student_bus.GetActive()[0][0]))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     st = StudentDialog()
#     st.exec_()
#     sys.exit(app.exec_())