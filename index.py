from selection import Selection
from Characters.Player import Player
import Characters.Creature as Creature


print("Welcome to the Hansle and Gretle Adventure!")
selector = Selection(["load", "New Game"],"Do you want to load a game or start a new one?")
selectetOption = selector.serve()

print(selectetOption)

mc = Player()

print(mc.stats['HUNGER'].value)

bear = Creature.create("Bear")

print(f"{bear.stats['HP'].value}/{bear.stats['HP'].maxValue}")

mc.attack(bear)

print(f"{bear.stats['HP'].value}/{bear.stats['HP'].maxValue}")
