import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox
import pandas as pd

from Views.Global import GlobalConst
from BUS.Classroom_BUS import Classroom_BUS
from DTO.Classroom import Classroom
from model.pandas_model_source import PandasModelSourse

classroom_ui = "dialogClassroom.ui"
Ui_DialogClassroom, QtBaseClass = uic.loadUiType(classroom_ui)

myGloabal = GlobalConst()

ADD = myGloabal.getImage('Add')
UPDATE = myGloabal.getImage('Update')
DELETE = myGloabal.getImage('Delete')


class DialogClassroom(QtWidgets.QDialog, Ui_DialogClassroom):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_DialogClassroom.__init__(self)
        self.setupUi(self)
        self.ACTION_TYPE_CLASSROOM = ADD
        self.___classroom_bus = Classroom_BUS()
        self.__classroom = Classroom()
        self.rdbtnAddClassroom.setChecked(True)
        # Set events
        self.SetEvents()
        self.load()
        self.LoadDataSource()

    def SetEvents(self):
        # Event handling
        self.rdbtnAddClassroom.toggled.connect(self.processRbDialogClassroom)
        self.rdbtnUpdateClassroom.toggled.connect(self.processRbDialogClassroom)
        self.rdbtnDeleteClassroom.toggled.connect(self.processRbDialogClassroom)
        self.pushBtnClassroom.clicked.connect(self.ProcessData)

    def ProcessData(self):
        # Check if the button is ready to take action
        # (other widgets info are emtpy or rdbtn not checked)
        if self.ACTION_TYPE_CLASSROOM == ADD:
            self.ClassroomInsert()
        elif self.ACTION_TYPE_CLASSROOM == UPDATE:
            self.ClassroomUpdate()
        elif self.ACTION_TYPE_CLASSROOM == DELETE:
            self.ClassroomDelete()

    def ClassroomInsert(self):
        code = self.txtClassCode.text()
        num = self.txtClassNum.text()
        buildingName = self.txtBuildingName.text()
        location = self.txtLocationName.text()

        self.__classroom.SetClassroomCode(code)
        self.__classroom.SetClassroomNumber(num)
        self.__classroom.SetBuildingName(buildingName)
        self.__classroom.SetLocationName(location)
        # print(self.__classroom.GetClassroomCode())
        # print(self.__classroom.GetClassroomNumber())
        # print(self.__classroom.GetBuildingName())
        # print(self.__classroom.GetLocationName())
        if self.___classroom_bus.Classroom_Insert(self.__classroom):
            print("True")
            self.ShowSuccessMessageBox(self.___classroom_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.___classroom_bus.GetExceptType())
            self.ResetControls()

    def ClassroomUpdate(self):
        code = self.txtClassCode.text()
        num = self.txtClassNum.text()
        buildingName = self.txtBuildingName.text()
        location = self.txtLocationName.text()

        self.__classroom.SetClassroomCode(code)
        self.__classroom.SetClassroomNumber(num)
        self.__classroom.SetBuildingName(buildingName)
        self.__classroom.SetLocationName(location)
        print(self.__classroom.GetClassroomCode())
        print(self.__classroom.GetClassroomNumber())
        print(self.__classroom.GetBuildingName())
        print(self.__classroom.GetLocationName())
        if self.___classroom_bus.Classroom_Update(self.__classroom):
            print("True")
            self.ShowSuccessMessageBox(self.___classroom_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.___classroom_bus.GetExceptType())
            self.ResetControls()

    def ClassroomDelete(self):
        code = self.txtClassCode.text()
        self.__classroom.SetClassroomCode(code)
        print(self.__classroom.GetClassroomCode())
        if self.___classroom_bus.Classroom_Delete(self.__classroom):
            print("True")
            self.ShowSuccessMessageBox(self.___classroom_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            err_code = self.___classroom_bus.GetExceptType()
            self.ShowFailedMessageBox(err_code)
            self.ResetControls()

    def processRbDialogClassroom(self):
        if self.rdbtnAddClassroom.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnAddClassroom.text()
            print(pushBtnText)
            self.pushBtnClassroom.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword readOnly FALSE
            self.txtClassCode.setEnabled(True)
            self.txtClassNum.setEnabled(True)
            self.txtBuildingName.setEnabled(True)
            self.txtLocationName.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_CLASSROOM = ADD
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnUpdateClassroom.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnUpdateClassroom.text()
            print(pushBtnText)
            self.pushBtnClassroom.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword to readOnly
            self.txtClassCode.setDisabled(False)
            self.txtClassNum.setEnabled(True)
            self.txtBuildingName.setEnabled(True)
            self.txtLocationName.setEnabled(True)
            # self.txtAdminName.setReadOnly(False)
            # self.txtAdminPassword.setReadOnly(True)
            # self.ckbActiveAdmin.setCheckable(True)
            # Add Image to the button
            self.ACTION_TYPE_CLASSROOM = UPDATE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnDeleteClassroom.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnDeleteClassroom.text()
            print(pushBtnText)
            self.pushBtnClassroom.setText(pushBtnText)
            # Set all info widgets disable
            self.txtClassCode.setDisabled(False)
            self.txtClassNum.setDisabled(True)
            self.txtBuildingName.setDisabled(True)
            self.txtLocationName.setDisabled(True)
            # Add Image to the button
            self.ACTION_TYPE_CLASSROOM = DELETE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)

    def ResetControls(self):
        # reset controls
        self.txtClassCode.setText("")
        self.txtClassNum.setText("")
        self.txtBuildingName.setText("")
        self.txtLocationName.setText("")

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

    def load(self):
        self.processRbDialogClassroom()
        self.LoadDataSource()

    def LoadDataSource(self):
        dataSource = self.___classroom_bus.SelectAllClassroom()
        dataSource = pd.DataFrame(dataSource, columns=self.___classroom_bus.GetColumnHeaders())
        self.model = PandasModelSourse(dataSource)
        self.tvClassroom.setModel(self.model)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     classroom = DialogClassroom()
#     classroom.exec_()
#     sys.exit(app.exec_())
