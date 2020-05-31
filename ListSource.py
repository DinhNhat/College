import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QMessageBox

from BUS.Schedule_BUS import Schedule_BUS

sourceTest_ui = "ListSourceTest.ui"
Ui_ListSource, QtBaseClass = uic.loadUiType(sourceTest_ui)


class WindowListSource(QtWidgets.QMainWindow, Ui_ListSource):
    COURSE_CODE, SEMESTER, PROFESSOR, STUDENTS = range(4)

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_ListSource.__init__(self)
        self.setupUi(self)
        self.__schedule_bus = Schedule_BUS()
        self.__courseAvailabilityInfo = self.__schedule_bus.getCourseAvailabilityInfo()
        # print(self.__courseAvailabilityInfo)
        self.initializeUI()
        self.setEvents()

    def initializeUI(self):
        self.treeView.setRootIsDecorated(False)
        self.treeView.setAlternatingRowColors(True)
        header = self.treeView.header()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        # header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        model = self.createCourseAvailableModel(self)
        self.treeView.setModel(model)
        for source in self.__courseAvailabilityInfo:
            self.addCourseAvailable(model, source[0], source[1], source[2], source[3])

    def setEvents(self):
        self.treeView.clicked.connect(self.onTableClicked)

    def onTableClicked(self, index):
        itemSelected = self.__courseAvailabilityInfo[index.row()]
        print(itemSelected)

    def createCourseAvailableModel(self, parent):
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.COURSE_CODE, Qt.Horizontal, "Course code")
        model.setHeaderData(self.SEMESTER, Qt.Horizontal, "Semester")
        model.setHeaderData(self.PROFESSOR, Qt.Horizontal, "Professor id")
        model.setHeaderData(self.STUDENTS, Qt.Horizontal, "Number of students")
        return model

    def addCourseAvailable(self, model, courseCode, semester, professorId, numberOfStudent):
        model.insertRow(0)
        model.setData(model.index(0, self.COURSE_CODE), courseCode)
        model.setData(model.index(0, self.SEMESTER), semester)
        model.setData(model.index(0, self.PROFESSOR), professorId)
        model.setData(model.index(0, self.STUDENTS), numberOfStudent)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    source = WindowListSource()
    source.show()
    sys.exit(app.exec_())
