class Schedule:

    def __init__(self, courseCode='', proId='', teachDate='', semester='', startDate='', endDate='', classRoomCode='',  timeStart='00:01:00', periodHour='0.00'):
        self.__course_code = courseCode
        self.__professor_id = proId
        self.__teach_date = teachDate
        self.__time_start = timeStart
        self.__period_hour = periodHour
        self.__semester = semester
        self.__start_date_semester = startDate
        self.__end_date_semester = endDate
        self.__classroom_code = classRoomCode

    @property
    def CourseCode(self):
        return self.__course_code

    @CourseCode.setter
    def CourseCode(self, value):
        self.__course_code = value

    @property
    def ProfessorId(self):
        return self.__professor_id

    @ProfessorId.setter
    def ProfessorId(self, value):
        self.__professor_id = value

    @property
    def TeachDate(self):
        return self.__teach_date
    
    @TeachDate.setter
    def TeachDate(self, value):
        self.__teach_date = value
        
    @property
    def TimeStart(self):
        return self.__time_start
    
    @TimeStart.setter
    def TimeStart(self, value):
        self.__time_start = value
        
    @property
    def PeriodHour(self):
        return self.__period_hour
    
    @PeriodHour.setter
    def PeriodHour(self, value):
        self.__period_hour = value
        
    @property
    def Semester(self):
        return self.__semester
    
    @Semester.setter
    def Semester(self, value):
        self.__semester = value
        
    @property
    def StartDateSemester(self):
        return self.__start_date_semester
    
    @StartDateSemester.setter
    def StartDateSemester(self, value):
        self.__start_date_semester = value

    @property
    def EndDateSemester(self):
        return self.__end_date_semester

    @EndDateSemester.setter
    def EndDateSemester(self, value):
        self.__end_date_semester = value

    @property
    def ClassroomCode(self):
        return self.__classroom_code

    @ClassroomCode.setter
    def ClassroomCode(self, value):
        self.__classroom_code = value

    def IsScheduleEmpty(self):
        if self.CourseCode == "" or self.ProfessorId == "" or self.TeachDate == "":
            return True
        else:
            return False

    def isKeyCodeEmpty(self):
        if self.CourseCode == "" and self.ProfessorId == "" and self.TeachDate == "" and self.Semester == "":
            return True
        else:
            return False