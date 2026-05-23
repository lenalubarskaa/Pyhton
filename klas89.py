from importlib.util import source_hash
from multiprocessing.connection import answer_challenge

"""
class Animal:

    def __init__(self, name, age):

        self.name = name
        self.age = age


        self.health = 100


    def info(self):

        print("Ім'я:", self.name)
        print("Вік:", self.age)
        print("HP:", self.health)

    def sound(self):
        print("Тварина видає звук")


class WildAnimal(Animal):

    def __init__(self, name, age, danger):

        super().__init__(name, age)

        self.danger = danger

    def attack(self):

        print("Тварина атакує")


class Predator(WildAnimal):

    def __init__(self, name, age, danger):

        super().__init__(name, age, danger)

        self.food = []


class Lion(Predator):

    def __init__(self, name, age, danger, bite):

        super().__init__(name, age, danger)

        self.bite = bite


    def sound(self):
        print("Тварина ричить")


class Tiger(Predator):

    def __init__(self, name, age, danger, sound):

        super().__init__(name, age, danger)

        self.sound = sound

    def sound(self):
        print("Тварина ричить")


class Wolf(Predator):

    def __init__(self, name, age, danger, sound):

        super().__init__(name, age, danger)

        self.sound = sound

    def sound(self):
        print("Тварина ричить")




class Herbivorous(WildAnimal):

    def __init__(self, name, age, danger):

        super().__init__(name, age, danger)

        self.food = []


class Wildebeest(Herbivorous):

    def __init__(self, name, age, danger, speed):

        super().__init__(name, age, danger)

        self.speed = speed

    def sound(self):

        print("Тварина видає звук")


class Hare(Herbivorous):

    def __init__(self, name, age, danger, jump):

        super().__init__(name, age, danger)

        self.jump = jump

    def sound(self):

        print("Тварина видає звук")


class Deer(Herbivorous):

    def __init__(self, name, age, danger, jump):

        super().__init__(name, age, danger)

        self.jump = jump

    def sound(self):
        print("Тварина видає звук")


animal1 = Lion("Лев", 5, 50, 30)

animal2 = Tiger("Тигр", 4, 60, 25)

animal3 = Wolf("Волк", 4, 30, 40)

animal4 = Wildebeest("Антилопа", 3, 25, 25)

animal5 = Hare("Заяц", 2, 15, 35)

animal6 = Deer("Олень", 3, 25, 35)

animal1.info()
animal2.info()
animal3.info()
animal4.info()
animal5.info()
animal6.info()
"""

"""
try:
    x = int(input("Введи число:  "))
    print(10 / x)
except ZeroDivisionError:
    print("НЕ можна ділити на 0")
except ValueError:
    print("Треба виводити число")
else:
    print("Все добре, число:", x)
finally:
    print("Дякую")

"""


class BankAccount:

    def __init__(self, money):
        self.money = money


    def withdraw(self, amount):

        if amount < 0:
            raise ValueError("Не можна знімати мінус")

        if amount > self.money:
            raise ValueError("Недостатньо грошей")

        if amount == 0:
            raise ValueError("Помилка!")

        if amount > self.money:
            need = amount - self.money
            answer = input("Недостатньо коштів. Взяти кредит на", need, "грн? (так/ні)")



        self.money -= amount

        print("Знято:", amount)
        print("Залишок:", self.money)

    def add_money(self, amount):

        if amount < 0:
            raise ValueError("Помилка!")


account = BankAccount(100)

try:
    take = int(input("Скільки зняти? "))
    account.withdraw(take)

except ValueError as e:
    print("Помилка:", e)