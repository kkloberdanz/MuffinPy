'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : Transaction.py
License         : GPLv3 (See LICENSE.txt)
'''

class Transaction:
    def __init__(self, year, month, day, trans_type="expense", name="default", amount=0, currency="USD", trans_id=-1, written_to_file=False):
        self.year       = int(year)
        self.month      = int(month)
        self.day        = int(day)

        self.trans_type = trans_type
        self.name       = name
        self.amount     = amount
        self.currency   = currency
        self.trans_id   = trans_id

        self.written_to_file = written_to_file

    def __repr__(self):
        return "date (dd/mm/yyyy): " + str(self.day) + "/" + str(self.month) + "/" + str(self.year) +\
               "\n\ttype: " + str(self.trans_type) + \
               "\n\tname: " + str(self.name) + \
               "\n\tamount: " + str(self.amount)+\
               "\n\tcurrency: " + str(self.currency)+\
               "\n\tid: " + str(self.trans_id)+ "\n"

    def __lt__(self, other):
        if self.year != other.year:
            return int(self.year) < int(other.year)

        elif self.month != other.month:
            return int(self.month) < int(other.month)

        else:
            return int(self.day) < int(other.day)
