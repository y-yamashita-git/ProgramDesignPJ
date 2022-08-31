class Main{
    Factory factory = new AccountFactory();
    GoogleAccount account = (GoogleAccount) factory.create("hoge", "hoge@gmail.com");
    account.toString();
}
