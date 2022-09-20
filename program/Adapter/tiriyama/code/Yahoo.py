# new

class Yahoo :
    __yahoo_logo = "yahoo"

    def __init__(self, string):
        self.__search_string = string

    def get_logo(self):
        return self.__yahoo_logo
    
    def search(self):
        return ("logo : {}   search : {}".format(self.__yahoo_logo, self.__search_string))