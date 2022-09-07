class TiriyamaComputer :
    __mac_address = "aa:bb:cc:dd"
    __instance = None
    def __new__(self):
        if self.__instance is None:
            self.__instance = super().__new__(self)
        return self.__instance
    def get_mac_address(self):
        return self.__mac_address
    def get_instance(self):
        return self.__instance

