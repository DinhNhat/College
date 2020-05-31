from DAL.Admin_DAL import Admin_DAL
from DTO.Admin import Admin


class Admin_BUS:
    def __init__(self):
        self.__admin_dal = Admin_DAL()

    def GetConnectionStatus(self):
        return self.__admin_dal.GetConnectionStatus()

    def SelectAllAdmin(self):
        return self.__admin_dal.SelectAllAdmin()

    def ValidateAdmin(self, admin_model):
        return self.__admin_dal.ValidateAdmin(admin_model)

    def Admin_Insert(self, admin_model):
        return self.__admin_dal.Admin_Insert(admin_model)

    def Admin_Update(self, admin_model):
        return self.__admin_dal.Admin_Update(admin_model)

    def Admin_Delete(self, admin_model):
        return self.__admin_dal.Admin_Delete(admin_model)

    def GetExceptType(self):
        return self.__admin_dal.GetExceptType()

    def updatePasswordById(self, password, adminId):
        return self.__admin_dal.updatePasswordById(password, adminId)

    def getAdminInfoByIdAndPassword(self, id, password):
        return self.__admin_dal.getAdminInfoByIdAndPassword(id, password)

# def main():
#     admin_bus = Admin_BUS()
#     if admin_bus.TestConnection():
#         print("True")
#     else:
#         print("False")
#
#
# main()
