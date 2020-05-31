from model.db_connect import DBConnect
import mysql.connector

from DTO.Schedule import Schedule
from DTO.Course import Course
from DTO.Classroom import Classroom
from Views.Global import GlobalConst


class Schedule_DAL:

    def __init__(self):
        self.__db_connect = DBConnect()
        self.__EXCEPT_TYPE = ''

    def GetExceptType(self):
        return self.__EXCEPT_TYPE

    def GetConnectionStatus(self):
        return self.__db_connect.GetConnectionStatus()

    def SelectAllSchedule(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectAllSchedule = "select * from professorcourse"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectAllSchedule)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Schedule table is: ", myCursor.rowcount)

            print("\nPrinting each Schedule record")
            lsRecords = list(records)
            # for row in lsRecords:  # cursor is a tuples
            #     print("Admin id: ", row[0])
            #     print("Admin login name: ", row[1])
            #     print("Admin password: ", row[2])
            #     print("Admin active: ", row[3])
            myCursor.close()
            conn.close()
            return lsRecords
        else:
            print("Error reading data from Schedule table")

    def GetDataSource(self):
        return self.SelectAllSchedule()

    def Schedule_Insert(self, schedule_model):
        schedule = Schedule()
        schedule = schedule_model
        if schedule.IsScheduleEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            mycursor = connection.cursor()
            # id = student.StId
            # full_name = student.StFullname
            # gender = student.StGender
            # dateOfBirth = student.StDateOfBirth
            # country = student.StCountry
            # address = student.StCurrentAddress
            # email = student.StEmail
            # registeredDate = student.StRegisteredDate
            # programCode = student.StProgramCode
            sql_insert = "INSERT INTO professorcourse (courseCode, professorId, teachDate, timeStart, periodHour, " \
                         "semester, startDateSemester, endDateSemester, classroomCode) VALUES (%s, %s, " \
                         "%s, %s, %s, %s, %s, %s, %s) "
            values = (
                schedule.CourseCode, schedule.ProfessorId, schedule.TeachDate, schedule.TimeStart, schedule.PeriodHour,
                schedule.Semester, schedule.StartDateSemester, schedule.EndDateSemester, schedule.ClassroomCode)

            mycursor.execute(sql_insert, values)
            connection.commit()
            print("Data inserted successfully into Schedule table using parameters")
            self.__EXCEPT_TYPE = 'Data inserted successfully into Schedule table'
            connection.close()
            return True
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Schedule_Delete(self, schedule_model):
        if schedule_model.isKeyCodeEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_deleteSchedule = "DELETE FROM professorcourse WHERE (courseCode = %s) AND (professorId = %s) " \
                                 "AND (teachDate = %s) AND (timeStart = %s) AND (semester = %s)"
            courseCode = schedule_model.CourseCode
            proId = schedule_model.ProfessorId
            teachDate = schedule_model.TeachDate
            timeStart = schedule_model.TimeStart
            semester = schedule_model.Semester
            values = (courseCode, proId, teachDate, timeStart, semester)
            myCursor.execute(sql_deleteSchedule, values)
            connection.commit()
            print("Record Deleted successfully ")
            self.__EXCEPT_TYPE = 'Record Deleted successfully from Schedule table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to DELETE record from Schedule table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def GetColumnHeaders(self):
        col_headers = ['COURSE CODE', 'PROFESSOR ID', 'TEACH DATE', 'TIME START', 'PERIOD HOUR', 'SEMESTER',
                       'START DATE SEMESTER', 'END DATE SEMESTER', 'CLASSROOM CODE']
        return col_headers

    def getCourseAvailabilityInfo(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_CourseAvailability = "SELECT courseCode, " \
                                     "semester, professorId, COUNT(studentId) as 'Number of students per course' FROM " \
                                     "studentcourse GROUP BY courseCode "
            myCursor = conn.cursor()
            myCursor.execute(sql_CourseAvailability)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Course availability table is: ", myCursor.rowcount)

            print("\nPrinting each Course availability record")
            lsRecords = list(records)
            # for row in lsRecords:  # cursor is a tuples
            #     print("Admin id: ", row[0])
            #     print("Admin login name: ", row[1])
            #     print("Admin password: ", row[2])
            #     print("Admin active: ", row[3])
            myCursor.close()
            conn.close()
            return lsRecords
        else:
            print("Error reading data from Course availability table")
            return False

    def getCoursesAvailable(self):
        ls_courses = []
        if self.getCourseAvailabilityInfo() is not False:
            records = self.getCourseAvailabilityInfo()
            for source in records:
                ls_courses.append(source[0])
            return ls_courses
        else:
            return False

    def getAssignedProfessorAvailable(self):
        ls_professors = []
        if self.getCourseAvailabilityInfo() is not False:
            records = self.getCourseAvailabilityInfo()
            for source in records:
                ls_professors.append(source[2])
            return ls_professors
        else:
            return False


# def main():
#     sche = Schedule()
#     sche.CourseCode = 'CSD 2206'
#     sche.ProfessorId = 'p1'
#     sche.TeachDate = '2019-10-04'
#     sche.TimeStart = '13:40:00'
#     sche.Semester = '2019Fall'
#     schedule = Schedule_DAL()
#     if schedule.Schedule_Delete(sche) is not False:
#         print("Delete current row successfully")
#     else:
#         print("Failed to delete source")
#
#
# main()
