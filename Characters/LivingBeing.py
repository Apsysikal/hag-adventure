from Characters.OwnStat import CharacterStat
import DiceRoll

class LivingBeing():
    def __init__(self, hp: int, attackStr: str):
        self.stats: dict[str: 'CharacterStat'] = {}
        self.stats['HP'] = CharacterStat("hp", hp)
        self.attackDice = DiceRoll.interprateRollString(attackStr)

    def attack(self, target: 'LivingBeing'):
        target.stats['HP'].change(-self.attackDice.roll())