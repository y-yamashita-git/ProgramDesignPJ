# Adaptee

class Google :
    __google_logo = "google"

    def __init__(self, string):
        self.__search_string = string

    def get_logo(self):
        return self.__google_logo
    
    def search(self):
        return ("logo : {}   search : {}".format(self.__google_logo, self.__search_string))