import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QMessageBox
import pandas as pd

from Views.Global import GlobalConst
from BUS.Admin_BUS import Admin_BUS
from DTO.Admin import Admin

admin_update_pass_ui = "dialogAdminUpdatePassword.ui"
Ui_DialogAd_Update_Pass, QtBaseClass = uic.loadUiType(admin_update_pass_ui)

myGloabal = GlobalConst()

ADD = myGloabal.getImage('Add')
UPDATE = myGloabal.getImage('Update')
DELETE = myGloabal.getImage('Delete')


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


class DialogAdminUpdatePass(QtWidgets.QDialog, Ui_DialogAd_Update_Pass):

    def __init__(self, currentAdmin):
        QtWidgets.QDialog.__init__(self)
        Ui_DialogAd_Update_Pass.__init__(self)
        self.setupUi(self)
        self.__admin_bus = Admin_BUS()
        self.__currentAdmin = currentAdmin
        # Set events
        self.setEventsAndWidgets()

    def setEventsAndWidgets(self):
        self.labelErrorOldPass.setVisible(False)
        self.labelError.setVisible(False)
        # Event handling
        self.lineEditOldPass.installEventFilter(self)
        self.lineEditNewPassRepeat.installEventFilter(self)
        self.btnUpdatePasswd.clicked.connect(self.updatePassword)

        # Related actions in tab update password
        # def eventFilter(self, source, event):  # Check condition of creating new password
        #     if source is self.lineEditOldPass:
        #         if event.type() == QEvent.KeyRelease:
        #             if self.lineEditOldPass.text() == self.__currentUser.StPassword:
        #                 self.labelErrorOldPass.setAutoFillBackground(True)
        #                 self.labelErrorOldPass.setVisible(True)
        #                 self.labelErrorOldPass.setText("Old password correct")
        #                 self.labelErrorOldPass.setStyleSheet("QLabel { background-color: rgb(0,255,0); }")
        #             else:
        #                 self.labelErrorOldPass.setAutoFillBackground(True)
        #                 self.labelErrorOldPass.setVisible(True)
        #                 self.labelErrorOldPass.setText("Old password Incorrect")
        #                 self.labelErrorOldPass.setStyleSheet("QLabel { background-color: rgb(255,0,0); }")
        #                 print('Old password incorrect')
        #     elif source is self.lineEditNewPassRepeat:
        #         if event.type() == QEvent.KeyRelease:
        #             if self.lineEditNewPassRepeat.text() == self.lineEditNewPass.text():
        #                 self.labelError.setAutoFillBackground(True)
        #                 self.labelError.setVisible(True)
        #                 self.labelError.setText("Password repeat correctly")
        #                 self.labelError.setStyleSheet("QLabel { background-color: rgb(0,255,0); }")
        #             else:
        #                 self.labelError.setAutoFillBackground(True)
        #                 self.labelError.setVisible(True)
        #                 self.labelError.setText("Password repeat Incorrectly")
        #                 self.labelError.setStyleSheet("QLabel { background-color: rgb(255,0,0); }")
        #     return super(DialogAdminUpdatePass, self).eventFilter(source, event)

    def eventFilter(self, source, event):
        if source is self.lineEditOldPass:
            if event.type() == QEvent.KeyRelease:
                if self.lineEditOldPass.text() == self.__currentAdmin.GetAdminPasswd():
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
        return super(DialogAdminUpdatePass, self).eventFilter(source, event)

    # def keyReleaseEvent(self, event):
    #     if event.type() == QEvent.KeyRelease:
    #         if event.key() == Qt.Key_Up:
    #             print("Key up")
    #             event.accept()
    #
    #         elif event.key() == Qt.Key_Down:
    #             print("key down")
    #             event.accept()

    def updatePassword(self):
        if self.checkIsPasswordMatch():
            # update password by is
            print('You are able to update password by professor id')
            if self.__admin_bus.updatePasswordById(self.lineEditNewPassRepeat.text(),
                                                   self.__currentAdmin.GetAdminId()):
                # showSuccess message box
                message = "Update password successfully"
                showSuccessMessageBox(message)
                adminId = self.__currentAdmin.GetAdminId()
                adPassword = self.lineEditNewPassRepeat.text()
                self.__currentAdmin = self.__admin_bus.getAdminInfoByIdAndPassword(adminId, adPassword)
                self.resetWidgets()
            else:
                # show unsuccess message box
                message = "Failed to update password"
                showFailedMessageBox(message)
                self.resetWidgets()
        else:
            print('You are NOT able to update password by professor id')
            # show unsuccess message box
            message = "Failed to update password"
            showFailedMessageBox(message)
            self.resetWidgets()

    def checkIsPasswordMatch(self):
        if self.lineEditOldPass.text() != "" and self.lineEditNewPass.text() != "" \
                and self.lineEditNewPassRepeat.text() != "":
            if self.labelErrorOldPass.text() == "Old password correct" and self.labelError.text() == "Password repeat " \
                                                                                                     "correctly":
                return True
        return False

    def resetWidgets(self):
        # reset controls
        self.lineEditOldPass.setText("")
        self.lineEditNewPass.setText("")
        self.lineEditNewPassRepeat.setText("")
        self.labelErrorOldPass.setVisible(False)
        self.labelError.setVisible(False)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     admin_bus = Admin_BUS()
#     admin = Admin()
#     admin.SetAdminId('ad1')
#     admin.SetAdminPasswd('kingkong')
#     admin = admin_bus.getAdminInfoByIdAndPassword(admin.GetAdminId(), admin.GetAdminPasswd())
#     adDialog = DialogAdminUpdatePass(admin)
#     adDialog.exec_()
#     sys.exit(app.exec_())
