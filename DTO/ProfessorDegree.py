
class ProfessorDegree:
    def __init__(self, code='', name ='', sal_index=0):
        self.__degree_code = code
        self.__degree_name = name
        self.__salary_index = sal_index

    def SetDegreeCode(self, code):
        self.__degree_code = code

    def SetDegreeName(self, name):
        self.__degree_name = name

    def SetSalaryIndex(self, sal_index):
        self.__salary_index = sal_index

    def GetDegreeCode(self):
        return self.__degree_code

    def GetDegreeName(self):
        return self.__degree_name

    def GetSalaryIndex(self):
        return self.__salary_index

    def IsDegreeEmpty(self):
        if self.__degree_code == "" or self.__degree_name == "":
            return True
        else:
            return False