from HtmlResult import HtmlResult
from Table import Table
from TableItem import TableItem

if __name__ == "__main__":
    fruit_table = Table("fruit")
    fruit_table.add_item(TableItem("リンゴ"))
    fruit_table.add_item(TableItem("みかん"))
    fruit_table.get_html()