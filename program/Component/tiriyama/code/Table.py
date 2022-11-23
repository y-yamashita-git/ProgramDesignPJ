from HtmlResult import HtmlResult

# Composite
class Table(HtmlResult):
    __html_table_list = []
    __html_table_name = ""
    def __init__(self,table_name):
        self.__html_table_name = "<th>" + table_name + "</th>"
        self.__html_table_list.append(self.__html_table_name)
    
    def add_item(self, item):
        self.__html_table_list.append(item.get_html())

    def get_html(self):
        for item in self.__html_table_list:
            print("<tr>")
            print(item)
            print("/<tr>")