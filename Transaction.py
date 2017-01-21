'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : Transaction.py
License         : GPLv3 (See LICENSE.txt)
'''

class Transaction:
    def __init__(self, date, trans_type, name, amount, currency, trans_id):
        self.year       = year
        self.month      = month
        self.day        = day

        self.trans_type = trans_type
        self.name       = name
        self.amount     = amount
        self.currency   = currency
        self.trans_id   = trans_id

    def __repr__(self):
        return "(year: " + str(self.year) +\
               ", month: " + str(self.month) + \
               ", day: " + str(self.day) + \
               ", type: " + str(self.trans_type) + \
               ", name: " + str(self.name) + \
               ", amount: " + str(self.amount)+\
               ", currency: " + str(self.currency)+\
               ", id: " + str(self.trans_id)+\
               ")"

