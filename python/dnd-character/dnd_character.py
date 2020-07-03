import math
import os
import random


def modifier(value):
    return math.floor((value - 10)/2)


def roll_dices():
    random.seed(os.urandom(25))
    return sum(sorted([random.randrange(1,7) for i in range(4)], reverse=True)[0:3])


class Character(object):
    def __init__(self):
        super(Character, self).__init__()
        self.strength = roll_dices()
        self.dexterity = roll_dices()
        self.constitution = roll_dices()
        self.intelligence = roll_dices()
        self.wisdom = roll_dices()
        self.charisma = roll_dices()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        abilites = [
            self.strength,
            self.dexterity,
            self.constitution,
            self.intelligence,
            self.wisdom,
            self.charisma,
        ]
        return random.choice(abilites)
