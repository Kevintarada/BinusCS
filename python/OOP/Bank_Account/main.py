from Bank_Account.Bank import Bank


def main():
    the_bank = Bank(input("Input bank name: "))
    print("")
    print("Welcome to {} Bank".format(the_bank.get_bank_name()))
    what_next(the_bank)


def what_next(the_bank):
    choices = input("Options:\n1. List of existing account(s)\n2. Add new account\n3. Choose existing account\n4. Change bank name\n5. End bank simulator\nChoice: ")
    if choices == "1":
        print("")
        print_customer_list(the_bank)

    elif choices == "2":
        print("")
        add_customer(the_bank)

    elif choices == "3":
        if the_bank.get_number_of_customers() == 0:
            print("No customer listed")
            what_next(the_bank)
        else:
            print("")
            print("Account(s):")
            for i in range(the_bank.get_number_of_customers()):
                print("{}. {}".format(i+1, the_bank.get_customer(i)))
            account_number = int(input("Your account: "))-1
            print("")
            print(the_bank.get_full_info(account_number)+"\n")
            second_choice(the_bank, account_number)

    elif choices == "4":
        print("")
        new_bank_name = input("Input new bank name: ")
        the_bank.set_bank_name(new_bank_name)
        print("")
        print("Welcome to {} Bank".format(the_bank.get_bank_name()))
        what_next(the_bank)

    elif choices == "5":
        print(the_bank.get_bank_name())

        for i in range(the_bank.get_number_of_customers()):
            print("{}. {}".format(i+1, the_bank.get_full_info(i)))
        print("Thanks for using bank simulator :)")

    else:
        print("Choose number from options!")
        what_next(the_bank)


def print_customer_list(the_bank):
    print("Customers:")
    if the_bank.get_number_of_customers() == 0:
        print("None")

    else:
        for i in range(the_bank.get_number_of_customers()):
            print("{}. {}".format(i+1, the_bank.get_customer(i)))

    print("Number of customer(s): {}{}".format(str(the_bank.get_number_of_customers()), "\n"))
    what_next(the_bank)


def add_customer(the_bank):
    first_name = input("First name: ").title()
    last_name = input("Last name: ").title()
    initial_balance = input_initial_balance()
    print("")
    the_bank.add_customer(first_name, last_name)
    the_bank.set_initial_balance(-1, initial_balance)
    what_next(the_bank)


def second_choice(the_bank, account_number):
    choice = input("Options:\n1. See balance\n2. Deposit\n3. Withdraw\n4. Back\nChoice: ")

    if choice == "1":
        print("")
        print(the_bank.get_initial_balance(account_number))
        second_choice(the_bank, account_number)

    elif choice == "2":
        print("")
        deposit(the_bank, account_number)

    elif choice == "3":
        print("")
        withdraw(the_bank, account_number)

    elif choice == "4":
        print("")
        what_next(the_bank)

    else:
        print("")
        print("Choose from the options!")
        second_choice(the_bank, account_number)


def deposit(the_bank, account_number):
    value = input("Deposit value: ")

    try:
        the_bank.add_balance(account_number, value)
        second_choice(the_bank, account_number)

    except:
        print("Deposit value must be a number/float!")
        deposit(the_bank, account_number)


def withdraw(the_bank, account_number):
    value = input("Deposit value: ")
    try:
        the_bank.sub_balance(account_number, value)
        second_choice(the_bank, account_number)

    except:
        print("Withdraw value must be a number/float!")
        withdraw(the_bank, account_number)


def input_initial_balance():
    initial_balance = input("Initial balance: ")

    try:
        initial_balance = float(initial_balance)
        return initial_balance

    except:
        print("")
        print("Initial balance must be a number!")
        input_initial_balance()

print("The bank simulator...\n")
main()
