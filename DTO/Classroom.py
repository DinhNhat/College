
class Classroom:
    def __init__(self):
        self.__classroom_code = ''
        self.__classroom_number = ''
        self.__building_name = ''
        self.__location_name = ''

    def SetClassroomCode(self, code):
        self.__classroom_code = code

    def SetClassroomNumber(self, num):
        self.__classroom_number = num

    def SetBuildingName(self, name):
        self.__building_name = name

    def SetLocationName(self, location):
        self.__location_name = location

    def GetClassroomCode(self):
        return self.__classroom_code

    def GetClassroomNumber(self):
        return self.__classroom_number

    def GetBuildingName(self):
        return self.__building_name

    def GetLocationName(self):
        return self.__location_name

    def IsClassroomEmpty(self):
        if self.__classroom_code == "" or self.__classroom_number == "":
            return True
        else:
            return False
