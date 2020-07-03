from datetime import timedelta
from decimal import Decimal, ROUND_HALF_UP

VENUS = 0.61519726
URANUS = 84.016846
SATURN = 29.447498
MERCURY = 0.2408467
NEPTUNE = 164.79132
MARS = 1.8808158
JUPITER = 11.862615

class SpaceAge:
    def __init__(self, seconds):
        self.earth = Decimal(seconds/31557600)

    def on_earth(self):
        return self._fmt(self.earth)

    def on_venus(self):
        return self._fmt(self._compare(VENUS))

    def on_uranus(self):
        return self._fmt(self._compare(URANUS))

    def on_saturn(self):
        return self._fmt(self._compare(SATURN))

    def on_mercury(self):
        return self._fmt(self._compare(MERCURY))

    def on_neptune(self):
        return self._fmt(self._compare(NEPTUNE))

    def on_mars(self):
        return self._fmt(self._compare(MARS))

    def on_jupiter(self):
        return self._fmt(self._compare(JUPITER))

    def _compare(self, planet):
        return self.earth / Decimal(planet)

    def _fmt(self, value):
        return float(value.quantize(Decimal('.01')))
