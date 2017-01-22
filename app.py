#!/usr/bin/python3

'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : app.py
License         : GPLv3 (See LICENSE.txt)
'''

import sys
from Database import Database
from Transaction import Transaction
from Parser import Parser
import datetime
import re
import Currency

class Interface:

    def __init__(self):
        self.d = Database()
        self.date_regex = re.compile("^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$")
        self.filename = ""

    def is_date(self, date):
        m = self.date_regex.search(date)
        if m:
            return True
        else:
            return False

    def read(self, filename):
        self.filename = filename
        self.d.read(filename)

    def get_transaction_from_stdin(self, trans_type): 
        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month)
        day = str(now.day)

        user_input = input("Date (" + day + '/' + month + '/' + year + ")> ")

        if self.is_date(user_input):
            year, month, day = user_input.split('/')

            year = user_input[0]
            month = user_input[1]
            day = user_input[2]

        else:
            print("Using default date")

        name = ""
        while not name:
            name = input("Name of transaction? > ")

        amount = ""
        while not amount:
            amount = input("Amount? > ")

        currency = input("Currency (USD) > ")

        if not currency:
            currency = "USD"

        if trans_type == "expense":
            self.d.add_expense(Transaction(year, month, day, trans_type, name, amount, currency, self.d.increment_and_get_num_items()))

        elif trans_type == "income":
            self.d.add_income(Transaction(year, month, day, trans_type, name, amount, currency, self.d.increment_and_get_num_items()))

        else:
            print("Not a valid transaction type")

        self.d.write(self.filename)

    def launch_cli(self):

        user_input = 'a'
        while user_input != 'q':
            print("Current items in DB: ", self.d)
            user_input = input("Type (expense, income)? > ") 

            if user_input == "expense":
                self.get_transaction_from_stdin("expense")

            elif user_input == "income":
                self.get_transaction_from_stdin("income")

            elif user_input == "q":
                quit()

            elif user_input == "":
                pass

            else:
                print(user_input, "Not a valid input")



if __name__ == "__main__":
    filename = sys.argv[1]
    interface = Interface()
    interface.read(filename)
    for arg in sys.argv[2:]:
        if arg == "--cli": 
            interface.launch_cli()
