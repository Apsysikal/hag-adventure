from turnLogic.TurnAction import TurnAction

class OwnStat(TurnAction):
    def __init__(self, name: str, value: int, turnMod = 0):
        self.name = name
        self.value = value
        self.turnMod = turnMod

    def change(self, mod: int) -> int:
        self.value += mod
        return self.value

    def turnAction():
        print(f"{self.name}: {self.value} -> {self.change(self.turnMod)}")
        #self.change(self.turnMod)

class CharacterStat(OwnStat):
    def __init__(self, name: str, value: int, maxValue = 0, turnMod = 0):
        self.maxValue = maxValue if maxValue else value
        super().__init__(name, value, turnMod)

