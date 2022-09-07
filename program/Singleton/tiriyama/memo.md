# Singleton

### Singleton とは

- インスタンスが1つしか存在しないデザインパターン

### Singleton の特徴

- インスタンスが外からnewされないようにコンストラクタをprivateに設定
　- pythonではコンストラクタをprivateにできなかったため、`__new__`内で`__instance`がNoneか否かを判定

### メリット

- インスタンスが1つしか存在しないため、下手に複製し、中身の変数を入れ替えたりするなどがない
- インスタンスが絶対に1つしか存在しないことを証明できる

### デメリット

- データに依存してしまう(単体テストでよろしくないかもしれない)


## コード備考欄

### `__new__`を使った理由
- 今回は唯一のインスタンス**生成**することが目的なため
    - `__init__`：インスタンスを**初期化**することが目的
    - `__new__`：インスタンスを**生成**することが目的


### 参考文献
[Singletonとは](https://qiita.com/shoheiyokoyama/items/c16fd547a77773c0ccc1)
[PythonでSingleton](https://qiita.com/ttsubo/items/c4af71ceba15b5b213f8)
[newとinitの違い](https://qiita.com/FGtatsuro/items/49f907a809e53b874b18)
