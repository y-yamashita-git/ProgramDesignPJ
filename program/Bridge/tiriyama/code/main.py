import random
from Genshin import Genshin
from SummonImpl import SummonImpl
from RyuseiImpl import RyuseiImpl

if __name__ == "__main__":
    genshin_summon = Genshin(RyuseiImpl())
    genshin_summon.roll_a_gacha()

    genshin_summon.roll_10_gacha()
