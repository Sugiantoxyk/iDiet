class RegisterObject():
    def __init__(self, username, firstname, lastname, password):
        self.__username = username
        self.__firstname = firstname
        self.__lastname = lastname
        self.__password = password

    def set_username(self, username):
        self.__username = username

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def set_password(self, password):
        self.__password = password

    def get_username(self):
        return self.__username

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_password(self):
        return self.__password