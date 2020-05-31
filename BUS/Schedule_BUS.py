from DAL.Schedule_DAL import Schedule_DAL


class Schedule_BUS:

    def __init__(self):
        self.__schedule_dal = Schedule_DAL()

    def GetConnectionStatus(self):
        return self.__schedule_dal.GetConnectionStatus()

    def SelectAllSchedule(self):
        return self.__schedule_dal.SelectAllSchedule()

    def Schedule_Insert(self, schedule_model):
        return self.__schedule_dal.Schedule_Insert(schedule_model)

    def Schedule_Delete(self, schedule_model):
        return self.__schedule_dal.Schedule_Delete(schedule_model)

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
        return self.__schedule_dal.GetColumnHeaders()

    def GetExceptType(self):
        return self.__schedule_dal.GetExceptType()

    def GetDataSource(self):
        return self.__schedule_dal.GetDataSource()

    def getCourseAvailabilityInfo(self):
        return self.__schedule_dal.getCourseAvailabilityInfo()
