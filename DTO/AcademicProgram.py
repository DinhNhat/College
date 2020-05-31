
class AcademicProgram:
    def __init__(self):
        self.__program_code = ''
        self.__program_name = ''
        self.__pro_tuition = 0
        self.__program_status = ''

    def SetProgramCode(self, code):
        self.__program_code = code

    def SetProgramName(self, name):
        self.__program_name = name

    def SetTuition(self, tui):
        # tuition = format(tui, ',.2f')
        self.__pro_tuition = tui

    def SetProStatus(self, status):
        self.__program_status = status

    def GetProgramCode(self):
        return self.__program_code

    def GetProgramName(self):
        return self.__program_name

    def GetTuition(self):
        return self.__pro_tuition

    def GetProStatus(self):
        return self.__program_status

    def IsAcaProgrameEmpty(self):
        if self.__program_code == "" or self.__program_name == "":
            return True
        else:
            return False