from DAL.Course_DAL import Course_DAL
from DTO.Admin import Admin


class Course_BUS:
    def __init__(self):
        self.__course_dal = Course_DAL()

    def GetConnectionStatus(self):
        return self.__course_dal.GetConnectionStatus()

    def SelectAllCourse(self):
        return self.__course_dal.SelectAllCourse()

    def Course_Insert(self, course_model):
        return self.__course_dal.Course_Insert(course_model)

    def Course_Update(self, course_model):
        return self.__course_dal.Course_Update(course_model)

    def Course_Delete(self, course_model):
        return self.__course_dal.Course_Delete(course_model)

    def GetExceptType(self):
        return self.__course_dal.GetExceptType()

    def GetDataSource(self):
        return self.__course_dal.GetDataSource()

    def GetColumnHeaders(self):
        return self.__course_dal.GetColumnHeaders()

    def GetCourseCode(self):
        return self.__course_dal.GetCourseCode()

# def main():
#     admin_bus = Admin_BUS()
#     if admin_bus.TestConnection():
#         print("True")
#     else:
#         print("False")
#
#
# main()
