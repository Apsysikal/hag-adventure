from Characters.LivingBeing import LivingBeing
import DiceRoll
import json

with open('data/creatures_template.json') as file:
    templatesJson = json.load(file)

def create(name: str):
    return Creature(templatesJson[name])

class Creature(LivingBeing):
    def __init__(self, template):
        super().__init__(DiceRoll.interprateRollString(template['hp']).roll(), template['attack'])
