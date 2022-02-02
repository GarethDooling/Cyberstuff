
from unittest import result


class Food:
    def __init__(self, item, cost, date):
        self.item = item
        self.cost = cost
        self.date = date 

    def __repr__(self):
        return = result

food1 = Food("bread", "1.99", "1 Feb")
food2 = Food("fish", "12.99", "31 Jan")

print(food1, food2)
