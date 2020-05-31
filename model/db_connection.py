import mysql.connector
# from mysql.connector import Error
from mysql.connector import errorcode

HOST_NAME = 'localhost'
USER_NAME = 'root'
PASSWORD = 'dinhnhat1994'
DATABASE = 'college_pygui'


# global cursor
# global connection
class DBConnection:
    def __init__(self):
        # self.__hostName = HOST_NAME
        # self.__userName = USER_NAME
        # self.__passwd = PASSWORD
        # self.__database = DATABASE
        # self.__connection_config_dict = {
        #     'host': HOST_NAME,
        #     'user': USER_NAME,
        #     'passwd': PASSWORD,
        #     'database': DATABASE
        # }
        self.__ConnStr = mysql.connector.connect(host=HOST_NAME, user=USER_NAME, passwd=PASSWORD)

    # def GetConnConfigurationDict(self):
    #     return self.__connection_config_dict

    # def GetHostName(self):
    #     return self.__hostName
    #
    # def GetUserName(self):
    #     return self.__userName
    #
    # def GetPassword(self):
    #     return self.__passwd
    #
    # def GetDatabase(self):
    #     return self.__database

    def TestConnStr(self):
        check = False
        try:
            # connection = mysql.connector.connect(host=HOST_NAME, user=USER_NAME, passwd=PASSWORD)
            connection = self.__ConnStr
            print("You're connected to database: ")
            check = True
        except mysql.connector.Error as err:
            print("Error while connecting to MySQL", err)
            check = False
        connection.close()
        print("MySQL connection is closed.")
        return check

    # def TestConnStr(self):
    #     check = False
    #     try:
    #         connection = mysql.connector.connect(host=HOST_NAME, user=USER_NAME, passwd=PASSWORD, db=DATABASE)
    #         if connection.is_connected():
    #             db_Info = connection.get_server_info()
    #             print("Connected to MySQL Server version ", db_Info)
    #             cursor = connection.cursor()
    #             cursor.execute("select database();")
    #             record = cursor.fetchone()
    #             print("You're connected to database: ", record)
    #             check = True
    #     except errorcode as err:
    #         print("Error while connecting to MySQL", err)
    #         check = False
    #     finally:
    #         cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed.")
    #     return check

    # def TestConnStr(self):
    #     """ Connect to MySQL database """
    #     try:
    #         if self.DetailErrConnectionDB():
    #             return True
    #     except Exception as err:
    #         print(err)
    #     return False
    #
    # def DetailErrConnectionDB(self):
    #     # global cursor, connection
    #     check = False
    #     try:
    #         connection = mysql.connector.connect(host=HOST_NAME, user=USER_NAME, passwd=PASSWORD, db=DATABASE)
    #         if connection.is_connected():
    #             db_Info = connection.get_server_info()
    #             print("Connected to MySQL Server version ", db_Info)
    #             cursor = connection.cursor()
    #             cursor.execute("select database();")
    #             record = cursor.fetchone()
    #             print("You're connected to database: ", record)
    #             check = True
    #     except errorcode as err:
    #         print("Error while connecting to MySQL", err)
    #         check = False
    #     finally:
    #         cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed.")
    #     return check

    # def GetAllDatabase(self):
    #     if self.TestConnStr():
    #         conn = mysql.connector.connect(host=HOST_NAME, user=USER_NAME, passwd=PASSWORD, db=DATABASE)
    #         myCursor = conn.cursor()
    #         test_query = 'SHOW DATABASES;'
    #         myCursor.execute(test_query)  # ExecuteReader in .NET
    #         for table in myCursor: # cursor is a tuples
    #             print(table)
    #         rows = myCursor.rowcount
    #         print("There is(are) database(s) ", rows)
    #         myCursor.close()
    #         conn.close()


# def main():
#     dbConnect = DBConnection()
#     if dbConnect.TestConnStr():
#         print("True")
#     else:
#         print("False")
#
#
# main()
