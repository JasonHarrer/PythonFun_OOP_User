#!/usr/bin/env python

from random import randint

class BankAccount:
    def __init__(self, starting_balance=0.00,
                       starting_interest_rate=0.025,
                       id=''):
        self.balance       = starting_balance
        self.interest_rate = starting_interest_rate


    def set_account_number(self, number):
        if number != '':
            self.number = number
        else:
            print(f'Error: set_account_number called without a number')


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f'Account #{self.number}\tBalance: ${self.balance:.2f}')
        if self.balance < 0:
            print('\t*** THIS ACCOUNT IS OVERDRAFTED ***')
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.interest_rate)
        return self


class User:
    def __init__(self, username, email_address):
        self.name            = username
        self.email           = email_address
        self.account         = {}

    def add_account(self, account=''):
        new_account = BankAccount()
        if account in self.account:
            print(f'Error: Account {account} already exists.')
            print()
            return

        new_account_number = account
        while new_account_number == '' or new_account_number in self.account:
            new_account_number = randint(100000000, 999999999)
        new_account.set_account_number(new_account_number)
        self.account[new_account_number] = new_account
        return new_account_number

    def remove_account(self, account):
        if account in self.account:
            self.account.remove(account)
        else:
            print(f'Account {account} does not exist')
            print()
        return

    def make_deposit(self, account, amount):
        if account in self.account:
            self.account[account].deposit(amount)
            return self
        else:
            print(f'Account {account} does not exist')
            print()

    def make_withdrawal(self, account, amount):
        if account in self.account:
            self.account[account].withdraw(amount)
            return self
        else:
            print(f'Account {account} does not exist')
            print()

    def display_user_balance(self):
        print(f'User: {self.name}:')
        for account in self.account.values():
            account.display_account_info()
        print()
        return self

    def display_user_account_balance(self, account):
        if account in self.account:
            self.account[account].display_account_info()
            return self
        else:
            print(f'Account {account} does not exist')
            print()
            


    def transfer_money(self, source_account, other_user, destination_account, amount):
       self.account[source_account].withdraw(amount)
       other_user.account[destination_account].deposit(amount)
       return self



# Test section
jeremy = User("Jeremy Fakename", "jeremy@fakename.com")
alice  = User("Alice I'dunno",   "alice@somecompany.com")
mickey = User("Mickey Mickey",   "youre@sofine.org")

#Test 1: Have the first user make 3 deposits and 1 withdrawal in the first account and then display their balance
jeremy_account  = jeremy.add_account()
jeremy.make_deposit(jeremy_account, 200).make_deposit(jeremy_account, 300).make_deposit(jeremy_account, 500).make_withdrawal(jeremy_account, 800).display_user_balance()

#Test 2: Have the first user open a second account and add some money, withdraw some money, then display their balance again.
#         display_user_balance should show both accounts.
jeremy_account2 = jeremy.add_account()
jeremy.make_deposit(jeremy_account2, 300).make_deposit(jeremy_account2, 700).make_withdrawal(jeremy_account2, 400).display_user_balance()

#Test 2: Have the second user make 2 deposits and 2 withdrawals and then display their balance
alice_account = alice.add_account('12345')
alice.make_deposit(alice_account, 500).make_deposit(alice_account, 400).make_withdrawal(alice_account, 650).make_withdrawal(alice_account, 100).display_user_balance()

#Test 3: Have the second user create a second account with the same account number.  It should fail.
alice_account2 = alice.add_account('12345')


#Test 3: Have the third user make 1 deposit and 3 withdrawals and then display their alance
mickey_account = mickey.add_account()
mickey.make_deposit(mickey_account, 500).make_withdrawal(mickey_account, 200).make_withdrawal(mickey_account, 100).make_withdrawal(mickey_account, 300).display_user_balance()


#Test 4: Have the first user transfer money to the third user and then print both users' balances'
jeremy.transfer_money(jeremy_account, mickey, mickey_account, 105).display_user_balance()
mickey.display_user_balance()
