from Characters.LivingBeing import LivingBeing
from Characters.OwnStat import CharacterStat

class Player(LivingBeing):
    def __init__(self):
        super().__init__(100, 7)
        self.stats['HUNGER'] = CharacterStat("hunger",100)