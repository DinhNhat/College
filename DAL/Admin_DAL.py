from model.db_connect import DBConnect
import mysql.connector
from DTO.Admin import Admin
from Views.Global import GlobalConst


class Admin_DAL:
    def __init__(self):
        self.__db_connect = DBConnect()
        self.__EXCEPT_TYPE = ''

    def GetExceptType(self):
        return self.__EXCEPT_TYPE

    def GetConnectionStatus(self):
        return self.__db_connect.GetConnectionStatus()

    def SelectAllAdmin(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectAllAdmin = "select * from admintb"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectAllAdmin)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Admin table is: ", myCursor.rowcount)

            print("\nPrinting each Admin record")
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
            print("Error reading data from admin table")

    def ValidateAdmin(self, admin_model):
        if admin_model.GetAdminId() == '' and admin_model.GetAdminPasswd() == '':
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        lsAdmin = self.SelectAllAdmin()
        for ad in lsAdmin:  # check admin ID and Password
            if admin_model.GetAdminId() == ad[0] and admin_model.GetAdminPasswd() == ad[2]:
                return True
            else:
                continue
        return False

    def Admin_Insert(self, admin_model):
        if admin_model.IsAnEmptyAdmin():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            mycursor = connection.cursor()
            id = admin_model.GetAdminId()
            name = admin_model.GetAdminLoginName()
            active = admin_model.GetAdminActive()
            sql_insert = "INSERT INTO admintb (adminId, adminNameLogin, adminIsActive) VALUES (%s, %s, %s);"
            values = (id, name, active)

            mycursor.execute(sql_insert, values)
            connection.commit()
            print("Data inserted successfully into Admin table using parameters")
            self.__EXCEPT_TYPE = 'Data inserted successfully into Admin table'
            connection.close()
            return True
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.__EXCEPT_TYPE = error
            return False

    def Admin_Update(self, admin_model):
        if admin_model.IsAnEmptyAdmin():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        # active = str(admin.GetAdminActive())
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_updateAdmin = " UPDATE admintb SET adminNameLogin = %s, adminIsActive = %s WHERE adminId = %s; "
            values = (admin_model.GetAdminLoginName(), admin_model.GetAdminActive(), admin_model.GetAdminId())
            myCursor.execute(sql_updateAdmin, values)  # ExecuteNoneQuery in .NET
            connection.commit()
            print(myCursor.rowcount, "Record Updated successfully into Admin table")
            self.__EXCEPT_TYPE = 'Record Updated successfully into Admin table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as errorcode:
            print("SQL command ERROR. Failed to UPDATE record into Admin table {}".format(errorcode))
            self.__EXCEPT_TYPE = errorcode
            return False

    def Admin_Delete(self, admin_model):
        if admin_model.GetAdminId() == "":
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_deleteAdmin = "DELETE FROM admintb WHERE adminId = %s"
            parameter = admin_model.GetAdminId()
            myCursor.execute(sql_deleteAdmin, (parameter,))
            connection.commit()
            print("Record Deleted successfully ")
            self.__EXCEPT_TYPE = 'Record Deleted successfully from Admin table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as errorcode:
            print("SQL command ERROR. Failed to DELETE record from Admin table {}".format(errorcode))
            self.__EXCEPT_TYPE = errorcode
            return False

    def updatePasswordById(self, password, adminId):
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_updatePassword = "UPDATE admintb SET adminPassword = %s WHERE adminId = %s"
            values = (password, adminId)
            myCursor.execute(sql_updatePassword, values)  # ExecuteNoneQuery in .NET
            connection.commit()
            print(myCursor.rowcount, "Record Updated successfully into Admin table")
            self.__EXCEPT_TYPE = 'Record Updated successfully into Admin table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to UPDATE record into Admin table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def getAdminInfoByIdAndPassword(self, id, password):
        for admin in self.SelectAllAdmin():
            if admin[0] == id and admin[2] == password:
                # tranform user into Student model
                ad = Admin()
                ad.SetAdminId(admin[0])
                ad.SetAdminLoginName(admin[1])
                ad.SetAdminPasswd(admin[2])
                ad.SetAdminActive(admin[3])
                # pro = self.tranformUser(professor)
                return ad
            else:
                continue
        return False


# def main():
#     admin = Admin_DAL()
#     if admin.Admin_Insert():
#         print()
#     else:
#         print("Error occurs")
#
#
# main()

