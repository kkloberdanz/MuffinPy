#!/usr/bin/python3

'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : app.py
License         : GPLv3 (See LICENSE.txt)
'''

import sys
from Database import Database
import datetime
import re

def is_date(date):
    date_regex = re.compile("^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$")
    m = date_regex.search(date)
    if m:
        return True
    else:
        return False

def get_transaction_from_stdin(trans_type): 
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)

    user_input = input("Date (" + day + '/' + month + '/' + year + ")> ")
    print("'" + user_input + "'")

    if is_date(user_input):
        user_input = user_input.split('/')
        year = user_input[0]
        month = user_input[1]
        day = user_input[2]

    else:
        print("Using default")

def launch_cli():
    d = Database()

    user_input = input("Type (expense, income)? > ")

    if user_input == "expense":
        #d.add_expense()
        get_transaction_from_stdin("expense")

        

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        if arg == "--cli": 
            launch_cli()
