class Character:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def info(self):
        print("Ім'я:", self.name)
        print("Рівень:", self.level)
        print("HP:", self.hp)

    def attack(self, enemy):
        damage = 10
        enemy.hp -= damage

        print(self.name, "атакує", enemy.name)
        print("Шкода:", damage)
        print("HP ворога:", enemy.hp)


class Warrior(Character):
    def attack(self, enemy):
        damage = 20 + self.level
        enemy.hp -= damage

        print(self.name, "б'є мечем")
        print("Шкода:", damage)
        print("HP ворога:", enemy.hp)


class Mage(Character):
    def attack(self, enemy):
        damage = 15 + self.level
        enemy.hp -= damage

        print(self.name, "атакує магією")
        print("Шкода:", damage)
        print("HP ворога:", enemy.hp)


class Archer(Character):
    def attack(self, enemy):
        damage = 18 + self.level
        enemy.hp -= damage

        print(self.name, "стріляє з лука")
        print("Шкода:", damage)
        print("HP ворога:", enemy.hp)


class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, hero):
        damage = 10
        hero.hp -= damage

        print(self.name, "атакує героя")
        print("Шкода:", damage)
        print("HP героя:", hero.hp)


warrior = Warrior("Thor", 3, 120)
mage = Mage("Merlin", 4, 80)
archer = Archer("Robin", 2, 90)

enemy = Enemy("Orc", 150)

heroes = [warrior, mage, archer]


print("БІЙ ПОЧАВСЯ")

while enemy.hp > 0:

    for hero in heroes:

        if enemy.hp <= 0:
            break

        hero.attack(enemy)

        if enemy.hp <= 0:
            print(enemy.name, "переможений!")
            break

        enemy.attack(hero)

        if hero.hp <= 0:
            print(hero.name, "програв!")