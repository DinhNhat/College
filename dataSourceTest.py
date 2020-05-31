import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from Views.Global import GlobalConst
from dialogCourse import DialogCourse
from BUS.ProDegree_BUS import ProDegree_BUS

dataSource_ui = "dataSourceTest.ui"
Ui_DataSource, QtBaseClass = uic.loadUiType(dataSource_ui)


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
        return len(self.__data[0])


class DegreeModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, degreeName=None, **kwargs):
        super(DegreeModel, self).__init__(*args, **kwargs)
        self.degreeName = degreeName or []

    def data(self, index, role=None):
        if role == Qt.DisplayRole:
            text = self.degreeName[index.row()]
            return text

    def rowCount(self, index):
        return len(self.degreeName)


class DataSource(QtWidgets.QMainWindow, Ui_DataSource):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.__degree_bus = ProDegree_BUS()
        self.load()
        Ui_DataSource.__init__(self)
        data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]
        self.model = TableModel(data)
        self.tbView.setModel(self.model)
        self.__type = self.tbView.isWidgetType()
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.comboBox.addItems(self.__degree_bus.GetAllDegreeName())

    def selectionchange(self, index):
        print("Current index", index, "selection changed ", self.comboBox.currentText())


    def load(self):
        print(self.__degree_bus.GetAllDegreeName())

    def GetTbViewType(self):
        return self.__type


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dataSource = DataSource()
    dataSource.show()
    print(dataSource.GetTbViewType())
    sys.exit(app.exec_())