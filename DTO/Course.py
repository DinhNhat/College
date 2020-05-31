class Course:
    def __init__(self):
        self.__code = ''
        self.__description = ''
        self.__credit = 0
        self.__outline = ''
        self.__programCode = ''

    @property
    def Code(self):
        return self.__code

    @Code.setter
    def Code(self, value):
        self.__code = value

    @property
    def Description(self):
        return self.__description

    @Description.setter
    def Description(self, value):
        self.__description = value

    @property
    def Credit(self):
        return self.__credit

    @Credit.setter
    def Credit(self, value):
        self.__credit = value

    @property
    def Outline(self):
        return self.__outline

    @Outline.setter
    def Outline(self, value):
        self.__outline = value

    @property
    def ProgramCode(self):
        return self.__programCode

    @ProgramCode.setter
    def ProgramCode(self, value):
        self.__programCode = value

    def IsCourseEmpty(self):
        if self.__code == "" or self.__description == "" or self.__credit == 0:
            return True
        else:
            return False