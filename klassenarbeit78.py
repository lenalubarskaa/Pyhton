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

class Cat(Animal):

    def __init__(self, name, age, flexibility):

        super().__init__(name, age)

        self.flexibility = flexibility

    def scratch(self):
        print(self.name, "царапає")

    def sound(self):
        print("Кішка нявкає")

    def info(self):
        super().info()

        print("Гибкість", self.flexibility)

animal2 = Cat("Гайка", 1, 10)


animal2.scratch()
animal2.sound()
animal2.info()

print("Гибкость:", animal2.flexibility)

class Bird(Animal):
    def __init__(self, name, age, volatility):
        super().__init__(name, age)

        self.volatility = volatility

    def fly(self):
        print(self.name, "летает")

    def sound(self):
        print("Пташка цвірінькає")

    def info(self):

        super().info()

        print("Цвирінькає", self.volatility)

animal3 = Bird("Воробей", 1, 20)


animal3.fly()
animal3.sound()
animal3.info()

print("Летучесть:", animal3.volatility)



