
import random
from die_rolls import *

class Page:

    def __init__(self, text, combat):
        self.text = text
        self.combat = combat

class Adventurer:

    def __init__(self, name, skill,stamina, luck, gold, jewels,potions,equipment):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.luck = luck
        self.gold = gold
        self.jewels = jewels
        self.potions = potions
        self.equipment = equipment

class Enemy:

    def __init__(self, name, skill, stamina):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        
def character_creation():
    player_name = input("What is your name Adventurer? ")
    skill = roll6() + 6
    stamina = roll6() + roll6() + 12
    luck = roll6() + 6
    print(f"Your SKILL is: {skill}")
    print(f"Your Stamina is: {stamina}")
    print(f"Your LUCK is: {luck}")
    return player_name, skill, stamina, luck



pg1 = Page("Text here", "Troglodyte")
print(pg1.text)
player_name = None
skill = None
stamina = None
luck = None
character_creation()
adventurer = Adventurer(player_name, skill,stamina, luck,"","","","")
print(adventurer.name,skill)

