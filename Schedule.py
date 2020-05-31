import sys

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMessageBox

from Views.Global import GlobalConst
from BUS.Course_BUS import Course_BUS
from BUS.Classroom_BUS import Classroom_BUS
from BUS.Schedule_BUS import Schedule_BUS
from DTO.Schedule import Schedule
from model.pandas_model_source import PandasModelSourse

schedule_ui = "dialogSchedule.ui"
Ui_DialogSchedule, QtBaseClass = uic.loadUiType(schedule_ui)

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


class DialogSchedule(QtWidgets.QDialog, Ui_DialogSchedule):
    COURSE_CODE, SEMESTER, PROFESSOR, STUDENTS = range(4)

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_DialogSchedule.__init__(self)
        self.setupUi(self)
        self.__schedule_bus = Schedule_BUS()
        self.__course_bus = Course_BUS()
        self.__classroom_bus = Classroom_BUS()
        self.__cbCourseCode = ''
        self.__cbClassroomCode = ''
        self.__schedulePatternDelete = Schedule()
        self.__courseAvailabilityInfo = self.__schedule_bus.getCourseAvailabilityInfo()
        self.__selectedRowDeleteEmit = False
        self.__selectedCourseAvailADDEmit = False
        self.__scheduleAddEmit_Only = Schedule()
        # self.cbScheduleCourseCode.addItems(self.__course_bus.GetCourseCode())
        # self.cbScheduleCourseCode.setCurrentIndex(-1)
        self.cbScheduleClassroomCode.addItems(self.__classroom_bus.GetClassroomCode())
        self.cbScheduleClassroomCode.setCurrentIndex(-1)
        self.ACTION_TYPE_SCHEDULE = ADD
        self.setEvents()
        self.DialogScheduleLoad()
        self.initializeTreView()

    def setEvents(self):
        # Tree view events
        self.treeViewCourseAvailable.clicked.connect(self.onClickedTreeViewItems)
        # Event handling
        self.rbAddSchedule.toggled.connect(self.processRbDialogSchedule)
        self.rbUpdateSchedule.toggled.connect(self.processRbDialogSchedule)
        self.rbDeleteSchedule.toggled.connect(self.processRbDialogSchedule)
        self.pushButtonSchedule.clicked.connect(self.processData)
        # self.cbScheduleCourseCode.currentIndexChanged.connect(self.selectionchangeCbScheduleCourseCode)
        self.cbScheduleClassroomCode.currentIndexChanged.connect(self.selectionchangeCbScheduleClassroomCode)
        self.tvSchedule.clicked.connect(self.onClickedTvSchedule)

    def processData(self):
        if self.ACTION_TYPE_SCHEDULE == ADD:
            self.ScheduleInsert()
        elif self.ACTION_TYPE_SCHEDULE == UPDATE:
            self.ScheduleUpdate()
        elif self.ACTION_TYPE_SCHEDULE == DELETE:
            self.ScheduleDelete()

    def ScheduleInsert(self):
        if self.__selectedCourseAvailADDEmit is False:
            message = "Please choose a row in list view of course available to ADD schedule"
            showFailedMessageBox(message)
        else:
            try:
                course_code = self.__scheduleAddEmit_Only.CourseCode
                # professor_id = self.txtScheduleProfessorId.text()
                professor_id = self.__scheduleAddEmit_Only.ProfessorId
                teach_date = self.dateScheduleTeachDate.date().toString("yyyy-MM-dd")
                time_start = self.timeEditScheduleTimeStart.time().toString("hh:mm:ss")
                period_hour = self.dsbSchedulePeriod.value()
                # semester = self.txtScheduleSemester.text()
                semester = self.__scheduleAddEmit_Only.Semester
                start_date_semester = self.dateEditScheduleStartDate.date().toString("yyyy-MM-dd")
                end_date_semester = self.dateEditScheduleEndDate.date().toString("yyyy-MM-dd")
                classroom_code = self.__cbClassroomCode
                schedule = Schedule(course_code, professor_id, teach_date, semester, start_date_semester,
                                    end_date_semester,
                                    classroom_code, time_start, period_hour)

                if self.__schedule_bus.Schedule_Insert(schedule):
                    print("True")
                    showSuccessMessageBox(self.__schedule_bus.GetExceptType())
                    self.LoadDataSource()
                    self.ResetControls()
                else:
                    print("False")
                    showFailedMessageBox(self.__schedule_bus.GetExceptType())
                    self.ResetControls()
            except Exception as exc:
                showFailedMessageBox(exc)
                self.ResetControls()
        # print(course_code)
        # print(professor_id)
        # print(teach_date)
        # print(type(time_start))
        # print(time_start)
        # print(period_hour)
        # print(semester)
        # print(start_date_semester)
        # print(end_date_semester)
        # print(classroom_code)

    def ScheduleUpdate(self):
        pass

    def ScheduleDelete(self):
        if self.__selectedRowDeleteEmit:
            if self.__schedule_bus.Schedule_Delete(self.__schedulePatternDelete):
                showSuccessMessageBox(self.__schedule_bus.GetExceptType())
                self.LoadDataSource()
                self.ResetControls()
            else:
                print("False")
                showFailedMessageBox(self.__schedule_bus.GetExceptType())
                self.ResetControls()
        else:
            message = 'Please choose a row in table to delete'
            showFailedMessageBox(message)
            self.ResetControls()

    def DialogScheduleLoad(self):
        self.processRbDialogSchedule()
        self.LoadDataSource()

    def LoadDataSource(self):
        data = self.__schedule_bus.GetDataSource()
        dataSource = pd.DataFrame(data, columns=self.__schedule_bus.GetColumnHeaders())
        model = PandasModelSourse(dataSource)
        self.tvSchedule.setModel(model)

    def selectionchangeCbScheduleClassroomCode(self, index):
        self.__cbClassroomCode = self.cbScheduleClassroomCode.currentText()
        print("Current index", index, "selection changed ", self.cbScheduleClassroomCode.currentText())

    def processRbDialogSchedule(self):
        if self.rbAddSchedule.isChecked():
            pushBtnText = self.rbAddSchedule.text()
            print(pushBtnText)
            self.pushButtonSchedule.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword readOnly FALSE
            self.dateScheduleTeachDate.setEnabled(True)
            self.timeEditScheduleTimeStart.setEnabled(True)
            self.dsbSchedulePeriod.setEnabled(True)
            self.dateEditScheduleStartDate.setEnabled(True)
            self.dateEditScheduleEndDate.setEnabled(True)
            self.cbScheduleClassroomCode.setEnabled(True)

            # Add Image to the button
            self.ACTION_TYPE_SCHEDULE = ADD
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rbUpdateSchedule.isChecked():
            pushBtnText = self.rbUpdateSchedule.text()
            print(pushBtnText)
            self.pushButtonSchedule.setText(pushBtnText)
            # Set txtAdminId and txtAdminPassword to readOnly
            self.dateScheduleTeachDate.setEnabled(True)
            self.timeEditScheduleTimeStart.setEnabled(True)
            self.dsbSchedulePeriod.setEnabled(True)
            self.dateEditScheduleStartDate.setEnabled(True)
            self.dateEditScheduleEndDate.setEnabled(True)
            self.cbScheduleClassroomCode.setEnabled(True)
            # Add Image to the button
            self.ACTION_TYPE_SCHEDULE = UPDATE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)
        elif self.rbDeleteSchedule.isChecked():
            pushBtnText = self.rbDeleteSchedule.text()
            print(pushBtnText)
            self.pushButtonSchedule.setText(pushBtnText)
            # Set all info widgets disable
            self.dateScheduleTeachDate.setEnabled(False)
            self.timeEditScheduleTimeStart.setEnabled(False)
            self.dsbSchedulePeriod.setEnabled(False)
            self.dateEditScheduleStartDate.setEnabled(False)
            self.dateEditScheduleEndDate.setEnabled(False)
            self.cbScheduleClassroomCode.setEnabled(False)
            # Add Image to the button
            self.ACTION_TYPE_SCHEDULE = DELETE
            # self.setDynamicImageToBtn(self.pushBtnAdmin, self.ACTION_TYPE_ADMIN_TAB)

    def ResetControls(self):
        self.dsbSchedulePeriod.setValue(0)
        self.cbScheduleClassroomCode.setCurrentIndex(-1)
        self.__selectedRowDeleteEmit = False
        self.__selectedCourseAvailADDEmit = False
        # reset selectedrow on table view

    def initializeTreView(self):
        self.treeViewCourseAvailable.setRootIsDecorated(False)
        self.treeViewCourseAvailable.setAlternatingRowColors(True)
        header = self.treeViewCourseAvailable.header()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        # header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        model = self.createCourseAvailableModel(self)
        self.treeViewCourseAvailable.setModel(model)
        rowNumInsertModel = 0
        for source in self.__courseAvailabilityInfo:
            self.addCourseAvailable(model, source[0], source[1], source[2], source[3], rowNumInsertModel)
            rowNumInsertModel += 1

    def onClickedTreeViewItems(self, index):
        print("You click on row: ", index.row())
        self.__selectedCourseAvailADDEmit = True
        itemSelected = self.__courseAvailabilityInfo[index.row()]
        print(self.__courseAvailabilityInfo)
        self.__scheduleAddEmit_Only.CourseCode = itemSelected[0]
        self.__scheduleAddEmit_Only.ProfessorId = itemSelected[2]
        self.__scheduleAddEmit_Only.Semester = itemSelected[1]

    def createCourseAvailableModel(self, parent):
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.COURSE_CODE, Qt.Horizontal, "Course code")
        model.setHeaderData(self.SEMESTER, Qt.Horizontal, "Semester")
        model.setHeaderData(self.PROFESSOR, Qt.Horizontal, "Professor id")
        model.setHeaderData(self.STUDENTS, Qt.Horizontal, "Number of students")
        return model

    def addCourseAvailable(self, model, courseCode, semester, professorId, numberOfStudent, rowNumInsertModel):
        model.insertRow(rowNumInsertModel)
        model.setData(model.index(rowNumInsertModel, self.COURSE_CODE), courseCode)
        model.setData(model.index(rowNumInsertModel, self.SEMESTER), semester)
        model.setData(model.index(rowNumInsertModel, self.PROFESSOR), professorId)
        model.setData(model.index(rowNumInsertModel, self.STUDENTS), numberOfStudent)

    def onClickedTvSchedule(self, index):
        if index.isValid():
            # print('You just click schedule with index: ', index)
            self.getInfoFromTvSchedule(index)

    def getInfoFromTvSchedule(self, indexSelected):
        self.__selectedRowDeleteEmit = True
        tv_source = self.__schedule_bus.GetDataSource()
        selectedItem = tv_source[indexSelected.row()]
        print(selectedItem)
        # Get the exact info to DELETE
        # print("Course code: ", selectedItem[0])
        # print("professor id: ", selectedItem[1])
        # print("Teach date: ", selectedItem[2])
        # print("Time start: ", selectedItem[3])
        # print("Semester: ", selectedItem[5])
        self.__schedulePatternDelete.CourseCode = selectedItem[0]
        self.__schedulePatternDelete.ProfessorId = selectedItem[1]
        self.__schedulePatternDelete.TeachDate = selectedItem[2]
        self.__schedulePatternDelete.TimeStart = selectedItem[3]
        self.__schedulePatternDelete.Semester = selectedItem[5]


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     schedule = DialogSchedule()
#     schedule.exec_()
#     sys.exit(app.exec_())
