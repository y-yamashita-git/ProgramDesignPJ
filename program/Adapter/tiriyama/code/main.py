from Google import Google
from Yahoo import Yahoo
from Chrome import Chrome

if __name__ == '__main__':

    # Google検索呼び出し
    google_search = Google("hogehoge1")
    print(Chrome.search(google_search))

    # Yahoo検索呼び出し
    yahoo_search = Yahoo("hogehoge2")
    print(Chrome.search(yahoo_search))

