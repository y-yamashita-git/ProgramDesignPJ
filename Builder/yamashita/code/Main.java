class Main{

    //クラス実装
     Class class = new Class()
     class.setTeacher("Taro")
     class.setSubTeacher("Hanako")
     class.setStudents(["hoge", "test"])

     //副担任がいるクラス(1-A)の作成
     ClassWithSubTeacher Aclass = new ClassWithSubTeacher()
     School school = Aclass.createClass(class)
     school.setClassName("1-A")

     print(school.ClassName)
     print(school.class.teacher)
     print(school.class.subTeacher)
     print(school.class.students)

    /*
     * 期待値
     * > 1-A
     * > Taro
     * > Hanako
     * > [hoge, test]
     */
}