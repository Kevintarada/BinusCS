from Bank_Account.Customer import Customer


class Bank:
    def __init__(self, bank_name):
        self.__customer = []
        self.__numberOfCustomers = 0
        self.__bankName = str(bank_name)

    def set_bank_name(self, new_name):
        self.__bankName = new_name

    def get_bank_name(self):
        return self.__bankName

    def add_customer(self, fname, lname):
        if self.__numberOfCustomers == 0:
            self.__customer.append(Customer(fname, lname))
            self.__numberOfCustomers += 1

        else:
            automagic_number = 0
            for i in range(self.__numberOfCustomers):
                name_check = fname.title() + lname.title()

                if self.__customer[i].join_name() == name_check:
                    automagic_number += 1

                else:
                    continue
            if automagic_number > 0:
                print("Account existed..\n")

            else:
                self.__customer. append(Customer(fname, lname))
                self.__numberOfCustomers += 1

    def get_number_of_customers(self):
        return self.__numberOfCustomers

    def get_customer(self, num):
        return "{} {}".format(self.__customer[int(num)].get_first_name(), self.__customer[int(num)].get_last_name())

    def set_initial_balance(self, num, value):
        self.__customer[int(num)].set_account(float(value))

    def get_initial_balance(self, num):
        return self.__customer[int(num)].get_account()

    def add_balance(self, num, value):
        self.__customer[int(num)].add_account(value)

    def sub_balance(self, num, value):
        self.__customer[int(num)].sub_account(value)

    def get_full_info(self, num):
        return "Name: {} {}, Balance: {}".format(self.__customer[int(num)].get_first_name(), self.__customer[int(num)].get_last_name(), str(self.__customer[int(num)].get_account()))
