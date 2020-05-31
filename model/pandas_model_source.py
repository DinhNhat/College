import pandas as pd
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from Views.Global import GlobalConst

myGlobal = GlobalConst()


class PandasModelSourse(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(PandasModelSourse, self).__init__()
        self.__data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self.__data.iloc[index.row(), index.column()]
            if isinstance(value, float):
                return "%.2f" % value

            if isinstance(value, str):
                return "%s" % value

            return str(value)

        if role == Qt.BackgroundRole:
            # See below for the data structure.
            color = myGlobal.GetColorsByIndex(11)
            return QtGui.QColor(color)

    def rowCount(self, index):
        return self.__data.shape[0]

    def columnCount(self, index):
        return self.__data.shape[1]

    def headerData(self, section, orientation, role=None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.__data.columns[section])

            if orientation == Qt.Vertical:
                return str(self.__data.index[section])