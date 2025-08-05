class BankAccount:

    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError(" cannot be negative.")
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("error negative value")
        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit negative")
        self._balance += amount
        print(f"Deposited: {amount}, New Balance: {self._balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw negative")
        if amount > self._balance:
            raise ValueError("fonduri insuficiente")
        self._balance -= amount
        print(f"Withdrew: {amount}, New Balance: {self._balance}")



if __name__ == "__main__":
    try:
        account = BankAccount(100)  
        print("Initial balance:", account.balance)

        account.deposit(50)
        account.withdraw(30)

        # Test invalid deposit
        try:
            account.deposit(-10)
        except ValueError as e:
            print("Error:", e)

        # Test invalid withdrawal
        try:
            account.withdraw(1000)
        except ValueError as e:
            print("Error:", e)

        # Test invalid balance set
        try:
            account.balance = -500
        except ValueError as e:
            print("Error:", e)

    except Exception as e:
        print("failed to create account:", e)
