class Professor:
    def __init__(self):
        self.__professor_id = ''
        self.__pro_fullname = ''
        self.__pro_gender = ''
        self.__pro_email = ''
        self.__pro_address = ''
        self.__pro_phone = '12345'
        self.__pro_is_active = 1
        self.__pro_password = '123'
        self.__pro_degree_code = ''

    @property
    def ProfessorId(self):
        return self.__professor_id

    @ProfessorId.setter
    def ProfessorId(self, value):
        self.__professor_id = value

    @property
    def FullName(self):
        return self.__pro_fullname

    @FullName.setter
    def FullName(self, value):
        self.__pro_fullname = value

    @property
    def Gender(self):
        return self.__pro_gender 
    
    @Gender.setter
    def Gender(self, value):
        self.__pro_gender = value
    
    @property
    def Email(self):
        return self.__pro_email 
    
    @Email.setter
    def Email(self, value):
        self.__pro_email = value
        
    @property
    def Address(self):
        return self.__pro_address
    
    @Address.setter
    def Address(self, value):
        self.__pro_address = value

    @property
    def Phone(self):
        return self.__pro_phone

    @Phone.setter
    def Phone(self, value):
        self.__pro_phone = value

    @property
    def Active(self):
        return self.__pro_is_active

    @Active.setter
    def Active(self, value):
        self.__pro_is_active = value

    @property
    def Password(self):
        return self.__pro_password

    @Password.setter
    def Password(self, value):
        self.__pro_password = value

    @property
    def DegreeCode(self):
        return self.__pro_degree_code

    @DegreeCode.setter
    def DegreeCode(self, value):
        self.__pro_degree_code = value
    
    # def SetProfessorId(self, id):
    #     self.__professor_id = id
    #
    # def SetProfessorFullName(self, fullname):
    #     self.__pro_fullname = fullname
    #
    # def SetProfessorGender(self, gender):
    #     self.__pro_gender = gender
    #
    # def SetProfessorEmail(self, email):
    #     self.__pro_email = email
    #
    # def SetProfessorAddress(self, addr):
    #     self.__pro_address = addr
    #
    # def SetProfessorPhone(self, phone):
    #     self.__pro_phone = phone
    #
    # def SetProfessorIsActive(self, active):
    #     self.__pro_is_active = active
    #
    # def SetProfessorPasswd(self, passw):
    #     self.__pro_password = passw
    #
    # def SetProfessorDegreeCode(self, de_code):
    #     self.__pro_degree_code = de_code
    #
    # def GetProfessorId(self):
    #     return self.__professor_id
    #
    # def GetProfessorFullName(self):
    #     return self.__pro_fullname
    #
    # def GetProfessorGender(self):
    #     return self.__pro_gender
    #
    # def GetProfessorEmail(self):
    #     return self.__pro_email
    #
    # def GetProfessorAddress(self):
    #     return self.__pro_address
    #
    # def GetProfessorPhone(self):
    #     return self.__pro_phone
    #
    # def GetProfessorIsActive(self):
    #     return self.__pro_is_active
    #
    # def GetProfessorPassword(self):
    #     return self.__pro_password
    #
    # def GetProfessorDegreeCode(self):
    #     return self.__pro_degree_code

    def IsProfessorEmpty(self):
        if self.ProfessorId == "" or self.Email == "" or self.FullName == "":
            return True
        else:
            return False

    def __str__(self):
        return "\nId: " + self.ProfessorId + "\nFull name: " + \
               self.FullName + "\nGender: " + self.Gender + "\nEmail: " + \
               self.Email + "\nAddress: " + self.Address + "\nPhone: " + self.Phone + \
               "\nActive: " + str(self.Active) + "\nPassword: " + self.Password + "\nDegree code: " + self.DegreeCode
