import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
# from Views.Global import GlobalConst
# import time

admin_ui = "dialogAdmin.ui"
Ui_AdminDialog, QtBaseClass = uic.loadUiType(admin_ui)

from Views.Global import GlobalConst
# from model.db_connection import DBConnection
from BUS.Admin_BUS import Admin_BUS
from DTO.Admin import Admin

myGloabal = GlobalConst()

ADD = myGloabal.getImage('Add')
UPDATE = myGloabal.getImage('Update')
DELETE = myGloabal.getImage('Delete')


# declare a table model
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self.__data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.__data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self.__data)

    def columnCount(self, index):
        return len(self.data[0])


class AdminDialog(QtWidgets.QDialog, Ui_AdminDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_AdminDialog.__init__(self)
        self.ACTION_TYPE_ADMIN_TAB = ''
        self.__admin_bus = Admin_BUS()
        self.__admin = Admin()
        self.setupUi(self)
        self.txtAdminPassword.setEnabled(False)
        self.rdbtnAddAdmin.setChecked(True)
        # self.ErrorLabel.setText('')
        self.setEvents()
        # process table view
        # data = [
        #     [4, 9, 2],
        #     [1, 0, 0],
        #     [3, 5, 0],
        #     [3, 3, 2],
        #     [7, 8, 9],
        # ]
        # self.model = TableModel(data)
        # self.tvDialogAdmin.setModel(self.model)

    def setEvents(self):
        # Event handling
        self.rdbtnAddAdmin.toggled.connect(self.processRdbtnAdminTab)
        self.rdbtnUpdateAdmin.toggled.connect(self.processRdbtnAdminTab)
        self.rdbtnDeleteAdmin.toggled.connect(self.processRdbtnAdminTab)
        # self.rdbtnAddProfessor.toggled.connect(self.processRdbtnProTab)
        # self.rdbtnUpdateProfessor.toggled.connect(self.processRdbtnProTab)
        # self.rdbtnDeleteProfessor.toggled.connect(self.processRdbtnProTab)
        # self.rdbtnAddStudent.toggled.connect(self.processRdbtnStudentTab)
        # self.rdbtnUpdateStudent.toggled.connect(self.processRdbtnStudentTab)
        # self.rdbtnDeleteStudent.toggled.connect(self.processRdbtnStudentTab)
        # self.rdbtnAddCourse.toggled.connect(self.processRdbtnCourseTab)
        # self.rdbtnUpdateCourse.toggled.connect(self.processRdbtnCourseTab)
        # self.rdbtnDeleteCourse.toggled.connect(self.processRdbtnCourseTab)
        self.pushBtnAdmin.clicked.connect(self.ProcessData)

    def closeEvent(self, event):
        print('You just closed Admin dialog!')

    def ProcessData(self):
        # Check if the button is ready to take action
        # (other widgets info are emtpy or rdbtn not checked)
        if self.ACTION_TYPE_ADMIN_TAB == ADD:
            self.AdminInsert()
        elif self.ACTION_TYPE_ADMIN_TAB == UPDATE:
            self.AdminUpdate()
        elif self.ACTION_TYPE_ADMIN_TAB == DELETE:
            self.AdminDelete()

    def AdminInsert(self):
        adminId = self.txtAdminId.text()
        adminName = self.txtAdminName.text()
        if self.rbAdminActiveYes.isChecked() and not self.rbAdminActiveNo.isChecked():
            active = 1
        elif self.rbAdminActiveYes.isChecked() == False and self.rbAdminActiveNo.isChecked() == True:
            active = 0
        self.__admin.SetAdminId(adminId)
        self.__admin.SetAdminLoginName(adminName)
        self.__admin.SetAdminActive(active)
        print(self.__admin.GetAdminId())
        print(self.__admin.GetAdminLoginName())
        print(self.__admin.GetAdminActive())
        if self.__admin_bus.Admin_Insert(self.__admin):
            print("True")
            self.ShowSuccessMessageBox(self.__admin_bus.GetExceptType())
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__admin_bus.GetExceptType())
            self.ResetControls()

    def AdminUpdate(self):
        adminId = self.txtAdminId.text()
        adminName = self.txtAdminName.text()
        if self.rbAdminActiveYes.isChecked() and not self.rbAdminActiveNo.isChecked():
            active = 1
        elif self.rbAdminActiveYes.isChecked() == False and self.rbAdminActiveNo.isChecked() == True:
            active = 0
        self.__admin.SetAdminId(adminId)
        self.__admin.SetAdminLoginName(adminName)
        self.__admin.SetAdminActive(active)
        if self.__admin_bus.Admin_Update(self.__admin):
            print("True")
            self.ShowSuccessMessageBox(self.__admin_bus.GetExceptType())
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__admin_bus.GetExceptType())
            self.ResetControls()

    def AdminDelete(self):
        adminId = self.txtAdminId.text()
        self.__admin.SetAdminId(adminId)
        if self.__admin_bus.Admin_Delete(self.__admin):
            print("True")
            self.ShowSuccessMessageBox(self.__admin_bus.GetExceptType())
            self.ResetControls()
        else:
            print("False")
            self.ShowFailedMessageBox(self.__admin_bus.GetExceptType())
            self.ResetControls()

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

    def ResetControls(self):
        # reset controls
        self.txtAdminId.setText("")
        self.txtAdminName.setText("")

    def processRdbtnAdminTab(self):
        if self.rdbtnAddAdmin.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnAddAdmin.text()
            print(pushBtnText)
            self.pushBtnAdmin.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword readOnly FALSE
            self.txtAdminId.setEnabled(True)
            self.txtAdminName.setEnabled(True)
            self.rbAdminActiveYes.setEnabled(True)
            self.rbAdminActiveNo.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_ADMIN_TAB = ADD
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnUpdateAdmin.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnUpdateAdmin.text()
            print(pushBtnText)
            self.pushBtnAdmin.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword to readOnly
            self.txtAdminId.setDisabled(False)
            self.txtAdminName.setEnabled(True)
            self.rbAdminActiveYes.setEnabled(True)
            self.rbAdminActiveNo.setEnabled(True)
            # self.txtAdminName.setReadOnly(False)
            # self.txtAdminPassword.setReadOnly(True)
            # self.ckbActiveAdmin.setCheckable(True)
            # Add Image to the button
            self.ACTION_TYPE_ADMIN_TAB = UPDATE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rdbtnDeleteAdmin.isChecked():
            # self.ResetControls()
            pushBtnText = self.rdbtnDeleteAdmin.text()
            print(pushBtnText)
            self.pushBtnAdmin.setText(pushBtnText)
            # Set all info widgets disable
            self.txtAdminId.setDisabled(False)
            self.txtAdminName.setDisabled(True)
            self.rbAdminActiveYes.setDisabled(True)
            self.rbAdminActiveNo.setDisabled(True)
            # Add Image to the button
            self.ACTION_TYPE_ADMIN_TAB = DELETE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
    #
    # def processRdbtnStudentTab(self):
    #     if self.rdbtnAddStudent.isChecked():
    #         pushBtnText = self.rdbtnAddStudent.text()
    #         print(pushBtnText)
    #         self.pushBtnStudent.setText(pushBtnText)
    #         # Add Image to the button
    #         actionType = ADD
    #         self.setDynamicImageToBtn(self.pushBtnStudent, actionType)
    #     elif self.rdbtnUpdateStudent.isChecked():
    #         pushBtnText = self.rdbtnUpdateStudent.text()
    #         print(pushBtnText)
    #         self.pushBtnStudent.setText(pushBtnText)
    #         # Add Image to the button
    #         actionType = UPDATE
    #         self.setDynamicImageToBtn(self.pushBtnStudent, actionType)
    #     elif self.rdbtnDeleteStudent.isChecked():
    #         pushBtnText = self.rdbtnDeleteStudent.text()
    #         print(pushBtnText)
    #         self.pushBtnStudent.setText(pushBtnText)
    #         # Add Image to the button
    #         actionType = DELETE
    #         self.setDynamicImageToBtn(self.pushBtnStudent, actionType)
    #
    # def processRdbtnCourseTab(self):
    #     if self.rdbtnAddCourse.isChecked():
    #         pushBtnText = self.rdbtnAddCourse.text()
    #         print(pushBtnText)
    #         self.pushBtnCourse.setText(pushBtnText)
    #         # Add Image to the button
    #         actionType = ADD
    #         self.setDynamicImageToBtn(self.pushBtnCourse, actionType)
    #     elif self.rdbtnUpdateCourse.isChecked():
    #         pushBtnText = self.rdbtnUpdateCourse.text()
    #         print(pushBtnText)
    #         self.pushBtnCourse.setText(pushBtnText)
    #         # Add Image to the button
    #         actionType = UPDATE
    #         self.setDynamicImageToBtn(self.pushBtnCourse, actionType)
    #     elif self.rdbtnDeleteCourse.isChecked():
    #         pushBtnText = self.rdbtnDeleteCourse.text()
    #         print(pushBtnText)
    #         self.pushBtnCourse.setText(pushBtnText)
    #         # Add Image to the button
    #         actionType = DELETE
    #         self.setDynamicImageToBtn(self.pushBtnCourse, actionType)
    #
    # def setDynamicImageToBtn(self, pushBtnType, action):
    #     # pushBtnType = QtWidgets.QPushButton
    #     # "../College_GUI_project/images/"
    #     path_file_image = './images' + action + '.png'
    #     icon = QtGui.QIcon()
    #     icon.addPixmap(QtGui.QPixmap(path_file_image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #     pushBtnType.setIcon(icon)
    #     pushBtnType.setIconSize(QtCore.QSize(50, 50))
    #
    # def disableWidgetPasswd(self):
    #     self.txtAdminPassword.setEnabled(False)
    #     font = QtGui.QFont()
    #     font.setStrikeOut(True)
    #     self.labelAdminPassword_2.setFont(font)
    #     self.ckbActiveAdmin.setCheckable(True)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     dialogAdmin = QtWidgets.QDialog()
#     ui = AdminDialog()
#     ui.setupUi(dialogAdmin)
#     dialogAdmin.exec_()
#     sys.exit(app.exec_())