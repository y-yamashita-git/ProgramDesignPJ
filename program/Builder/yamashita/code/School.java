//教室名を設定するクラス定義
class ClassName(string)

//Builder
@Abstract
class Class()

//Director
@Abstract
class School{
    fun setClassName(string) : ClassName
    fun createClass() : Class 
}