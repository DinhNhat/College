
class Admin:
    def __init__(self):
        self.__adminId = ''
        self.__adminLoginName = ''
        self.__adminPasswd = ''
        self.__adminActive = -1

    def SetAdminId(self, adId):
        self.__adminId = adId

    def SetAdminLoginName(self, name):
        self.__adminLoginName = name

    def SetAdminPasswd(self, pw):
        self.__adminPasswd = pw

    def SetAdminActive(self, active):
        self.__adminActive = active

    def GetAdminId(self):
        return self.__adminId

    def GetAdminLoginName(self):
        return self.__adminLoginName

    def GetAdminPasswd(self):
        return self.__adminPasswd

    def GetAdminActive(self):
        return self.__adminActive

    def IsAnEmptyAdmin(self):
        if self.__adminId == "" or self.__adminLoginName == "":
            return True
        else:
            return False