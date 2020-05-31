from model.db_connect import DBConnect
import mysql.connector
# from DTO.Admin import Admin
from Views.Global import GlobalConst


class Course_DAL:
    def __init__(self):
        self.__db_connect = DBConnect()
        self.__EXCEPT_TYPE = ''

    def GetExceptType(self):
        return self.__EXCEPT_TYPE

    def GetConnectionStatus(self):
        return self.__db_connect.GetConnectionStatus()

    def SelectAllCourse(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectAllCourse = "select * from course"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectAllCourse)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Course table is: ", myCursor.rowcount)

            print("\nPrinting each Course record")
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
            print("Error reading data from Course table")

    def ListDataSourceCourse(self):
        dataSource = []
        courses = self.SelectAllCourse()
        for course in courses:
            lsCourse = list(course)
            dataSource.append(lsCourse)
        return dataSource

    def GetDataSource(self):
        return self.SelectAllCourse()

    def Course_Insert(self, course_model):
        if course_model.IsCourseEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            mycursor = connection.cursor()
            code = course_model.Code
            desc = course_model.Description
            credit = course_model.Credit
            outline = course_model.Outline
            programCode = course_model.ProgramCode
            sql_insert = "INSERT INTO course (courseCode, courseDescription, CourseCredit, courseOutline, programCode) " \
                         "VALUES (%s, %s, %s, %s, %s) "
            values = (code, desc, credit, outline, programCode)

            mycursor.execute(sql_insert, values)
            connection.commit()
            print("Data inserted successfully into Course table using parameters")
            self.__EXCEPT_TYPE = 'Data inserted successfully into Course table'
            connection.close()
            return True
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Course_Update(self, course_model):
        if course_model.IsCourseEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            mycursor = connection.cursor()
            code = course_model.Code
            desc = course_model.Description
            credit = course_model.Credit
            outline = course_model.Outline
            programCode = course_model.ProgramCode
            sql_update = "UPDATE course SET courseDescription = %s, courseCredit = %s, courseOutline = %s, " \
                         "programCode = %s WHERE courseCode = %s "
            values = (desc, credit, outline, programCode, code)

            mycursor.execute(sql_update, values)
            connection.commit()
            print("Record UPDATED successfully into Course table using parameters")
            self.__EXCEPT_TYPE = 'Record UPDATED successfully into Course table'
            connection.close()
            return True
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Course_Delete(self, course_model):
        if course_model.Code == "":
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_delete = "DELETE FROM course WHERE courseCode = %s "
            parameter = course_model.Code
            myCursor.execute(sql_delete, (parameter,))
            connection.commit()
            print("Record Deleted successfully ")
            self.__EXCEPT_TYPE = 'Record Deleted successfully from Course table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to DELETE record from Course table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def GetColumnHeaders(self):
        col_headers = ['COURSE CODE', 'COURSE DESCRIPTION', 'COURSE CREDIT',  'COURSE OUTLINE', 'PROGRAM CODE']
        return col_headers

    def GetCourseCode(self):
        course_code = []
        for course in self.SelectAllCourse():
            code = course[0]
            course_code.append(code)
        return course_code


# def main():
#     course = Course_DAL()
#     print(course.GetCourseCode())
#
#
# main()
