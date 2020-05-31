from model.db_connect import DBConnect
import mysql.connector
from DTO.StEnrolment import Enrolment
from Views.Global import GlobalConst


class Enrolment_DAL:
    def __init__(self):
        self.__db_connect = DBConnect()
        self.__EXCEPT_TYPE = ''

    def GetExceptType(self):
        return self.__EXCEPT_TYPE

    def GetConnectionStatus(self):
        return self.__db_connect.GetConnectionStatus()

    def SelectAllEnrolment(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectAllEnrolment = "select * from studentcourse"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectAllEnrolment)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Enrolment student course table is: ", myCursor.rowcount)

            print("\nPrinting each Enrolment student course record")
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
            print("Error reading data from Enrolment student course table")

    def GetDataSource(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectDataSource = "select courseCode, studentId, professorId, semester, term, " \
                                   "enrolDate from studentcourse"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectDataSource)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Enrolment student course table is: ", myCursor.rowcount)

            print("\nPrinting each Enrolment student course record")
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
            print("Error reading data from Enrolment student course table")

    def Enrolement_Insert(self, enrolment_model):
        enrol = Enrolment()
        enrol = enrolment_model
        if enrol.IsStEnrolmentEmpty():
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
            sql_insert = "INSERT INTO studentcourse (courseCode, studentId, professorId, semester, term, enrolDate) " \
                         "VALUES (%s, %s, %s, %s, %s, %s); "
            values = (
            enrol.CourseCode, enrol.StudentId, enrol.ProfessorId, enrol.Semester, enrol.Term, enrol.EnrolmentDate)

            mycursor.execute(sql_insert, values)
            connection.commit()
            print("Data inserted successfully into Enrolment table using parameters")
            self.__EXCEPT_TYPE = 'Data inserted successfully into Enrolment table'
            connection.close()
            return True
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Enrolement_Update(self, enrolment_model):
        pass
        # DELETE FROM studentcourse WHERE (courseCode = 'CSD-2354') AND (studentId = 'st2') AND (professorId = 'p3');
        # enrol = Enrolment()
        # enrol = enrolment_model
        # if student.IsStudentEmpty():
        #     self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
        #     return False
        # # active = str(admin.GetAdminActive())
        # try:
        #     connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
        #     myCursor = connection.cursor()
        #     sql_updateStudent = "UPDATE student SET stFullName = %s, stGender = %s, stDateOfBirth = %s, stCountry = %s, stCurrentAddress=%s, stEmail=%s, stIsActive=%s, stRegisteredDate=%s, programCode=%s WHERE studentId = %s;"
        #     values = (
        #         student.StFullname, student.StGender,
        #         student.StDateOfBirth, student.StCountry,
        #         student.StCurrentAddress,
        #         student.StEmail, student.StActive,
        #         student.StRegisteredDate, student.StProgramCode, student.StId)
        #     myCursor.execute(sql_updateStudent, values)  # ExecuteNoneQuery in .NET
        #     connection.commit()
        #     print(myCursor.rowcount, "Record Updated successfully into Student table")
        #     self.__EXCEPT_TYPE = 'Record Updated successfully into Student table'
        #     myCursor.close()
        #     connection.close()
        #     print('MySQL connection is closed.')
        #     return True
        # except mysql.connector.Error as error:
        #     print("SQL command ERROR. Failed to UPDATE record into Student table {}".format(error))
        #     self.__EXCEPT_TYPE = error.msg
        #     return False

    def Enrolement_DeleteByKeyCode(self, enrolment_model):
        # enrol = Enrolment()
        courseCode = enrolment_model.CourseCode
        studentId = enrolment_model.StudentId
        professorId = enrolment_model.ProfessorId
        if enrolment_model.IsStEnrolmentEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        else:
            try:
                connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
                myCursor = connection.cursor()
                sql_deleteEnrol = "DELETE FROM studentcourse WHERE (courseCode = %s) AND (studentId = %s) " \
                                  "AND (professorId = %s) "
                values = (courseCode, studentId, professorId)
                myCursor.execute(sql_deleteEnrol, values)
                connection.commit()
                print("Record Deleted successfully ")
                self.__EXCEPT_TYPE = 'Record Deleted successfully from Student Enrolment table'
                myCursor.close()
                connection.close()
                print('MySQL connection is closed.')
                return True
            except mysql.connector.Error as error:
                print("SQL command ERROR. Failed to DELETE record from Student Enrolment table {}".format(error))
                self.__EXCEPT_TYPE = error.msg
                return False

    def GetColumnHeaders(self):
        col_headers = ['COURSE CODE', 'STUDENT ID', 'PROFESSOR ID', 'SEMESTER', 'TERM', 'ENROLMENT DATE']
        return col_headers

    def updateStudentGPAByConditions(self, GPA, courseCode, studentId, professorId, semester, term):
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_updateGrade = "UPDATE studentcourse SET GPA = %s WHERE (courseCode = %s) AND (studentId = %s) AND (professorId = %s) " \
                              "AND (semester = %s) AND (term = %s)"
            values = (GPA, courseCode, studentId, professorId, semester, term)
            myCursor.execute(sql_updateGrade, values)  # ExecuteNoneQuery in .NET
            connection.commit()
            print(myCursor.rowcount, "Record Updated successfully into Student Grade table")
            self.__EXCEPT_TYPE = 'Record Updated successfully into Student Grade table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to UPDATE record into Student Grade table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

# def main():
#     enrol = Enrolment_DAL()
#     gpa = 3.23
#     course = 'CSD 2206'
#     stId = 'st2'
#     proId = 'p1'
#     semester = '2019Fall'
#     term = 1
#     if enrol.changeStudentGradeByConditions(gpa, course, stId, proId, semester, term):
#         print("Update successfully")
#     else:
#         print("Failed to update")
#
#
# main()
