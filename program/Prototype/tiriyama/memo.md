### Prototypeとは
* 元となるインスタンスから新しいインスタンスを生成するパターン

### Prototypeの構成
* `Prototype`：複製するためのメソッドが用意されたインスタンス
* `ConcretePrototype`：`Prototype`継承

### サンプル問題
* 文字装飾(markdown形式)

### 用意する機能
* 箇条書き(指定した文字の前に`*`を追加する)

### 用意するクラス
* `Markdown`：`Prototype`に該当
* `BulletPoint`：`ConcretePrototype`に該当し、指定した文字の前に`*`を付ける

### 使用する目的
* 本番環境で実装することはあまりなさそう
* 実装するのであれば、コピーの処理をインスタンス生成で楽にするためかなと予想
* 名前の通り試しに動くか確かめてみる際に使用しそう

### 参考文献
https://www.techscore.com/tech/DesignPattern/Prototype
