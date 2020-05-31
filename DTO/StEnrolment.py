class Enrolment:
    def __init__(self, courseCode='', stId='', proId='', sem='', term=0, enDate='', GPA=0):
        self.__courseCode = courseCode
        self.__studentId = stId
        self.__proId = proId
        self.__semester = sem
        self.__term = term
        self.__GPA = GPA
        self.__enrolDate = enDate
        
    @property
    def CourseCode(self):
        return self.__courseCode
    
    @CourseCode.setter
    def CourseCode(self, value):
        self.__courseCode = value
        
    @property
    def StudentId(self):
        return self.__studentId
    
    @StudentId.setter
    def StudentId(self, value):
        self.__studentId = value
        
    @property
    def ProfessorId(self):
        return self.__proId
    
    @ProfessorId.setter
    def ProfessorId(self, value):
        self.__proId = value
        
    @property
    def Semester(self):
        return self.__semester
    
    @Semester.setter
    def Semester(self, value):
        self.__semester = value
    
    @property
    def Term(self):
        return self.__term
    
    @Term.setter
    def Term(self, value):
        self.__term = value
        
    @property
    def GPA(self):
        return self.__GPA

    @GPA.setter
    def GPA(self, value):
        self.__GPA = value

    @property
    def EnrolmentDate(self):
        return self.__enrolDate

    @EnrolmentDate.setter
    def EnrolmentDate(self, value):
        self.__enrolDate = value

    def IsStEnrolmentEmpty(self):
        if self.CourseCode == "" and self.StudentId == "" and self.ProfessorId == "":
            return True
        else:
            return False