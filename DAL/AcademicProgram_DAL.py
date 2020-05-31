from model.db_connect import DBConnect
import mysql.connector
# from DTO.Admin import Admin
from Views.Global import GlobalConst


class AcademicProgram_DAL:
    def __init__(self):
        self.__db_connect = DBConnect()
        self.__EXCEPT_TYPE = ''

    def GetExceptType(self):
        return self.__EXCEPT_TYPE

    def GetConnectionStatus(self):
        return self.__db_connect.GetConnectionStatus()

    def SelectAllAcaProgram(self):
        if self.GetConnectionStatus():
            conn = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            sql_selectAllAcaProgram = "select * from academicprogram"
            myCursor = conn.cursor()
            myCursor.execute(sql_selectAllAcaProgram)  # ExecuteReader in .NET
            records = myCursor.fetchall()
            print("Total number of rows in Academic program table is: ", myCursor.rowcount)

            print("\nPrinting each Academic program record")
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
            print("Error reading data from Academic program table")

    def AcaProgram_Insert(self, acaprogram_model):
        if acaprogram_model.IsAcaProgrameEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            mycursor = connection.cursor()
            code = acaprogram_model.GetProgramCode()
            name = acaprogram_model.GetProgramName()
            tuition = acaprogram_model.GetTuition()
            status = acaprogram_model.GetProStatus()
            sql_insert = "INSERT INTO academicprogram (programCode, programName, tuition, acaStatus) " \
                         "VALUES (%s, %s, %s, %s); "
            values = (code, name, tuition, status)

            mycursor.execute(sql_insert, values)
            connection.commit()
            print("Data inserted successfully into Academic program table using parameters")
            self.__EXCEPT_TYPE = 'Data inserted successfully into Academic program table'
            connection.close()
            return True
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def AcaProgram_Update(self, acaprogram_model):
        if acaprogram_model.IsAcaProgrameEmpty():
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        # active = str(admin.GetAdminActive())
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_updateAcaProgram = "UPDATE academicprogram SET programName = %s, tuition = %s, acaStatus = %s " \
                                  "WHERE programCode = %s;"
            values = (acaprogram_model.GetProgramName(), acaprogram_model.GetTuition(),
                      acaprogram_model.GetProStatus(), acaprogram_model.GetProgramCode())
            myCursor.execute(sql_updateAcaProgram, values)  # ExecuteNoneQuery in .NET
            connection.commit()
            print(myCursor.rowcount, "Record Updated successfully into Academic program table")
            self.__EXCEPT_TYPE = 'Record Updated successfully into Academic program table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to UPDATE record into Academic program table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def AcaProgram_Delete(self, acaprogram_model):
        if acaprogram_model.GetProgramCode() == "":
            self.__EXCEPT_TYPE = GlobalConst().GetExceptType('EI')
            return False
        try:
            connection = mysql.connector.connect(**self.__db_connect.GetConnectConfig())
            myCursor = connection.cursor()
            sql_deleteAcaProgram = "DELETE FROM academicprogram WHERE programCode = %s"
            parameter = acaprogram_model.GetProgramCode()
            myCursor.execute(sql_deleteAcaProgram, (parameter,))
            connection.commit()
            print("Record Deleted successfully ")
            self.__EXCEPT_TYPE = 'Record Deleted successfully from Academic program table'
            myCursor.close()
            connection.close()
            print('MySQL connection is closed.')
            return True
        except mysql.connector.Error as error:
            print("SQL command ERROR. Failed to DELETE record from Academic program table {}".format(error))
            self.__EXCEPT_TYPE = error.msg
            return False

    def GetAllAcaProgramName(self):
        names = []
        lsProgram = self.SelectAllAcaProgram()
        for program in lsProgram:
            names.append(program[1])
        return names

    def GetProgramCodeByName(self, name):
        lsPrograms = self.SelectAllAcaProgram()
        for program in lsPrograms:
            if program[1] == name:
                return program[0]
            else:
                continue

    def GetColumnHeaders(self):
        col_headers = ['PROGRAM CODE', 'PROGRAM NAME', 'TUITION', 'PROGRAM STATUS']
        return col_headers

    def getProgramNameByCode(self, code):
        lsPrograms = self.SelectAllAcaProgram()
        for program in lsPrograms:
            if program[0] == code:
                return program[1]
            else:
                continue
        return False


# def main():
#     aca = AcademicProgram_DAL()
#     name = aca.getProgramNameByCode('CPCT')
#     if name is not False:
#         print(name)
#     else:
#         print('Failed to fetch info')
#
#
# main()

