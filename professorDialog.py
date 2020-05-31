import sys

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox

from Views.Global import GlobalConst
from dialogCourse import DialogCourse
from BUS.Professor_BUS import Professor_BUS
from DTO.Professor import Professor
from BUS.ProDegree_BUS import ProDegree_BUS
from model.pandas_model_source import PandasModelSourse

professor_ui = "dialogProfessor.ui"
Ui_ProfessorDialog, QtBaseClass = uic.loadUiType(professor_ui)

myGloabal = GlobalConst()

ADD = myGloabal.getImage('Add')
UPDATE = myGloabal.getImage('Update')
DELETE = myGloabal.getImage('Delete')


class ProfessorDialog(QtWidgets.QDialog, Ui_ProfessorDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_ProfessorDialog.__init__(self)
        self.setupUi(self)
        self.__professor_bus = Professor_BUS()
        self.__professor = Professor()
        self.__proDegree_bus = ProDegree_BUS()
        self.__cbDegreeName = ''
        self.cbDegreeCodePro.addItems(self.__proDegree_bus.GetAllDegreeName())
        self.cbDegreeCodePro.currentIndexChanged.connect(self.selectionchangeCbDegree)
        self.ACTION_TYPE_PROFESSOR = ADD
        self.rdbtnAddProfessor.setChecked(True)
        self.setEvents()
        self.DialogProfessorLoad()

    def setEvents(self):
        # Event handling
        self.rdbtnAddProfessor.toggled.connect(self.processRbDialogProfessor)
        self.rdbtnUpdateProfessor.toggled.connect(self.processRbDialogProfessor)
        self.rdbtnDeleteProfessor.toggled.connect(self.processRbDialogProfessor)
        # self.rdbtnAddProfessor.toggled.connect(self.processRdbtnProTab)
        # self.rdbtnUpdateProfessor.toggled.connect(self.processRdbtnProTab)
        # self.rdbtnDeleteProfessor.toggled.connect(self.processRdbtnProTab)
        # self.rdbtnAddStudent.toggled.connect(self.processRdbtnStudentTab)
        # self.rdbtnUpdateStudent.toggled.connect(self.processRdbtnStudentTab)
        # self.rdbtnDeleteStudent.toggled.connect(self.processRdbtnStudentTab)
        # self.rdbtnAddCourse.toggled.connect(self.processRdbtnCourseTab)
        # self.rdbtnUpdateCourse.toggled.connect(self.processRdbtnCourseTab)
        # self.rdbtnDeleteCourse.toggled.connect(self.processRdbtnCourseTab)
        self.pushBtnProfessor.clicked.connect(self.ProcessData)

    def ProcessData(self):
        if self.ACTION_TYPE_PROFESSOR == ADD:
            self.ProfessorInsert()
        elif self.ACTION_TYPE_PROFESSOR == UPDATE:
            self.ProfessorUpdate()
        elif self.ACTION_TYPE_PROFESSOR == DELETE:
            self.ProfessorDelete()

    def ProfessorInsert(self):
        id = self.txtProfessorId.text()
        fullname = self.txtProfessorName.text()
        gender = self.cbGenderPro.currentText()
        email = self.txtProfessorEmail.text()
        adress =  self.txtProfessorAddress.text()
        phone = self.txtProfessorPhone.text()
        degreeName = self.__cbDegreeName
        # print(degreeName)
        degreeCode = self.__proDegree_bus.GetDegreeCode(degreeName)
        if self.rdDialogProActiveYes.isChecked() and not self.rdDialogProActiveNo.isChecked():
            active = 1
        elif not self.rdDialogProActiveYes.isChecked() and self.rdDialogProActiveNo.isChecked():
            active = 0

        self.__professor.ProfessorId = id
        self.__professor.FullName = fullname
        self.__professor.Gender = gender
        self.__professor.Email = email
        self.__professor.Address = adress
        self.__professor.Phone = phone
        self.__professor.Active = active
        self.__professor.DegreeCode = degreeCode
        # print(self.__professor.GetProfessorId())
        # print(self.__professor.GetProfessorFullName())
        # print(self.__professor.GetProfessorGender())
        # print(self.__professor.GetProfessorEmail())
        # print(self.__professor.GetProfessorAddress())
        # print(self.__professor.GetProfessorPhone())
        # print(self.__professor.GetProfessorIsActive())
        # print(self.__professor.GetProfessorDegreeCode())
        if self.__professor_bus.Professor_Insert(self.__professor):
            print("True")
            self.ShowSuccessMessageBox(self.__professor_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__professor_bus.GetExceptType())
            self.ResetControls()

    def ProfessorUpdate(self):
        id = self.txtProfessorId.text()
        fullname = self.txtProfessorName.text()
        gender = self.cbGenderPro.currentText()
        email = self.txtProfessorEmail.text()
        adress =  self.txtProfessorAddress.text()
        phone = self.txtProfessorPhone.text()
        degreeName = self.cbDegreeCodePro.currentText()
        print(degreeName)
        degreeCode = self.__proDegree_bus.GetDegreeCode(degreeName)
        if self.rdDialogProActiveYes.isChecked() and not self.rdDialogProActiveNo.isChecked():
            active = 1
        elif not self.rdDialogProActiveYes.isChecked() and self.rdDialogProActiveNo.isChecked():
            active = 0

        self.__professor.ProfessorId = id
        self.__professor.FullName = fullname
        self.__professor.Gender = gender
        self.__professor.Email = email
        self.__professor.Address = adress
        self.__professor.Phone = phone
        self.__professor.Active = active
        self.__professor.DegreeCode = degreeCode

        # print(self.__professor.GetProfessorId())
        # print(self.__professor.GetProfessorFullName())
        # print(self.__professor.GetProfessorGender())
        # print(self.__professor.GetProfessorEmail())
        # print(self.__professor.GetProfessorAddress())
        # print(self.__professor.GetProfessorPhone())
        # print(self.__professor.GetProfessorIsActive())
        # print(self.__professor.GetProfessorDegreeCode())

        if self.__professor_bus.Professor_Update(self.__professor):
            print("True")
            self.ShowSuccessMessageBox(self.__professor_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__professor_bus.GetExceptType())
            self.ResetControls()

    def ProfessorDelete(self):
        id = self.txtProfessorId.text()
        self.__professor.ProfessorId = id
        # print(self.__professor.GetProfessorId())

        if self.__professor_bus.Professor_Delete(self.__professor):
            print("True")
            self.ShowSuccessMessageBox(self.__professor_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__professor_bus.GetExceptType())
            self.ResetControls()

    def selectionchangeCbDegree(self, index):
        self.__cbDegreeName = self.cbDegreeCodePro.currentText()
        print("Current index", index, "selection changed ", self.cbDegreeCodePro.currentText())

    def processRbDialogProfessor(self):
        if self.rdbtnAddProfessor.isChecked():
            pushBtnText = self.rdbtnAddProfessor.text()
            print(pushBtnText)
            self.pushBtnProfessor.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword readOnly FALSE
            self.txtProfessorId.setEnabled(True)
            self.txtProfessorName.setEnabled(True)
            self.cbGenderPro.setEnabled(True)
            self.txtProfessorEmail.setEnabled(True)
            self.txtProfessorAddress.setEnabled(True)
            self.txtProfessorPhone.setEnabled(True)
            self.cbDegreeCodePro.setEnabled(True)
            self.rdDialogProActiveYes.setEnabled(True)
            self.rdDialogProActiveNo.setEnabled(True)

            # Add Image to the button
            self.ACTION_TYPE_PROFESSOR = ADD
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnUpdateProfessor.isChecked():
            pushBtnText = self.rdbtnUpdateProfessor.text()
            print(pushBtnText)
            self.pushBtnProfessor.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword to readOnly
            self.txtProfessorId.setEnabled(True)
            self.txtProfessorName.setEnabled(True)
            self.cbGenderPro.setEnabled(True)
            self.txtProfessorEmail.setEnabled(True)
            self.txtProfessorAddress.setEnabled(True)
            self.txtProfessorPhone.setEnabled(True)
            self.cbDegreeCodePro.setEnabled(True)
            self.rdDialogProActiveYes.setEnabled(True)
            self.rdDialogProActiveNo.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_PROFESSOR = UPDATE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnDeleteProfessor.isChecked():
            pushBtnText = self.rdbtnDeleteProfessor.text()
            print(pushBtnText)
            self.pushBtnProfessor.setText(pushBtnText)
            # Set all info widgets disable
            self.txtProfessorId.setEnabled(True)
            self.txtProfessorName.setEnabled(False)
            self.cbGenderPro.setEnabled(False)
            self.txtProfessorEmail.setEnabled(False)
            self.txtProfessorAddress.setEnabled(False)
            self.txtProfessorPhone.setEnabled(False)
            self.cbDegreeCodePro.setEnabled(False)
            self.rdDialogProActiveYes.setEnabled(False)
            self.rdDialogProActiveNo.setEnabled(False)
            # Add Image to the button
            self.ACTION_TYPE_PROFESSOR = DELETE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)

    def ResetControls(self):
        # reset controls
        self.txtProfessorId.setText("")
        self.txtProfessorName.setText("")
        self.cbGenderPro.setCurrentIndex(0)
        self.txtProfessorEmail.setText("")
        self.txtProfessorAddress.setText("")
        self.txtProfessorPhone.setText("")
        self.cbDegreeCodePro.setCurrentIndex(0)
        self.rdDialogProActiveYes.setChecked(True)
        self.rdDialogProActiveNo.setChecked(False)

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


    def DialogProfessorLoad(self):
        self.processRbDialogProfessor()
        self.LoadDataSource()

    def LoadDataSource(self):
        data = self.__professor_bus.GetDataSource()
        dataSource = pd.DataFrame(data, columns=self.__professor_bus.GetColumnHeaders())
        self.model = PandasModelSourse(dataSource)
        self.tvProfessor.setModel(self.model)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     pro = ProfessorDialog()
#     pro.exec_()
#     sys.exit(app.exec_())