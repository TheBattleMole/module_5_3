class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors:
            print("Такого этажа не существует")
        else:
            for i in range(1,new_floor + 1):
                print(i)

    def __len__(self):
        return self.floors

    def __str__(self):
        return f" Название: {self.name}, количество этажей: {self.floors}"

    def __eq__(self, other):
        return self.floors == other.floors

    def __lt__(self, other):
        return self.floors < other.floors

    def __le__(self, other):
        return self.floors <= other.floors

    def __gt__(self, other):
        return self.floors > other.floors

    def __ge__(self, other):
        return self.floors >= other.floors

    def __ne__(self, other):
        return self.floors != other.floors

    def __add__(self, value):
        self.floors = self.floors + value
        return self

    def __iadd__(self, value):
        self.floors += value
        return self

    def __radd__(self, value):
        self.floors = value + self.floors
        return self


h1 = House("Бурдж-Халифа", 163)
h2 = House("Хрущевка", 5)

print(h1)
print(h2)
print(h1 == h2) # __eq__
h2 = h2 + 158 # __add__
h2.name = "Великая хрущевка"
print(h2)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__