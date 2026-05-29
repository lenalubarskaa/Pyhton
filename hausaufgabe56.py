class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def info(self):
        print("Предмет:", self.name)
        print("Цінність:", self.value)


class Player:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

        self.hp = 100
        self.inventory = []

    def info(self):
        print("Ім'я:", self.name)
        print("Здоров'я:", self.hp)
        print("Зброя:", self.weapon.name)

    def attack(self, enemy):
        print(self.name, "атакує", enemy.name)

        enemy.hp -= self.weapon.damage

        print(enemy.name, "откримав шкоду")
        print("HP ворога:", enemy.hp)

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("Інвентар:")
        for item in self.inventory:
            print("-", item.name)


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def info(self):
        print("Ворог", self.name)
        print("HP:", self.hp)

    def attack(self, player):
        print(self.name, "атакує", player.name)

        player.hp -= self.damage

        print(player.name, "отримав шкоду")
        print("HP гравця:", player.hp)


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def info(self):
        print("Зброя", self.name)
        print("Шкода", self.damage)







sword1 = Weapon("Iron Sword", 25)
sword2 = Weapon("Axe", 15)
sword3 = Weapon("Magic Staff", 35)


print("Оберіть зброю:")
print("1 - Iron Sword")
print("2 - Axe")
print("3 - Magic Staff")

choice = input("Ваш вибір: ")

if choice == "1":
    weapon = sword1
elif choice == "2":
    weapon = sword2
else:
    weapon = sword3

potion = Item("Health Potion", 50)
gold = Item("Gold Coin", 100)

player = Player("Player", weapon)
enemy = Enemy("Enemy", 100, 20)

player.add_item(potion)
player.add_item(gold)

player.info()
enemy.info()

print("БІЙ ПОЧАВСЯ")

while player.hp > 0 and enemy.hp > 0:

    player.attack(enemy)

    if enemy.hp <= 0:
        print(enemy.name, "переможений!")
        break

    enemy.attack(player)

    if player.hp <= 0:
        print(player.name, "програв!")
        break


