from model.db_connect import DBConnect
import mysql.connector
# from DTO.Admin import Admin
from Views.Global import GlobalConst


class ProDegree_DAL:
    def __init__(self):
        self.__db_connect = DBConnect()
        self.__EXCEPT_TYPE = ''

    def GetExceptType(self):
        return self.__EXCEPT_TYPE

    def GetConnectionStatus(self):
        return self.__db_connect.GetConnectionStatus()

    def SelectAllDegree(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectAllDegree = "select * from degree"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectAllDegree)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Degree table is: ", myCursor.rowcount)

            print("\nPrinting each Degree record")
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
            print("Error reading data from Degree table")

    def GetAllDegreeName(self, lsDegree):
        lsDegreeName = []
        for degree in lsDegree:
            name = degree[1]
            lsDegreeName.append(name)
        return lsDegreeName

    def GetDegreeCode(self, degreeName):
        # print(degreeName)
        lsDegree = self.SelectAllDegree()
        # print(lsDegree)
        for degree in lsDegree:
            if degree[1] == degreeName:
                return degree[0]  # return degreeCode
            else:
                continue

    def Degree_Insert(self, degree_model):
        if degree_model.IsDegreeEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            mycursor = connection.cursor()
            code = degree_model.GetDegreeCode()
            name = degree_model.GetDegreeName()
            salary_index = degree_model.GetSalaryIndex()
            sql_insert = "INSERT INTO degree (degreeCode, degreeName, salaryIndex) VALUES (%s, %s, %s);"
            values = (code, name, salary_index)

            mycursor.execute(sql_insert, values)
            connection.commit()
            print("Data inserted successfully into Professor Degree table using parameters")
            self.__EXCEPT_TYPE = 'Data inserted successfully into Professor Degree table'
            connection.close()
            return True
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Degree_Update(self, degree_model):
        if degree_model.IsDegreeEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        # active = str(admin.GetAdminActive())
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_updateDegree = "UPDATE degree SET degreeName = %s, salaryIndex = %s WHERE degreeCode = %s;"
            values = (degree_model.GetDegreeName(), degree_model.GetSalaryIndex(), degree_model.GetDegreeCode())
            myCursor.execute(sql_updateDegree, values)  # ExecuteNoneQuery in .NET
            connection.commit()
            print(myCursor.rowcount, "Record Updated successfully into Professor Degree table")
            self.__EXCEPT_TYPE = 'Record Updated successfully into Professor Degree table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to UPDATE record into Professor Degree table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def Degree_Delete(self, degree_model):
        if degree_model.GetDegreeCode() == "":
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_deleteDegree = "DELETE FROM degree WHERE degreeCode = %s;"
            parameter = degree_model.GetDegreeCode()
            myCursor.execute(sql_deleteDegree, (parameter,))
            connection.commit()
            print("Record Deleted successfully ")
            self.__EXCEPT_TYPE = 'Record Deleted successfully from Professor Degree table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to DELETE record from Professor Degree table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def GetColumnHeaders(self):
        col_headers = ['DEGREE CODE', 'DEGREE NAME', 'SALARY INDEX']
        return col_headers

    def GetDegreeNameByCode(self, code):
        # print(degreeName)
        lsDegree = self.SelectAllDegree()
        # print(lsDegree)
        for degree in lsDegree:
            if degree[0] == code:
                return degree[1]  # return degreeCode
            else:
                continue

# def main():
#     degree = ProDegree_DAL()
#     print("All degree name: ", degree.GetAllDegreeName(degree.SelectAllDegree()))
#
#
# main()

