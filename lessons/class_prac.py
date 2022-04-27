"""Practice with writing classes for final exam."""


class HotCocoa:

    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, whip: bool, flav: str, count: int, sweet: int):
        self.has_whip = whip
        self.flavor = flav
        self.marshmallow_count = count
        self.sweetness = sweet

    def mallow_adder(self, mallows: int):
        self.marshmallow_count += mallows
        self.sweetness = self.sweetness + (mallows * 2)
    
    def calorie_count(self) -> float:
        cals: float = 0

        if (self.flavor == "vanilla" or self.flavor == "peppermint"):
            cals += 30
        else:
            cals += 20
        if self.has_whip:
            cals += 100
        if self.marshmallow_count > 0:
            cals += self.marshmallow_count / 2
        return cals
    

class TimeSpent:

    name: str
    purpose: str
    minutes: int

    def __init__(self, n: str, p: str, m: int):
        self.name = n
        self.purpose = p
        self.minutes = m

    def add_time(self, time: int) -> None:
        self.minutes += time

    def reset(self) -> int:
        store: int = self.minutes
        self.minutes = 0
        return store

    def report(self):
        mins: int = self.minutes % 60
        hours: int = self.minutes // 60
        print(f"{self.name} has spent {hours} hours and {mins} minutes on {self.purpose}")  


def factorial(fact: int) -> int:
    sum: int = 0
    if sum < 2:
        return 1
    else:
        return sum * factorial(fact - 1)