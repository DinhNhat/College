class Student:
    def __init__(self):
        self.__st_id = ''
        self.__st_fullname = ''
        self.__st_gender = ''
        self.__st_dateOfBirth = ''
        self.__st_country = ''
        self.__st_current_address = ''
        self.__st_email = ''
        self.__st_isActive = 1
        self.__st_password = '123'
        self.__st__registeredDate = ''
        self.__st_programCode = ''

    @property
    def StId(self):
        return self.__st_id

    @StId.setter
    def StId(self, value):
        self.__st_id = value

    @property
    def StFullname(self):
        return self.__st_fullname

    @StFullname.setter
    def StFullname(self, value):
        self.__st_fullname = value

    @property
    def StGender(self):
        return self.__st_gender

    @StGender.setter
    def StGender(self, value):
        self.__st_gender = value

    @property
    def StDateOfBirth(self):
        return self.__st_dateOfBirth

    @StDateOfBirth.setter
    def StDateOfBirth(self, value):
        self.__st_dateOfBirth = value

    @property
    def StCountry(self):
        return self.__st_country

    @StCountry.setter
    def StCountry(self, value):
        self.__st_country = value

    @property
    def StCurrentAddress(self):
        return self.__st_current_address

    @StCurrentAddress.setter
    def StCurrentAddress(self, value):
        self.__st_current_address = value

    @property
    def StEmail(self):
        return self.__st_email

    @StEmail.setter
    def StEmail(self, value):
        self.__st_email = value

    @property
    def StActive(self):
        return self.__st_isActive

    @StActive.setter
    def StActive(self, value):
        self.__st_isActive = value

    @property
    def StPassword(self):
        return self.__st_password

    @StPassword.setter
    def StPassword(self, value):
        self.__st_password = value

    @property
    def StRegisteredDate(self):
        return self.__st__registeredDate

    @StRegisteredDate.setter
    def StRegisteredDate(self, value):
        self.__st__registeredDate = value

    @property
    def StProgramCode(self):
        return self.__st_programCode

    @StProgramCode.setter
    def StProgramCode(self, value):
        self.__st_programCode = value

    def IsStudentEmpty(self):
        if self.__st_id == "" or self.__st_fullname == "" or self.__st_email == "":
            return True
        else:
            return False

    def __str__(self):
        return "\nId: " + self.StId + "\nName: " + self.StFullname + "\nGender: " + self.StGender + \
               "\nDate of birth: " + str(self.StDateOfBirth) + "\nCountry: " + self.StCountry + "\nCurrent address: " \
               + self.StCurrentAddress + "\nEmail: " + self.StEmail + "\nPassword: " + self.StPassword + \
               "\nRegistered date: " + str(self.StRegisteredDate) + "\nProgram code: " + self.StProgramCode
