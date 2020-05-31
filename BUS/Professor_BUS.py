from DAL.Professor_DAL import Professor_DAL
from DTO.Professor import Professor


class Professor_BUS:
    def __init__(self):
        self.__professor_dal = Professor_DAL()

    def GetConnectionStatus(self):
        return self.__professor_dal.GetConnectionStatus()

    def SelectAllProfessor(self):
        return self.__professor_dal.SelectAllProfessor()

    def Professor_Insert(self, professor_model):
        return self.__professor_dal.Professor_Insert(professor_model)

    def Professor_Update(self, professor_model):
        return self.__professor_dal.Professor_Update(professor_model)

    def Professor_Delete(self, professor_model):
        return self.__professor_dal.Professor_Delete(professor_model)

    def GetExceptType(self):
        return self.__professor_dal.GetExceptType()

    def GetColumnHeaders(self):
        return self.__professor_dal.GetColumnHeaders()

    def GetDataSource(self):
        return self.__professor_dal.GetDataSource()

    def ValidateProfessor(self, professor_model):
        return self.__professor_dal.ValidateProfessor(professor_model)

    def GetProfessorInfoByIdAndPasswd(self, id, password):
        return self.__professor_dal.GetProfessorInfoByIdAndPasswd(id, password)

    def GetStudentGrade(self, professorId):
        return self.__professor_dal.GetStudentGrade(professorId)

    def GetColumnHeadersForStudentGradeTb(self):
        return self.__professor_dal.GetColumnHeadersForStudentGradeTb()

    def GetInfoByRowStGradeTable(self, professorId, row_index):
        return self.__professor_dal.GetInfoByRowStGradeTable(professorId, row_index)

    def updatePasswordById(self, password, id):
        return self.__professor_dal.updatePasswordById(password, id)

    def getRead_Only_Schedule(self, proId):
        return self.__professor_dal.getRead_Only_Schedule(proId)

    def getColumnHeadersScheduleTb(self):
        return self.__professor_dal.getColumnHeadersScheduleTb()


# def main():
#     admin_bus = Admin_BUS()
#     if admin_bus.TestConnection():
#         print("True")
#     else:
#         print("False")
#
#
# main()
