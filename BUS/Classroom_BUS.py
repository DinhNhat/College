from DAL.Classroom_DAL import Classroom_DAL
from DTO.Admin import Admin


class Classroom_BUS:
    def __init__(self):
        self.__classroom_dal = Classroom_DAL()

    def GetConnectionStatus(self):
        return self.__classroom_dal.GetConnectionStatus()

    def SelectAllClassroom(self):
        return self.__classroom_dal.SelectAllClassroom()

    def Classroom_Insert(self, classroom_model):
        return self.__classroom_dal.Classroom_Insert(classroom_model)

    def Classroom_Update(self, admin_model):
        return self.__classroom_dal.Classroom_Update(admin_model)

    def Classroom_Delete(self, admin_model):
        return self.__classroom_dal.Classroom_Delete(admin_model)

    def GetExceptType(self):
        return self.__classroom_dal.GetExceptType()

    def GetColumnHeaders(self):
        return self.__classroom_dal.GetColumnHeaders()

    def GetClassroomCode(self):
        return self.__classroom_dal.GetClassroomCode()

# def main():
#     admin_bus = Admin_BUS()
#     if admin_bus.TestConnection():
#         print("True")
#     else:
#         print("False")
#
#
# main()
