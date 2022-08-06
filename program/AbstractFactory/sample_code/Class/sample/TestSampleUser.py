import sys
from SampleItemClass import Tester,TestEmail,TestSex,TestPasswoed
sys.path.append('../master/')
from User import User

class TestSampleUser(User):
    def __init__(self):
        pass

    def add_name(self):
        return Tester().check()

    def add_email(self):
        return TestEmail().check()

    def add_password(self):
        return TestPasswoed().check()

    def add_sex(self):
        return TestSex().check()