import random
import re

regexDice = "^(\d*)d(\d+)$"
regexRoll = "^(\d*d\d+)((-|\+)(\d*))?"

class Dice():
    def __init__(self, diceType: int):
        self.diceType = diceType
        self.options = range(1, diceType + 1)

    def roll(self) -> int:
        eyes = random.choice(self.options)
        print(f"d{self.diceType}: {eyes}")
        return eyes


class DiceRoll():
    def __init__(self, dices: list, modifier = 0):
        self.dices = dices
        self.modifier = modifier

    def roll(self) -> int:
        totalDices = 0
        for dice in self.dices:
            totalDices += dice.roll()
        total = totalDices + self.modifier
        print("Total: ", totalDices, " + ", self.modifier, " = ", total)
        return total


def createDiceList(amount: int, diceType: int) -> list:
    return [Dice(diceType)] * amount


def interprateDiceString(string: str) -> list:
    match = re.search(regexDice, string)
    if (match):
        diceType = int(match.group(2))
        if (match.group(1)):
            return createDiceList(int(match.group(1)), diceType)
        return [Dice(diceType)]
        

def interprateRollString(string: str) -> DiceRoll:
    match = re.search(regexRoll, string)
    if (match):
        dices = interprateDiceString(match.group(1))
        if (match.group(2)):
            if (match.group(3) == "-"):
                return DiceRoll(dices, -int(match.group(4)))
            return DiceRoll(dices, int(match.group(4)))
        return DiceRoll(dices)
