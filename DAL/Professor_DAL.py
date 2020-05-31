from model.db_connect import DBConnect
import mysql.connector
from DTO.Professor import Professor
from Views.Global import GlobalConst


class Professor_DAL:
    def __init__(self):
        self.__db_connect = DBConnect()
        self.__EXCEPT_TYPE = ''

    def GetExceptType(self):
        return self.__EXCEPT_TYPE

    def GetConnectionStatus(self):
        return self.__db_connect.GetConnectionStatus()

    def SelectAllProfessor(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectAllProfessor = "select * from professor"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectAllProfessor)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Professor table is: ", myCursor.rowcount)

            print("\nPrinting each Professor record")
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

    def Professor_Insert(self, professor_model):
        if professor_model.IsProfessorEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            mycursor = connection.cursor()
            id = professor_model.GetProfessorId()
            full_name = professor_model.GetProfessorFullName()
            gender = professor_model.GetProfessorGender()
            email = professor_model.GetProfessorEmail()
            address = professor_model.GetProfessorAddress()
            phone = professor_model.GetProfessorPhone()
            active = professor_model.GetProfessorIsActive()
            degreeCode = professor_model.GetProfessorDegreeCode()
            sql_insert = "INSERT INTO professor (professorId, proFullName, proGender, proEmail, proAddress, proPhone, proIsActive, degreeCode) " \
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            values = (id, full_name, gender, email, address, phone, active, degreeCode)

            mycursor.execute(sql_insert, values)
            connection.commit()
            print("Data inserted successfully into Professor table using parameters")
            self.__EXCEPT_TYPE = 'Data inserted successfully into Professor table'
            connection.close()
            return True
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Professor_Update(self, professor_model):
        if professor_model.IsProfessorEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        # active = str(admin.GetAdminActive())
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_updateProfessor = "UPDATE professor SET " \
                                  "proFullName = %s, proGender = %s, proEmail = %s, proAddress = %s, proPhone = %s, " \
                                  "proIsActive = %s, degreeCode = %s " \
                                  "WHERE professorId = %s;"
            values = (
                professor_model.GetProfessorFullName(), professor_model.GetProfessorGender(),
                professor_model.GetProfessorEmail(), professor_model.GetProfessorAddress(),
                professor_model.GetProfessorPhone(),
                professor_model.GetProfessorIsActive(), professor_model.GetProfessorDegreeCode(),
                professor_model.GetProfessorId())
            myCursor.execute(sql_updateProfessor, values)  # ExecuteNoneQuery in .NET
            connection.commit()
            print(myCursor.rowcount, "Record Updated successfully into Professor table")
            self.__EXCEPT_TYPE = 'Record Updated successfully into Professor table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to UPDATE record into Professor table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Professor_Delete(self, professor_model):
        if professor_model.GetProfessorId() == "":
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_deleteProfessor = "DELETE FROM professor WHERE professorId = %s;"
            parameter = professor_model.GetProfessorId()
            myCursor.execute(sql_deleteProfessor, (parameter,))
            connection.commit()
            print("Record Deleted successfully ")
            self.__EXCEPT_TYPE = 'Record Deleted successfully from Professor table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to DELETE record from Professor table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def GetDataSource(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_getDataSource = "SELECT professorId, proFullName, proGender, proEmail, proAddress, proPhone, " \
                                "proIsActive, degreeCode FROM professor "
            myCursor = conn.cursor()
            myCursor.execute(sql_getDataSource)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Professor table is: ", myCursor.rowcount)

            print("\nPrinting each Professor record")
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

    def GetColumnHeaders(self):
        col_headers = ['ID', 'FULL NAME', 'GENDER', 'EMAIL', 'ADDRESS',
                       'PHONE NUMBER', 'ACTIVE', 'DEGREE CODE']
        return col_headers

    def ValidateProfessor(self, professor_model):
        if professor_model.ProfessorId == '' and professor_model.Password == '123':
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        lsProfessor = self.SelectAllProfessor()
        for professor in lsProfessor:  # check admin ID and Password
            if professor[0] == professor_model.ProfessorId and professor[7] == professor_model.Password:
                return True
            else:
                continue
        return False

    def GetProfessorInfoByIdAndPasswd(self, id, password):
        for professor in self.SelectAllProfessor():
            if professor[0] == id and professor[7] == password:
                # tranform user into Professor model
                pro = Professor()
                pro.ProfessorId = professor[0]
                pro.FullName = professor[1]
                pro.Gender = professor[2]
                pro.Email = professor[3]
                pro.Address = professor[4]
                pro.Phone = professor[5]
                pro.Active = professor[6]
                pro.Password = professor[7]
                pro.DegreeCode = professor[8]
                # pro = self.tranformUser(professor)
                return pro
            else:
                continue
        return False

    def GetStudentGrade(self, porfessorId):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_getDataSource = "SELECT DISTINCT enrol.courseCode, student.studentId, student.stFullName, enrol.semester, enrol.term, enrol.GPA, proSchedule.startDateSemester, proSchedule.endDateSemester " \
                                "FROM studentcourse as enrol LEFT JOIN professorcourse as proSchedule ON enrol.professorId = proSchedule.professorId " \
                                "LEFT JOIN student ON enrol.studentId = student.studentId WHERE proSchedule.professorId = %s;"
            myCursor = conn.cursor(buffered=True)
            value = porfessorId
            myCursor.execute(sql_getDataSource, (value,))  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Student Grade table is: ", myCursor.rowcount)

            print("\nPrinting each Student Grade record")
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
            print("Error reading data from Student Grade table")

    def GetColumnHeadersForStudentGradeTb(self):
        col_headers = ['COURSE CODE', 'STUDENT ID',  'STUDENT FULL NAME', 'SEMESTER', 'TERM', 'GPA',
                       'START DATE SEMESTER', 'END DATE SEMESTER']
        return col_headers

    def GetInfoByRowStGradeTable(self, professorId, row_index):
        if row_index > -1:
            ls_st = self.GetStudentGrade(professorId)
            student = ls_st[row_index]
            return student
        else:
            return False

    def updatePasswordById(self,password, id):
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_updatePassword = "UPDATE professor SET proPassword = %s WHERE professorId = %s;"
            values = (password, id)
            myCursor.execute(sql_updatePassword, values)  # ExecuteNoneQuery in .NET
            connection.commit()
            print(myCursor.rowcount, "Record Updated successfully into Professor table")
            self.__EXCEPT_TYPE = 'Record Updated successfully into Professor table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to UPDATE record into Professor table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def getRead_Only_Schedule(self, proId):  # Get read-only schedule table for a given professor id
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_getSchedule = "SELECT courseCode, teachDate, timeStart, periodHour, semester, startDateSemester, endDateSemester, " \
                              "classroom.roomNumber, classroom.buildingName, classroom.locationName  " \
                                "FROM professorcourse as schedulePro  " \
                                "LEFT JOIN classroom ON schedulePro.classroomCode = classroom.classroomCode " \
                                "WHERE professorId = %s"
            myCursor = conn.cursor(buffered=True)
            value = proId
            myCursor.execute(sql_getSchedule, (value,))  # ExecuteReader in .NET
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
            return False

    def getColumnHeadersScheduleTb(self):
        col_headers = ['COURSE CODE', 'TEACH DATE', 'TIME START', 'PERIOD HOUR', 'SEMESTER',
                       'START DATE SEMESTER', 'END DATE SEMESTER', 'ROOM NUMBER', 'BUILDING NAME', 'LOCATION NAME']
        return col_headers


# def main():
#     professor = Professor()
#     professor.ProfessorId = 'p2'
#     professor.Password = '123'
#     pro = Professor_DAL()
#     if pro.GetStudentGrade(professor.ProfessorId) is not False:
#         print("Length of the array result: ", len(pro.GetStudentGrade(professor.ProfessorId)))
#         print(pro.GetStudentGrade(professor.ProfessorId))
#     else:
#         print("Failed to print Schedule records")
#
#
# main()
