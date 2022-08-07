class Main {
/*
  中身を切り替えたい場合、以下のようにする
  account は実体を気にする必要がない
  Account account = new AccountYahoo()
*/

  Account account = new AccountGoogle()

  Name name = account.createName("hoge")
  Email email = account.createEmail("fuga")
  print(name)
  print(email)
}

/* 
  期待値
  > hoge
  > fuga@gmail.com
*/