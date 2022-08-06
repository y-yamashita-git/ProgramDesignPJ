import sys
sys.path.append('../master/')
from itemClass import Name,Password,Sex,Email

class Tester(Name):
    def check(self):
        return "Tester"

class TestPasswoed:
    def check(self):
        return "hogehoge"

class TestSex:
    def check(self):
        return "man"

class TestEmail:
    def check(self):
        return "test@hoge.com"
