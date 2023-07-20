from HI6Cypher import Encription, Decription
class Loger :
    """Loger
    ~~~
    Loger Module makes for saving username and password\n
    or check them whether True or not"""
    def __init__(self, username, password) :
        self.__username = username
        self.__password = password
        self.__checked = ""

    def loging(self) :
        """### Loging : this method returns True or False or None
        ~~~
        if loging() == True -> means the password is correct\n
        elif loging() == False -> means the password is wronge\n
        else loging() == None -> means password has been saved"""
        encript_logs = Encription(self.__username, self.__password)
        decript_logs = Decription(self.__username)
        __decripted = decript_logs.Decript()
        if __decripted :
            self.__checker(self.__password, __decripted)
            return self.__checked
        else :
            encript_logs.Encript()
            return None
            
    def __checker(self, value_1, value_2) :
        if value_1 == value_2 :
            self.__checked = True
        else :
            self.__checked = False
