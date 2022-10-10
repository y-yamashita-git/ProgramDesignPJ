from SummonImpl import SummonImpl


# Abstraction
class Summon:
    __impl = SummonImpl()
    
    def __init__(self, impl):
        self.__impl = impl

    # 画面表示
    def display(self):
        return self.__impl.get_scene()
