class Rectangle:
    width = None
    height = None

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)


rectangle = Rectangle(2, 4)

print(rectangle.area())
print(rectangle.perimeter())


class Car:
    def __init__(self, mark: str, max_speed: int):
        self.mark = mark
        self.max_speed = max_speed
        self.speed = 0

    def display_speed(self):
        return self.speed

    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed = self.speed + 10
        else:
            return self.max_speed
        return self.speed

    def brake(self):
        if self.speed > 0:
            self.speed = self.speed - 10
        else:
            return 0
        return self.speed


car = Car("Audi", 20)
print(car.accelerate())
print(car.accelerate())
print(car.accelerate())
print(car.accelerate())
print(car.brake())
print(car.brake())


class BankAccount:
    def __init__(self, name: str, balance: int):
        self._name = name
        self._balance = balance

    def deposit(self, amount: int):
        self._balance += amount
        return self._balance

    def withdraw(self, amount: int):
        if self._balance > amount:
            self._balance -= amount
            return self._balance
        else:
            print("Not enough money on your account...")
            return self._balance

    def get_balance(self):
        return self._balance


account = BankAccount("Maria", 1000)

print(account.deposit(700))
print(account.withdraw(200))


class OverdraftAccount(BankAccount):
    def __init__(self, name: str, balance: int):
        super().__init__(name, balance)

    def withdraw(self, amount: int):
        super()
        self._balance -= amount
        return self._balance


over_draft = OverdraftAccount("Maria", 1000)
print(over_draft.withdraw(500))
print(over_draft.withdraw(600))
