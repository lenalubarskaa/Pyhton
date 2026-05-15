class Player:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

        self.hp = 100
        self.inventory = []


    def info(self, name, weapon, hp):
        print("Ім'я:", self.name)
        print("Здоров'я:", self.hp)
        print("Зброя:", self.weapon)

    def attack(self, enemy):
        print(self.name, "атакує", enemy.name)

        enemy.hp -= self.weapon.damage

        print(enemy.name, "откримав шкоду")
        print("HP ворога:", enemy.hp)



class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def info(self):
        print("Ворог", self.name)
        print("HP:", self.hp)


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def info(self):
        print("Зброя", self.name)
        print("Шкода", self.damage)



player = Player("Player")
enemy = Enemy("Enemy", 100)

sword1 = Weapon("Iron Sword", 25)
sword2 = Weapon("Axe", 15)
sword3 = Weapon("Magic Staff", 35)

player.info()