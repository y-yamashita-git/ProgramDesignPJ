//Factory
class Factory{
    /* テンプレート */
    Product create(String name, String email):
    /* 抽象メソッド */
	abstract Product createProduct(String name, String email):
}

//Product
class Product{
    String toString():
}
