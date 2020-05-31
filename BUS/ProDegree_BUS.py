from DAL.ProDegree_DAL import ProDegree_DAL
from DTO.ProfessorDegree import ProfessorDegree


class ProDegree_BUS:
    def __init__(self):
        self.__proDegree_dal = ProDegree_DAL()

    def GetConnectionStatus(self):
        return self.__proDegree_dal.GetConnectionStatus()

    def SelectAllDegree(self):
        return self.__proDegree_dal.SelectAllDegree()

    def GetDegreeCode(self, degreeName):
        return self.__proDegree_dal.GetDegreeCode(degreeName)

    def GetAllDegreeName(self):
        return self.__proDegree_dal.GetAllDegreeName(self.__proDegree_dal.SelectAllDegree())

    def Degree_Insert(self, degree_model):
        return self.__proDegree_dal.Degree_Insert(degree_model)

    def Degree_Update(self, degree_model):
        return self.__proDegree_dal.Degree_Update(degree_model)

    def Degree_Delete(self, degree_model):
        return self.__proDegree_dal.Degree_Delete(degree_model)

    def GetExceptType(self):
        return self.__proDegree_dal.GetExceptType()

    def GetColumnHeaders(self):
        return self.__proDegree_dal.GetColumnHeaders()

    def GetDegreeNameByCode(self, code):
        return self.__proDegree_dal.GetDegreeNameByCode(code)

# def main():
#     admin_bus = Admin_BUS()
#     if admin_bus.TestConnection():
#         print("True")
#     else:
#         print("False")
#
#
# main()
