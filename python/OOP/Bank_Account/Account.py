class Account:
    def __init__(self):
        self.__balance = float(0)

    def get_balance(self):
        return float(self.__balance)

    def set_balance(self, value):
        self.__balance = float(value)

    def deposit(self, amt):
        if float(amt) <= 0:
            print("Deposit amount must be more than 0")
            return False

        else:
            self.__balance = self.__balance + float(amt)
            return True

    def withdraw(self, amt):
        if float(amt) < 0:
            print("Withdraw amount must be more than 0")
            return False

        elif float(amt) > self.__balance:
            print("Account balance lower than withdraw amount")
            return False

        else:
            self.__balance = self.__balance - float(amt)
            return True
