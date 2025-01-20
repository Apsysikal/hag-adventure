from Characters.OwnStat import CharacterStat

class LivingBeing():
    def __init__(self, hp: int, attackValue: int):
        self.stats: dict[str: 'CharacterStat'] = {}
        self.stats['HP'] = CharacterStat("hp", hp)
        self.attackValue = attackValue

    def attack(self, target: 'LivingBeing'):
        target.hp.change(self.attackValue)