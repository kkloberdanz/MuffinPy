'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : Transaction.py
License         : GPLv3 (See LICENSE.txt)
'''

class Transaction:
    def __init__(self, date, trans_type, name, amount):
        self.date       = date
        self.trans_type = trans_type
        self.name       = name
        self.amount     = amount
