class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(
            f"Balans kifayət etmir! Mövcud: {balance:.2f}, Tələb olunan: {amount:.2f}"
        )

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = 0
        self.balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not value.isalpha():
            raise ValueError("Owner adı yalnız hərflərdən ibarət olmalıdır.")
        if len(value) < 3:
            raise ValueError("Owner adı minimum 3 simvol olmalıdır.")
        self.__owner = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Balans yalnız int və ya float ola bilər.")
        if value < 0:
            raise ValueError("Balans mənfi ola bilməz.")
        self.__balance = value
        if self.__balance > 10000:
            print("VIP account")

    def deposit(self, amount):
        self.balance += amount
        print(f"Depozit: +{amount:.2f} | Yeni balans: {self.__balance:.2f}")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsError(self.__balance, amount)
        self.__balance -= amount
        print(f"Çəkildi: -{amount:.2f} | Yeni balans: {self.__balance:.2f}")

    def info(self):
        print(f"{self.__owner}, {self.__balance:.2f}")


acc = BankAccount("Sharaf", 500)
acc.info()

acc.deposit(200)
acc.deposit(9500)

try:
    acc.withdraw(50000)
except InsufficientFundsError as e:
    print(e)

acc.withdraw(100)
acc.info()
