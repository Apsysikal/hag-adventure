from Characters.LivingBeing import LivingBeing
from Characters.OwnStat import CharacterStat

class Player(LivingBeing):
    def __init__(self):
        super().__init__(100, "2d6")
        self.stats['HUNGER'] = CharacterStat("hunger", 0, 100, 10)
        self.stats['THIRST'] = CharacterStat("thirst", 0, 100, 10)
        self.stats['STAMINA'] = CharacterStat("stamina", 100, turnMod= 20)