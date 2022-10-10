import random
from Summon import Summon

class Genshin(Summon):
    __card_list = {"★5": ["ディルック","七七"], "★4":["ベネット","行秋","トーマ","ドリー","★4武器"], "★3":["★3武器"]}
    __card_rarity_list = [{"rarity" : "★5", "prob" : 0.6}, {"rarity" : "★4" , "prob" : 2.55}, {"rarity" : "★3" , "prob" : 94.3}]

    def __init__(self, impl):
        super().__init__(impl)

    # 単発
    def roll_a_gacha(self):
        rand = random.random() * 100
        print(self.display())
        for i in range(len(self.__card_rarity_list)):
            if rand <= self.__card_rarity_list[i]["prob"]:
                print(random.choice(self.__card_list[self.__card_rarity_list[i]["rarity"]]))
                break

    # 10連
    def roll_10_gacha(self):
        print(self.display())
        for count in range(10):
            rand = random.random() * 100
            if count == 9 :
                print(random.choice(self.__card_list["★4"]))
                continue
            for i in range(len(self.__card_rarity_list)):
                    if rand <= self.__card_rarity_list[i]["prob"]:
                        print(random.choice(self.__card_list[self.__card_rarity_list[i]["rarity"]]))
                        continue
