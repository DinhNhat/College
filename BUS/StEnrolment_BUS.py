from DAL.StEnrolment_DAL import Enrolment_DAL


class Enrolment_BUS:
    def __init__(self):
        self.__enrolment_dal = Enrolment_DAL()

    def GetConnectionStatus(self):
        return self.__enrolment_dal.GetConnectionStatus()

    def SelectAllEnrolment(self):
        return self.__enrolment_dal.SelectAllEnrolment()

    def Enrolement_Insert(self, enrolment_model):
        return self.__enrolment_dal.Enrolement_Insert(enrolment_model)

    def Enrolement_DeleteByKeyCode(self, enrolment_model):
        return self.__enrolment_dal.Enrolement_DeleteByKeyCode(enrolment_model)

    # def Student_Update(self, student_model):
    #     return self.__enrolment_dal.Student_Update(student_model)
    #
    # def Student_Delete(self, student_model):
    #     return self.__enrolment_dal.Student_Delete(student_model)
    #
    # def GetExceptType(self):
    #     return self.__enrolment_dal.GetExceptType()
    #
    # def GetDatSource(self):
    #     return self.__enrolment_dal.GetDataSource()

    def GetColumnHeaders(self):
        return self.__enrolment_dal.GetColumnHeaders()

    def GetExceptType(self):
        return self.__enrolment_dal.GetExceptType()

    def GetDataSource(self):
        return self.__enrolment_dal.GetDataSource()

    def updateStudentGPAByConditions(self, GPA, courseCode, studentId, professorId, semester, term):
        return self.__enrolment_dal.updateStudentGPAByConditions(GPA, courseCode, studentId, professorId, semester, term)

    # def GetActive(self):
    #     return self.__enrolment_dal.GetActive()