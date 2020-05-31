from model.db_connect import DBConnect
import mysql.connector
# from DTO.Admin import Admin
from Views.Global import GlobalConst


class Classroom_DAL:
    def __init__(self):
        self.__db_connect = DBConnect()
        self.__EXCEPT_TYPE = ''

    def GetExceptType(self):
        return self.__EXCEPT_TYPE

    def GetConnectionStatus(self):
        return self.__db_connect.GetConnectionStatus()

    def SelectAllClassroom(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectAllClassroom = "select * from classroom"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectAllClassroom)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Classroom table is: ", myCursor.rowcount)

            print("\nPrinting each Classroom record")
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
            print("Error reading data from Classroom table")

    def ListDataSourceClassroom(self):
        dataSource = []
        classrooms = self.SelectAllClassroom()
        for element in classrooms:
            lsClass = list(element)
            dataSource.append(lsClass)
        return dataSource

    def Classroom_Insert(self, classroom_model):
        if classroom_model.IsClassroomEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            mycursor = connection.cursor()
            code = classroom_model.GetClassroomCode()
            number = classroom_model.GetClassroomNumber()
            buil_name = classroom_model.GetBuildingName()
            location = classroom_model.GetLocationName()
            sql_insert = "INSERT INTO classroom (classroomCode, roomNumber, buildingName, locationName) VALUES (%s, " \
                         "%s, %s, %s); "
            values = (code, number, buil_name, location)

            mycursor.execute(sql_insert, values)
            connection.commit()
            print("Data inserted successfully into Classroom table using parameters")
            self.__EXCEPT_TYPE = 'Data inserted successfully into Classroom table'
            connection.close()
            return True
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Classroom_Update(self, classroom_model):
        if classroom_model.IsClassroomEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        # active = str(admin.GetAdminActive())
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_updateClassroom = "UPDATE classroom SET roomNumber = %s, buildingName = %s, locationName = %s WHERE " \
                              "classroomCode = %s; "
            values = (classroom_model.GetClassroomNumber(), classroom_model.GetBuildingName(),
                      classroom_model.GetLocationName(), classroom_model.GetClassroomCode())
            myCursor.execute(sql_updateClassroom, values)  # ExecuteNoneQuery in .NET
            connection.commit()
            print(myCursor.rowcount, "Record Updated successfully into Classroom table")
            self.__EXCEPT_TYPE = 'Record Updated successfully into Classroom table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to UPDATE record into Admin table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Classroom_Delete(self, classroom_model):
        if classroom_model.GetClassroomCode() == "":
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_deleteClassroom = "DELETE FROM classroom WHERE classroomCode = %s"
            parameter = classroom_model.GetClassroomCode()
            myCursor.execute(sql_deleteClassroom, (parameter,))
            connection.commit()
            print("Record Deleted successfully ")
            self.__EXCEPT_TYPE = 'Record Deleted successfully from Classroom table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to DELETE record from Classroom table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def GetColumnHeaders(self):
        col_headers = ['CLASSROOM CODE', 'CLASSROOM NUMBER', 'BUILDING NAME', 'LOCATION NAME']
        return col_headers

    def GetClassroomCode(self):
        classroom_code = []
        for classroom in self.SelectAllClassroom():
            code = classroom[0]
            classroom_code.append(code)
        return classroom_code
# def main():
#     classroom = Classroom_DAL()
#     print(classroom.ListDataSourceClassroom())
#
#
# main()

