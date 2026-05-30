class Item:
    def __init__(self, name, price, rarity):
        self.name = name
        self.price = price
        self.rarity = rarity

    def info(self):
        print("Ім'я:", self.name)
        print("Ціна:", self.price)
        print("Рідкісність:", self.rarity)

    def apply(self):
        print("Предмет використано")


class Weapon(Item):
    def __init__(self, name, price, rarity, damage):

        super().__init__(name, price, rarity)

        self.damage = damage

    def apple(self):
        print("Завдано шкоди", self.damage)


class Potion(Item):
    def __init__(self, name, price, rarity, hp):

        super().__init__(name, price, rarity)

        self.hp = hp

    def apply(self):
        print("Восстановлено здоров'я:", self.hp)

class Armor(Item):
    def __init__(self, name, price, rarity, protection):

        super().__init__(name, price, rarity)

        self.protection = protection

    def apply(self):
        print("Захист +", self.protection)


class Shop:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self):
        for item in self.items:
            print(item.name, item.price, item.rarity)

    def get(self, index):
        return self.items[index]


class Buyer:
    def __init__(self, money):
        self.money = money
        self.inventory = []

    def buy(self, item):
        if self.money >= item.price:
            self.money -= item.price
            self.inventory.append(item)
            print("Куплено:", item.name)
            print("Залишок:", player.money)
        else:
            print("Не вистачає грошей")

    def show_inventory(self):
        print("Інвертар:")
        for item in self.inventory:
            print("*", item.name)



Weapon1 = Weapon("Меч", 100, "Рідкісний", 25)
Potion1 = Potion("Зілля", 50, "Звичайний", 30)
Armor1 = Armor("Броня", 150, "Епічна", 20)

shop = Shop()

shop.add(Weapon1)
shop.add(Potion1)
shop.add(Armor1)


player = Buyer(200)

while True:
    print("Вітаємо у «Арсенал STEPus». Тут ви можете обрати:")
    print("1 - Магазин")
    print("2 - Купити")
    print("3 - Інвертар")
    print("4 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        shop.show()

    elif choice == "2":
        shop.show()
        num = int(input("номер товару: "))
        item = shop.get(num - 1)
        item.apply()

        player.buy(item)

    elif choice == "3":
        player.show_inventory()

    elif choice == "4":
        print("Ви вийшли з магазину")
