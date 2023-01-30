
def is_triangle(sides):
    sides = sorted(sides)
    return sum(sides[:2]) > sides[2]

def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
   return is_triangle(sides) and len(set(sides)) == 3
