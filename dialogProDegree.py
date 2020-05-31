import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox
import pandas as pd

from Views.Global import GlobalConst
from BUS.ProDegree_BUS import ProDegree_BUS
from DTO.ProfessorDegree import ProfessorDegree
from model.pandas_model_source import PandasModelSourse

# classroom_ui = "dialogClassroom.ui"
# Ui_DialogClassroom, QtBaseClass = uic.loadUiType(classroom_ui)

myGloabal = GlobalConst()

ADD = myGloabal.getImage('Add')
UPDATE = myGloabal.getImage('Update')
DELETE = myGloabal.getImage('Delete')

proDegree_ui = "dialogProDegree.ui"
Ui_DialogProDegree, QtBaseClass = uic.loadUiType(proDegree_ui)


class DialogProDegree(QtWidgets.QDialog, Ui_DialogProDegree):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_DialogProDegree.__init__(self)
        self.setupUi(self)
        self.ACTION_TYPE_PRODEGREE = ADD
        self.___proDegree_bus = ProDegree_BUS()
        self.__proDegree = ProfessorDegree()
        self.rdAddDegree.setChecked(True)
        # Set events
        self.SetEvents()
        self.DialogDegreeLoad()

    def SetEvents(self):
        # Event handling
        self.rdAddDegree.toggled.connect(self.processRbDialogDegree)
        self.rdbUpdateDegree.toggled.connect(self.processRbDialogDegree)
        self.rdDeleteDegree.toggled.connect(self.processRbDialogDegree)
        self.pushBtnDegree.clicked.connect(self.ProcessData)

    def ProcessData(self):
        # Check if the button is ready to take action
        # (other widgets info are emtpy or rdbtn not checked)
        if self.ACTION_TYPE_PRODEGREE == ADD:
            self.DegreeInsert()
        elif self.ACTION_TYPE_PRODEGREE == UPDATE:
            self.DegreeUpdate()
        elif self.ACTION_TYPE_PRODEGREE == DELETE:
            self.DegreeDelete()

    def DegreeInsert(self):
        code = self.txtDegreeCode.text()
        name = self.txtDegreeName.text()
        salary_index = self.dsbSalaryIndex.value()
        degree = ProfessorDegree(code, name, salary_index)
        # self.__proDegree.SetDegreeCode(code)
        # self.__proDegree.SetDegreeName(name)
        # self.__proDegree.SetSalaryIndex(salary_index)
        # print(degree.GetDegreeCode())
        # print(degree.GetDegreeName())
        # print(degree.GetSalaryIndex())

        if self.___proDegree_bus.Degree_Insert(degree):
            print("True")
            self.ShowSuccessMessageBox(self.___proDegree_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.___proDegree_bus.GetExceptType())
            self.ResetControls()

    def DegreeUpdate(self):
        code = self.txtDegreeCode.text()
        name = self.txtDegreeName.text()
        salary_index = self.dsbSalaryIndex.value()
        self.__proDegree.SetDegreeCode(code)
        self.__proDegree.SetDegreeName(name)
        self.__proDegree.SetSalaryIndex(salary_index)
        # print(self.__proDegree.GetDegreeCode())
        # print(self.__proDegree.GetDegreeName())
        # print(self.__proDegree.GetSalaryIndex())

        if self.___proDegree_bus.Degree_Update(self.__proDegree):
            print("True")
            self.ShowSuccessMessageBox(self.___proDegree_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.___proDegree_bus.GetExceptType())
            self.ResetControls()

    def DegreeDelete(self):
        code = self.txtDegreeCode.text()
        self.__proDegree.SetDegreeCode(code)

        print(self.__proDegree.GetDegreeCode())

        if self.___proDegree_bus.Degree_Delete(self.__proDegree):
            print("True")
            self.ShowSuccessMessageBox(self.___proDegree_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.___proDegree_bus.GetExceptType())
            self.ResetControls()

    def processRbDialogDegree(self):
        if self.rdAddDegree.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdAddDegree.text()
            print(pushBtnText)
            self.pushBtnDegree.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword readOnly FALSE
            self.txtDegreeCode.setEnabled(True)
            self.txtDegreeName.setEnabled(True)
            self.dsbSalaryIndex.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_PRODEGREE = ADD
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbUpdateDegree.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbUpdateDegree.text()
            print(pushBtnText)
            self.pushBtnDegree.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword to readOnly
            self.txtDegreeCode.setEnabled(True)
            self.txtDegreeName.setEnabled(True)
            self.dsbSalaryIndex.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_PRODEGREE = UPDATE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdDeleteDegree.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdDeleteDegree.text()
            print(pushBtnText)
            self.pushBtnDegree.setText(pushBtnText)
            # Set all info widgets disable
            self.txtDegreeCode.setEnabled(True)
            self.txtDegreeName.setEnabled(False)
            self.dsbSalaryIndex.setEnabled(False)
            # Add Image to the button
            self.ACTION_TYPE_PRODEGREE = DELETE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)

    def ResetControls(self):
        # reset controls
        self.txtDegreeCode.setText("")
        self.txtDegreeName.setText("")
        self.dsbSalaryIndex.setValue(0.00)

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

    def DialogDegreeLoad(self):
        self.processRbDialogDegree()
        self.LoadDataSource()

    # def LoadDataSource(self):
    #     dataSource = self.___proDegree_bus.SelectAllDegree()
    #     self.model = DegreeModel(dataSource)
    #     self.tvProfessorDegree.setModel(self.model)

    def LoadDataSource(self):
        data = self.___proDegree_bus.SelectAllDegree()
        dataSource = pd.DataFrame(data, columns=self.___proDegree_bus.GetColumnHeaders())
        self.model = PandasModelSourse(dataSource)
        self.tvProfessorDegree.setModel(self.model)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     degree = DialogProDegree()
#     degree.exec_()
#     sys.exit(app.exec_())
