class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

person_one = Person(name="Samuel")
print(person_one)

