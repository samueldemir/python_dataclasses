class Food:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def __str__(self):
        return f"{self.price} blub"

    def __repr__(self):
        return "debugging"


salad = Food("large", 20)
print(repr(salad))