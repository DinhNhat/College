import mysql.connector
from mysql.connector import Error

HOST_NAME = 'localhost'
USER_NAME = 'root'
PASSWORD = 'sa123'
DATABASE = 'college_pygui'


def DB_Connect():
    try:
        connection = mysql.connector.connect(host=HOST_NAME, user=USER_NAME, password=PASSWORD)

        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
        return True
    except Error as e:
        print("Error while connecting to MySQL", e)
        return False
    except Exception as e:
        print(e)
        return False


class DBConnect:
    def __init__(self):
        self.__connectionStatus = DB_Connect()
        self.__connection_config_dict = {
            'host': HOST_NAME,
            'user': USER_NAME,
            'password': PASSWORD,
            'db': DATABASE
        }

    def GetConnectConfig(self):
        return self.__connection_config_dict

    def GetConnectionStatus(self):
        return self.__connectionStatus


# def main():
#     db_connect = DBConnect()
#     print(db_connect.GetConnectionStatus())
#
#
# main()
