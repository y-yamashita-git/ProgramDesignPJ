### Factory Methodとは
* インスタンス作成時、サブクラスに処理を任せるデザインパターン

### Factory Methodの特徴
1. インスタンス生成を管理するクラスと、インスタンス生成処理をするクラスで分かれている

### Factory Methodのメリット
1. 具象クラスに依存せずにインスタンスを生成する
2. オブジェクトの生成を用意することで、変更や総入れ替えが用意

### Factory MethodとAbstract Factoryの違い
1. 何を抽象化するのか
    * Abstract Factory：インスタンス生成のインターフェース（オブジェクト）
    * Factory Method：インスタンス生成のインターフェースおよび処理(メソッド)

### Factory Methodの使い道
1. サブクラス間でペアになる場合(Factory<->Product)
2. 今後コードが増え、複雑性が増す場合


------------

### 依存性とは
* クラスやメソッドに、固定値が入っていることを指す。また「依存性の注入」とはクラスやメソッド内の固定値を外から参照することを指す

------------

# 個人的疑問点(調べればいいなと思う)
1. 必然的にクラスの数はAbstract Factoryよりも多くなるが、クラス数が増えた場合クラスの管理はどうするのか

### 参考文献
1. Factory Methodとは何か：https://blog.ecbeing.tech/entry/2021/01/20/114000
2. Factory Methodの構成：http://www.itsenka.com/contents/development/designpattern/factory_method.html
3. コードの書き方：http://teacher.nagano-nct.ac.jp/fujita/LightNEasy.php?page=FactoryMethod
