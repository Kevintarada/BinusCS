from Bank_Account.Account import Account


class Customer:
    def __init__(self, fname, lname):
        self.__fname = str(fname)
        self.__lname = str(lname)
        self.__account = Account()

    def get_first_name(self):
        return str(self.__fname)

    def get_last_name(self):
        return str(self.__lname)

    def get_account(self):
        return self.__account.get_balance()

    def set_account(self, value):
        self.__account.set_balance(value)

    def add_account(self, value):
        self.__account.deposit(float(value))

    def sub_account(self, value):
        self.__account.withdraw(float(value))

    def join_name(self):
        return self.__fname.title() + self.__lname.title()

    def all_info(self):
        return "{} {}, Balance {}".format(self.get_first_name(), self.get_last_name(), self.get_account())
