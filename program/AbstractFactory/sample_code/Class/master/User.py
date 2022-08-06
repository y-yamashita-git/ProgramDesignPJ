from tokenize import Name

#AbstractFactory
class User:
    def __init__(self, user_factory):
        self.factroy = user_factory

    def add_name(self):
        pass

    def add_email(self):
        pass

    def add_password(self):
        pass

    def add_sex(self):
        pass
