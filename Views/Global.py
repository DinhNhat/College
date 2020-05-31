class GlobalConst:
    def __init__(self):
        self.__IMAGES_DIC = {'Add': 'add', 'Update': 'update',
                             'Delete': 'delete', 'LoadData': 'database',
                             'Search': 'search', 'Database': 'database', 'Exit': 'cancel', 'Login': 'login'}
        self.__EXCEPT_TYPE = {'EI': 'Empty Input', 'CP': 'Connection Problem',
                              'UE': 'User does NOT exist in database', 'ID': 'Invalid user name or password',
                              'NC': 'Nothing changed', 'PK': 'Duplicate primary key'}
        self.__countries = ['Canda', 'US', 'UK', 'Australia', 'New Zealand', 'Germany']

        self.__COLORS = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0', '#f7f7f7', '#fddbc7', '#f4a582',
                         '#d6604d', '#b2182b', '#67001f', '#fee08b']

        self.__COUNTRIES = ['Canada', 'US', 'France', 'UK', 'Spain', 'Japan', 'South Korea',
                            'Indonesia', 'Philippines', 'Laos', 'India', 'Vietnam', 'Italy', 'Germany',
                            'Mexico', 'Brazil', 'Argentina', 'Angola', 'South Africa', 'Egypt']

    def getImage(self, key):
        return self.__IMAGES_DIC[key]

    def GetExceptType(self, key):
        return self.__EXCEPT_TYPE[key]

    def SetExceptType(self, key, value):
        self.__EXCEPT_TYPE[key] = value

    def GetColorsByIndex(self, index):
        return self.__COLORS[index]

    def GetCountriesList(self):
        return self.__COUNTRIES
