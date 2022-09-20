from Google import Google
from Yahoo import Yahoo

# Adapter
class Adapter(Google):

    def __init__(self, string):
        self.yahoo = Yahoo(string)
    
    def get_logo(self):
        return self.yahoo.get_logo()
    
    def search(self):
        return self.yahoo.search()