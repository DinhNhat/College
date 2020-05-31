from DAL.AcademicProgram_DAL import AcademicProgram_DAL
from DTO.Admin import Admin


class AcaProgram_BUS:
    def __init__(self):
        self.__aca_program_dal = AcademicProgram_DAL()

    def GetConnectionStatus(self):
        return self.__aca_program_dal.GetConnectionStatus()

    def SelectAllAcaProgram(self):
        return self.__aca_program_dal.SelectAllAcaProgram()

    def AcaProgram_Insert(self, acaprogram_model):
        return self.__aca_program_dal.AcaProgram_Insert(acaprogram_model)

    def AcaProgram_Update(self, acaprogram_model):
        return self.__aca_program_dal.AcaProgram_Update(acaprogram_model)

    def AcaProgram_Delete(self, acaprogram_model):
        return self.__aca_program_dal.AcaProgram_Delete(acaprogram_model)

    def GetExceptType(self):
        return self.__aca_program_dal.GetExceptType()

    def GetAllAcaProgramName(self):
        return self.__aca_program_dal.GetAllAcaProgramName()

    def GetProgramCodeByName(self, name):
        return self.__aca_program_dal.GetProgramCodeByName(name)

    def GetColumnHeaders(self):
        return self.__aca_program_dal.GetColumnHeaders()

    def getProgramNameByCode(self, code):
        return self.__aca_program_dal.getProgramNameByCode(code)

# def main():
#     admin_bus = Admin_BUS()
#     if admin_bus.TestConnection():
#         print("True")
#     else:
#         print("False")
#
#
# main()
