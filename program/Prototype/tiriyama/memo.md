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

### 参考文献
https://www.techscore.com/tech/DesignPattern/Prototype
