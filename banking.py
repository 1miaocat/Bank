class Bank:
    number_of_customers = 0

    def __init__(self, bank_name, customers):
        self.bank_name = bank_name
        self.customers = customers

    def add_customer(self, first_name, last_name, number_of_customers=0):
        self.customers.append(Customer(first_name, last_name))
        number_of_customers += 1

    def get_number_of_customers(self):
        return self.number_of_customers

    def get_customers(self, index):
        return self.customers[index]


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account = Account()

    def get_fname(self):
        return self.first_name

    def get_lname(self):
        return self.last_name

    def get_acc(self):
        return self.account

    def set_acc(self, acc):
        self.account = acc


class Account:

    def __init__(self, balance=None):
        self.balance = balance

    def get_balance(self):
        print(f'Your balance is {self.balance}')

    def deposit(self, amt):
        if amt > 0:
            self.balance = int(amt) + self.balance
            print(f'You balance now: {self.balance}')
            return True
        else:
            print('Your minimum deposit have to be more than 0  ')
            return False

    def withdraw(self, amt):
        if self.balance > int(amt):
            self.balance = self.balance - int(amt)
            print(f'Your balance now: {self.balance}')
            return True
        else:
            print('Insufficient balance  ')
            return False


# ac1 = Account(10000)

# customer1 = Customer('John', 'Bakery')
# customer2 = Customer('kevin', 'cake')
# customer1.set_acc(Account(500))
# Customer('kevin', 'cake').set_acc(Account(1000))
# customer1.get_acc().get_balance()
# Customer('kevin', 'cake').get_acc().get_balance()


def main():
    customers = []
    cba = Bank('CBA', customers)

    def log_in():
        print('Welcome to bank CBA')
        print('Do you have an account? ')
        is_account = input('Y or N\n')

        while is_account != 'Y' and is_account != 'N':
            print('Y or N only. Try again.')
            is_account = input('Y or N\n')
        if is_account == 'Y':
            print('Please insert your username.')
            userF = input('First name: ')
            userL = input('Last name: ')
            user_full = userF + userL
            while user_full not in customers:
                print('No account found. Try again.')
                log_in()

            user_input = input(
                f'welcome {userF} {userL}, select your transaction.\n1. Withdrawal 2. Deposit 3. Balance inquiry\n')

            index = customers.index(user_full)

            if user_input == '1':
                withdraw_amt = input('Enter ammount to withdraw: ')
                cba.get_customers(
                    index + 1).get_acc().withdraw(withdraw_amt)
                log_in()

            elif user_input == '2':
                deposit_amt = input('Enter ammount to deposit: ')
                cba.get_customers(index + 1).get_acc().deposit(deposit_amt)
                log_in()

            elif user_input == '3':
                cba.get_customers(index + 1).get_acc().get_balance()
                log_in()

        elif is_account == 'N':
            print('Make new account.')
            new_nameF = input('Enter your first name: ')
            new_nameL = input('Enter your last name: ')
            first_depo = int(input('Amount to deposit: '))
            new_name = new_nameF + new_nameL
            if new_name in customers:
                print('You already have an account. Account not created.')
                log_in()
            customers.append(new_name)
            cba.add_customer(new_nameF, new_nameL, len(customers))
            cba.get_customers(len(customers) - 1).set_acc(Account(first_depo))
            print(
                f'Congrats, {new_nameF} {new_nameL}. You have successfully created an account.\nYour balance is {first_depo}')

            log_in()
    log_in()


main()
