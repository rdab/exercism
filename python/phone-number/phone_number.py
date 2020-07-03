import re

pattern = "(1?)([2-9]\d{2})([2-9]\d{2})(\d{4})$"


class PhoneNumber:
    def __init__(self, number):
        number = "".join([n for n in number if n.isdigit()])
        m = re.match(pattern, number)
        if m is None:
            raise ValueError("Invalid number")
        self.country, self.area_code, self.exchange_code, self.subscriber = m.groups()

    def pretty(self):
        return f"({self.area_code}) {self.exchange_code}-{self.subscriber}"

    @property
    def number(self):
        return f"{self.area_code}{self.exchange_code}{self.subscriber}"
