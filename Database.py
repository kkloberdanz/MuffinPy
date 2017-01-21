'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : Database.py
License         : GPLv3 (See LICENSE.txt)
'''

import Parser

def dollars_to_cents(amount):
    return int(amount.replace('.', ''))

class Database:
    ''' Reads from and stores transactions to an XML file '''

    def __init__(self, balance=0):
        ''' Enter balance as integer, i.e. number of cents '''

        # data_d stores dates as keys, and holds lists of
        # the values from the XML file
        self.data_d = {}
        self.balance = balance

    def get_balance_str(self):
        b_str = str(self.balance)
        return '$' + b_str[:-2] + '.' + b_str[-2:]

    def read(self, filename):
        # Read in XML file, and put it into datastructure

        for transaction in Parser.parse_xml(filename):
            if transaction.trans_type == "expense":
                self.add_expense(transaction)

            elif transaction.trans_type == "income":
                self.add_income(transaction)

            else:
                print("Transaction type not known")

    def add_transaction(self, transaction):
        key = transaction.date

        if (key not in self.data_d):
            self.data_d[key] = []

        self.data_d[key].append(transaction)

    def add_expense(self, expense):
        ''' takes expense of type Transaction '''
        self.balance -= dollars_to_cents(expense.amount)
        self.add_transaction(expense)

    def add_income(self, income):
        ''' takes income of type Transaction '''
        self.balance += dollars_to_cents(income.amount)
        self.add_transaction(income)

'''
d = Database()
d.read("example.xml")
print(d.data_d)
print(d.get_balance_str())
'''
