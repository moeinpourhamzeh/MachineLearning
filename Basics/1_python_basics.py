
import math


def radius_calc(radius):
    area = math.pi * radius ** 2
    return "The area is {}".format(area)

print(radius_calc(6))

class Frood:
    def __init__(self, age) -> None:
        self.age = age
        print("Frood innitialized")

    def anniversary(self):
        self.age += 1
        print("Frood is now {} years old".format(self.age))

f1 = Frood(12)

f1.anniversary()