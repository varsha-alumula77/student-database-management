class Account:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Balance after deposit: {self.__balance}")
        else:
            print("Please deposit an amount greater than 0.")

    def withdraw(self, withdraw_amount):
        if 0 < withdraw_amount <= self.__balance:
            self.__balance -= withdraw_amount
            print(f"Balance after withdrawal: {self.__balance}")
        else:
            print(f"You have only {self.__balance} available.")

    def get_balance(self):
        return self.__balance

    def display_account(self):
        print(f"Account holder name: {self.account_holder}")
        print(f"Account number: {self.account_number}")
        print(f"Your balance: {self.__balance}")


class SavingAccount(Account):
    def __init__(self, account_holder, account_number, balance, interest_rate):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        balance = self.get_balance()
        print(f"Your current balance: {balance}")

        interest = (balance * self.interest_rate) / 100
        self.deposit(interest)

        print(f"Interest added: {interest}")


name = input("Enter the account holder name: ")
acc_number = input("Enter the account number: ")

acc = SavingAccount(name, acc_number, 10000, 5)
acc.add_interest()