class Student:
    def __init__(self, name):
        self.name = name

        self.food = 100
        self.money = 100
        self.know = 50

    def info(self):
        print("Ім'я:", self.name)
        print("Їжа:", self.food)
        print("Гроші:", self.money)
        print("Знання:", self.know)


    def study(self):
        print(self.name, "навчається")

        self.know += 20
        self.food -= 50

    def work(self):
        print(self.name, "працює")

        self.money += 20
        self.food -= 50

    def buy(self):
        print(self.name, "закупається")

        self.food += 100
        self.money -=100

    def relax(self):
        print(self.name, "відпочиває")

        self.food -= 15
        self.know -= 20
        self.money -= 20

    def live(self):
        if self.money < 20:
            self.work()

        elif self.know < 60:
            self.study()

        elif self.food < 70:
            self.buy()

        else:
            self.relax()




student = Student("Andrey")


student.live()
student.info()