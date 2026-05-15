class Character:
    def __init__(self, name, level, weapon, armor):
        self.name = name
        self.level = level
        self.weapon = weapon
        self.armor = armor

        self.health = 100

    def info(self):
        print("Ім'я:", self.name)
        print("Рівень:", self.level)
        print("Зброя:", self.weapon.name)
        print("Броня:", self.armor.name)

    def show_weapon(self):
        print(self.name, "використовує", self.weapon.name)

    def attack(self, enemy):
        print(self.name, "атакує", enemy.name)

        enemy.health -= self.weapon.damage

        print(enemy.name, "откримав шкоду")
        print("HP ворога:", enemy.health)

    def attack2(self, enemy2):
        print(self.name, "атакує", enemy2.name)

        enemy2.health -= self.weapon.damage

        print(enemy2.name, "откримав шкоду")
        print("HP ворога:", enemy2.health)


class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def info(self):
        print("Зброя", self.name)
        print("Шкода", self.damage)


class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def info(self):
        print("Ворог", self.name)
        print("HP:", self.health)


sword1 = Weapon("Iron Sword", 25)
sword2 = Weapon("Axe", 15)
sword3 = Weapon("Magic Staff", 35)





sword = Weapon("Dragon Sword", 35)

enemy = Enemy("Skeleton", 120)
enemy2 = Enemy("Creeper", 200)




armor1 = Armor("Iron Armor", 15)
armor2 = Armor("Gold Armor", 25)
armor3 = Armor("Diamond Armor", 35)

weapon1 = Weapon("Steel Sword", 30)

player = Character("Warrior", 8, weapon1, armor1)
player1 = Character("Knight", 18, sword3, armor2)
player2 = Character("Gogog", 20, sword2, armor3)

player.info()
player1.info()
player2.info()

player1.attack(enemy)
player1.attack2(enemy2)

