from DAL.Student_DAL import Student_DAL
from DTO.Professor import Professor


class Student_BUS:
    def __init__(self):
        self.__student_dal = Student_DAL()

    def GetConnectionStatus(self):
        return self.__student_dal.GetConnectionStatus()

    def SelectAllStudent(self):
        return self.__student_dal.SelectAllStudent()

    def Student_Insert(self, student_model):
        return self.__student_dal.Student_Insert(student_model)

    def Student_Update(self, student_model):
        return self.__student_dal.Student_Update(student_model)

    def Student_Delete(self, student_model):
        return self.__student_dal.Student_Delete(student_model)

    def GetExceptType(self):
        return self.__student_dal.GetExceptType()

    def GetDatSource(self):
        return self.__student_dal.GetDataSource()

    def GetColumnHeaders(self):
        return self.__student_dal.GetColumnHeaders()

    def GetActive(self):
        return self.__student_dal.GetActive()

    def getRead_Only_StudentSchedule(self, studentId):
        return self.__student_dal.getRead_Only_StudentSchedule(studentId)

    def getStudentInfoByIdAndPassword(self, id, password):
        return self.__student_dal.getStudentInfoByIdAndPassword(id, password)

    def validateStudent(self, student_model):
        return self.__student_dal.validateStudent(student_model)

    def getColumnHeadersForScheduleTb(self):
        return self.__student_dal.getColumnHeadersForScheduleTb()

    def updatePasswordById(self, password, studentId):
        return self.__student_dal.updatePasswordById(password, studentId)

# def main():
#     admin_bus = Admin_BUS()
#     if admin_bus.TestConnection():
#         print("True")
#     else:
#         print("False")
#
#
# main()
