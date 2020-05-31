from model.db_connect import DBConnect
import mysql.connector
from DTO.Student import Student
from Views.Global import GlobalConst
from datetime import date


class Student_DAL:
    def __init__(self):
        self.__db_connect = DBConnect()
        self.__EXCEPT_TYPE = ''

    def GetExceptType(self):
        return self.__EXCEPT_TYPE

    def GetConnectionStatus(self):
        return self.__db_connect.GetConnectionStatus()

    def SelectAllStudent(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectAllStudent = "select * from student"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectAllStudent)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Student table is: ", myCursor.rowcount)

            print("\nPrinting each Student record")
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
            print("Error reading data from Professor table")

    def GetDataSource(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectDataSource = "select studentId, stFullName, stGender, stDateOfBirth, stCountry, " \
                                   "stCurrentAddress, stEmail, stIsActive, stRegisteredDate, programCode  from student"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectDataSource)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Student table is: ", myCursor.rowcount)

            print("\nPrinting each Student record")
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
            print("Error reading data from Professor table")

    def Student_Insert(self, student_model):
        student = Student()
        student = student_model
        if student.IsStudentEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            mycursor = connection.cursor()
            id = student.StId
            full_name = student.StFullname
            gender = student.StGender
            dateOfBirth = student.StDateOfBirth
            country = student.StCountry
            address = student.StCurrentAddress
            email = student.StEmail
            registeredDate = student.StRegisteredDate
            programCode = student.StProgramCode
            sql_insert = "INSERT INTO student(studentId, stFullName, stGender, stDateOfBirth, stCountry, stCurrentAddress, stEmail, stRegisteredDate, programCode) " \
                         "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"
            values = (id, full_name, gender, dateOfBirth, country, address, email, registeredDate, programCode)

            mycursor.execute(sql_insert, values)
            connection.commit()
            print("Data inserted successfully into Student table using parameters")
            self.__EXCEPT_TYPE = 'Data inserted successfully into Student table'
            connection.close()
            return True
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Student_Update(self, student_model):
        student = Student()
        student = student_model
        if student.IsStudentEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        # active = str(admin.GetAdminActive())
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_updateStudent = "UPDATE student SET stFullName = %s, stGender = %s, stDateOfBirth = %s, stCountry = %s, stCurrentAddress=%s, stEmail=%s, stIsActive=%s, stRegisteredDate=%s, programCode=%s WHERE studentId = %s;"
            values = (
                student.StFullname, student.StGender,
                student.StDateOfBirth, student.StCountry,
                student.StCurrentAddress,
                student.StEmail, student.StActive,
                student.StRegisteredDate, student.StProgramCode, student.StId)
            myCursor.execute(sql_updateStudent, values)  # ExecuteNoneQuery in .NET
            connection.commit()
            print(myCursor.rowcount, "Record Updated successfully into Student table")
            self.__EXCEPT_TYPE = 'Record Updated successfully into Student table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to UPDATE record into Student table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Student_Delete(self, student_model):
        student = Student()
        student = student_model
        if student.StId == "":
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_deleteStudent = "DELETE FROM student WHERE studentId = %s;"
            parameter = student.StId
            myCursor.execute(sql_deleteStudent, (parameter,))
            connection.commit()
            print("Record Deleted successfully ")
            self.__EXCEPT_TYPE = 'Record Deleted successfully from Student table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to DELETE record from Student table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def GetColumnHeaders(self):
        col_headers = ['ID', 'FULL NAME', 'GENDER', 'DATE OF BIRTH', 'COUNTRY', 'CURRENT ADDRESS', 'EMAIL', 'ACTIVE',
                       'REGISTERDATE', 'PROGRAM CODE']
        return col_headers

    def GetActive(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectAllStudent = "select stIsActive from student"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectAllStudent)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Student table is: ", myCursor.rowcount)

            print("\nPrinting each Student record")
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
            print("Error reading data from Professor table")

    def getRead_Only_StudentSchedule(self, studentId):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_getSchedule = "SELECT proSchedule.courseCode, pro.proFullName, proSchedule.teachDate, proSchedule.timeStart, proSchedule.periodHour, proSchedule.semester, " \
                              "stSchedule.term, classroom.roomNumber, classroom.buildingName, classroom.locationName " \
                              "FROM professorcourse as proSchedule " \
                              "LEFT JOIN studentcourse as stSchedule ON proSchedule.courseCode = stSchedule.courseCode LEFT JOIN professor as pro ON proSchedule.professorId = pro.professorId " \
                              "LEFT JOIN classroom ON proSchedule.classroomCode = classroom.classroomCode WHERE stSchedule.studentId = %s"
            myCursor = conn.cursor(buffered=True)
            value = studentId
            myCursor.execute(sql_getSchedule, (value,))  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Schedule Student table is: ", myCursor.rowcount)

            print("\nPrinting each Schedule Student record")
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
            print("Error reading data from Schedule Student table")
            return False

    def getStudentInfoByIdAndPassword(self, id, password):
        for student in self.SelectAllStudent():
            if student[0] == id and student[8] == password:
                # tranform user into Student model
                st = Student()
                st.StId = student[0]
                st.StFullname = student[1]
                st.StGender = student[2]
                st.StDateOfBirth = student[3]
                st.StCountry = student[4]
                st.StCurrentAddress = student[5]
                st.StEmail = student[6]
                st.StActive = student[7]
                st.StPassword = student[8]
                st.StRegisteredDate = student[9]
                st.StProgramCode = student[10]

                # pro = self.tranformUser(professor)
                return st
            else:
                continue
        return False

    def validateStudent(self, student_model):
        if (student_model.StId == '' and student_model.StPassword == '')\
                or (student_model.StId == '' and student_model.StPassword is not '') \
                or (student_model.StId is not '' and student_model.StPassword == ''):
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        lsStudent = self.SelectAllStudent()
        for student in lsStudent:  # check student ID and Password
            if student[0] == student_model.StId and student[8] == student_model.StPassword:
                return True
            else:
                continue
        return False

    def getColumnHeadersForScheduleTb(self):
        col_headers = ['COURSE CODE', 'INSTRUCTOR', 'DATE', 'TIME', 'DURATION', 'SEMESTER', 'TERM', 'ROOM NUMBER', 'BUILDING NAME', 'LOCATION']
        return col_headers

    def updatePasswordById(self, password, studentId):
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_updatePassword = "UPDATE student SET stPassword = %s WHERE studentId = %s"
            values = (password, studentId)
            myCursor.execute(sql_updatePassword, values)  # ExecuteNoneQuery in .NET
            connection.commit()
            print(myCursor.rowcount, "Record Updated successfully into Student table")
            self.__EXCEPT_TYPE = 'Record Updated successfully into Student table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to UPDATE record into Student table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

# def main():
#     student = Student_DAL()
#     # ls_st = student.SelectAllStudent()
#     # for st in ls_st:
#     #     print(type(st[3]))
#     #     print(st[3])
#     #     print(type(st[9]))
#     #     print(st[9])
#     #     print()
#     if student.getStudentInfoByIdAndPassword('st1', '123') is not False:
#         ls_record = student.getStudentInfoByIdAndPassword('st1', '123')
#         print(ls_record)
#     else:
#         print("Failed to get data")
#
#
# main()
