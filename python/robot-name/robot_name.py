from string import ascii_uppercase as letters
from itertools import product
from random import shuffle


def names_generator():
    letter_pairs = (''.join(p) for p in product(letters, repeat=2))
    numbers = (str(i).zfill(3) for i in range(1000))
    names = [l + n for l, n in product(letter_pairs, numbers)]
    shuffle(names)
    return names


class RobotController:
    def __init__(self):
        self.name_pool = names_generator()

    def recycle(self, name):
        self.name_pool.insert(0, name)
        shuffle(self.name_pool)

    def register(self, robot):
        try:
            new_name = self.name_pool.pop()
        except IndexError:
            raise Exception('No names available')
        if robot.name is not None:
            self.recycle(robot.name)
        robot.name = new_name


NAME_AUHTORITY = RobotController()

class Robot:
    def __init__(self):
        self.name = None
        self.reset()

    def reset(self):
        NAME_AUHTORITY.register(self)
