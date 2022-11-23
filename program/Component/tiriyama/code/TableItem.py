from HtmlResult import HtmlResult

# Leaf
class TableItem(HtmlResult):
    __html_message = ""
    def __init__(self,item):
        self.__html_message = "<td>" + item + "</td>"
    
    def get_html(self):
        return self.__html_message
