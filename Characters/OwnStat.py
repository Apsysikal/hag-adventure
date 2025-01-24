from turnLogic.TurnAction import TurnAction

class OwnStat(TurnAction):
    def __init__(self, name: str, value: int, turnMod = 0):
        self.name = name
        self.value = value
        self.turnMod = turnMod

    def change(self, mod: int) -> int:
        print(mod)
        self.value = self.value + mod
        if (self.value > self.maxValue):
            self.value = self.maxValue
        if (self.value < 0):
            self.value = 0
        return self.value

    def turnAction():
        print(f"{self.name}: {self.value} -> {self.change(self.turnMod)}")
        #self.change(self.turnMod)

class CharacterStat(OwnStat):
    def __init__(self, name: str, value: int, maxValue = 0, turnMod = 0):
        self.maxValue = maxValue if maxValue else value
        super().__init__(name, value, turnMod)

