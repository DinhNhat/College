import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox
import pandas as pd

from Views.Global import GlobalConst
from BUS.AcademicProgram_BUS import AcaProgram_BUS
from DTO.AcademicProgram import AcademicProgram
from model.pandas_model_source import PandasModelSourse

myGloabal = GlobalConst()

ADD = myGloabal.getImage('Add')
UPDATE = myGloabal.getImage('Update')
DELETE = myGloabal.getImage('Delete')

academicProgram_ui = "dialogAcaProgram.ui"
Ui_DialogAcaProgram, QtBaseClass = uic.loadUiType(academicProgram_ui)


class DialogAcaProgram(QtWidgets.QDialog, Ui_DialogAcaProgram):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_DialogAcaProgram.__init__(self)
        self.setupUi(self)
        self.ACTION_TYPE_ACADEMICPROGRAM = ADD
        self.___aca_program_bus = AcaProgram_BUS()
        self.__aca_program = AcademicProgram()
        self.rdbtnAddAcaProgram.setChecked(True)
        # Set events
        self.SetEvents()
        self.DialogProgramLoad()

    def SetEvents(self):
        # Event handling
        self.rdbtnAddAcaProgram.toggled.connect(self.processRbDialogAcaProgram)
        self.rdbtnUpdateAcaProgram.toggled.connect(self.processRbDialogAcaProgram)
        self.rdbtnDeleteAcaProgram.toggled.connect(self.processRbDialogAcaProgram)
        self.pushBtnAcaProgram.clicked.connect(self.ProcessData)

    def ProcessData(self):
        # Check if the button is ready to take action
        # (other widgets info are emtpy or rdbtn not checked)
        if self.ACTION_TYPE_ACADEMICPROGRAM == ADD:
            self.AcProgramInsert()
        elif self.ACTION_TYPE_ACADEMICPROGRAM == UPDATE:
            self.AcaProgramUpdate()
        elif self.ACTION_TYPE_ACADEMICPROGRAM == DELETE:
            self.AcaProgramDelete()

    def AcProgramInsert(self):
        global status
        code = self.txtProgramCode.text()
        name = self.txtProgramName.text()
        tuition = self.dsbProgramTuition.value()
        if self.rdAcaStatusOpen.isChecked() and not self.rdAcaStatusClose.isChecked():
            status = 'open'
        elif not self.rdAcaStatusOpen.isChecked() and self.rdAcaStatusClose.isChecked():
            status = 'closed'

        self.__aca_program.SetProgramCode(code)
        self.__aca_program.SetProgramName(name)
        self.__aca_program.SetTuition(tuition)
        self.__aca_program.SetProStatus(status)
        # print(self.__aca_program.GetProgramCode())
        # print(self.__aca_program.GetProgramName())
        # print(self.__aca_program.GetTuition())
        # print(self.__aca_program.GetProStatus())
        if self.___aca_program_bus.AcaProgram_Insert(self.__aca_program):
            print("True")
            self.ShowSuccessMessageBox(self.___aca_program_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            print(self.___aca_program_bus.GetExceptType())
            self.ShowFailedMessageBox(self.___aca_program_bus.GetExceptType())
            self.ResetControls()

    def AcaProgramUpdate(self):
        global status
        code = self.txtProgramCode.text()
        name = self.txtProgramName.text()
        tuition = self.dsbProgramTuition.value()
        if self.rdAcaStatusOpen.isChecked() and not self.rdAcaStatusClose.isChecked():
            status = 'open'
        elif not self.rdAcaStatusOpen.isChecked() and self.rdAcaStatusClose.isChecked():
            status = 'closed'

        self.__aca_program.SetProgramCode(code)
        self.__aca_program.SetProgramName(name)
        self.__aca_program.SetTuition(tuition)
        self.__aca_program.SetProStatus(status)
        # print(self.__aca_program.GetProgramCode())
        # print(self.__aca_program.GetProgramName())
        # print(self.__aca_program.GetTuition())
        # print(self.__aca_program.GetProStatus())
        if self.___aca_program_bus.AcaProgram_Update(self.__aca_program):
            print("True")
            self.ShowSuccessMessageBox(self.___aca_program_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            print(self.___aca_program_bus.GetExceptType())
            self.ShowFailedMessageBox(self.___aca_program_bus.GetExceptType())
            self.ResetControls()

    def AcaProgramDelete(self):
        global status
        code = self.txtProgramCode.text()
        name = self.txtProgramName.text()
        tuition = self.dsbProgramTuition.value()
        if self.rdAcaStatusOpen.isChecked() and not self.rdAcaStatusClose.isChecked():
            status = 'open'
        elif not self.rdAcaStatusOpen.isChecked() and self.rdAcaStatusClose.isChecked():
            status = 'closed'

        self.__aca_program.SetProgramCode(code)
        self.__aca_program.SetProgramName(name)
        self.__aca_program.SetTuition(tuition)
        self.__aca_program.SetProStatus(status)
        # print(self.__aca_program.GetProgramCode())
        # print(self.__aca_program.GetProgramName())
        # print(self.__aca_program.GetTuition())
        # print(self.__aca_program.GetProStatus())
        if self.___aca_program_bus.AcaProgram_Delete(self.__aca_program):
            print("True")
            self.ShowSuccessMessageBox(self.___aca_program_bus.GetExceptType())
            self.LoadDataSource()
            self.ResetControls()
        else:
            print("False")
            print(self.___aca_program_bus.GetExceptType())
            self.ShowFailedMessageBox(self.___aca_program_bus.GetExceptType())
            self.ResetControls()

    def processRbDialogAcaProgram(self):
        if self.rdbtnAddAcaProgram.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnAddAcaProgram.text()
            print(pushBtnText)
            self.pushBtnAcaProgram.setText(pushBtnText)
            self.txtProgramCode.setEnabled(True)
            self.txtProgramName.setEnabled(True)
            self.dsbProgramTuition.setEnabled(True)
            self.rdAcaStatusOpen.setEnabled(True)
            self.rdAcaStatusClose.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_ACADEMICPROGRAM = ADD
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnUpdateAcaProgram.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnUpdateAcaProgram.text()
            print(pushBtnText)
            self.pushBtnAcaProgram.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword to readOnly
            self.txtProgramCode.setEnabled(True)
            self.txtProgramName.setEnabled(True)
            self.dsbProgramTuition.setEnabled(True)
            self.rdAcaStatusOpen.setEnabled(True)
            self.rdAcaStatusClose.setEnabled(True)
            # self.txtAdminName.setReadOnly(False)
            # self.txtAdminPassword.setReadOnly(True)
            # self.ckbActiveAdmin.setCheckable(True)
            # Add Image to the button
            self.ACTION_TYPE_ACADEMICPROGRAM = UPDATE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnDeleteAcaProgram.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnDeleteAcaProgram.text()
            print(pushBtnText)
            self.pushBtnAcaProgram.setText(pushBtnText)
            # Set all info widgets disable
            self.txtProgramCode.setEnabled(True)
            self.txtProgramName.setEnabled(False)
            self.dsbProgramTuition.setEnabled(False)
            self.rdAcaStatusOpen.setEnabled(False)
            self.rdAcaStatusClose.setEnabled(False)
            # Add Image to the button
            self.ACTION_TYPE_ACADEMICPROGRAM = DELETE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)

    def ResetControls(self):
        # reset controls
        self.txtProgramCode.setText("")
        self.txtProgramName.setText("")
        self.dsbProgramTuition.setValue(0.00)
        self.rdAcaStatusOpen.setChecked(True)
        self.rdAcaStatusClose.setChecked(False)

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

    def DialogProgramLoad(self):
        self.processRbDialogAcaProgram()
        self.LoadDataSource()

    def LoadDataSource(self):
        data = self.___aca_program_bus.SelectAllAcaProgram()
        dataSource = pd.DataFrame(data, columns=self.___aca_program_bus.GetColumnHeaders())
        self.model = PandasModelSourse(dataSource)
        self.tvAcaProgram.setModel(self.model)


# if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     course = DialogAcaProgram()
# #     course.exec_()
# #     sys.exit(app.exec_())