'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : Database.py
License         : GPLv3 (See LICENSE.txt)
'''

from Parser import Parser
from Transaction import Transaction
import Currency
import operator

class Database:
    ''' Reads from and stores transactions to an XML file '''

    def __init__(self, balance=0):
        ''' Enter balance as integer, i.e. number of cents '''

        # data_d stores dates as keys, and holds lists of
        # the values from the XML file

        # TODO: make this into a Trie instead of dict
        self.data_d = {}

        self.balance = balance
        self.p = Parser()

    def __repr__(self):
        ret_s = "\n"
        sorted_l = sorted(self.data_d.items(), key=operator.itemgetter(0))
        for key, value in sorted_l:
            ret_s += str(key) + ":\n"
            for item in value:
                ret_s += "\t" + str(item) + '\n'
        ret_s += "Balance: " + self.get_balance_str()
        return ret_s

    def write(self, filename):
        for key, value in self.data_d.items():
            for i in range(len(value)):
                if not value[i].written_to_file:
                    self.p.write(filename, value[i])
                    value[i].written_to_file = True

    def set_all_written(self, set_val): 
        for key, value in self.data_d.items():
            for i in range(len(value)):
                value[i].written_to_file = set_val

    def delete(self, filename, trans_id):
        will_rebuild_file = False
        keys_to_delete = []
        self.set_all_written(False)
        for key, value in self.data_d.items():
            for i in range(len(value)):
                if trans_id == value[i].trans_id:
                    will_rebuild_file = True
                    del value[i]
                    if len(value) <= 0 and key in self.data_d:
                        keys_to_delete.append(key)


        for key in keys_to_delete:
            self.data_d.pop(key) 

        if will_rebuild_file:
            tmp_file = filename + ".tmp"
            self.p.clear_tmp(tmp_file)
            #self.set_all_written(False)
            self.write(tmp_file)
            self.p.rename_file(tmp_file, filename)

        else:
            print("Item:", trans_id, "not found")

    def get_balance_str(self):
        b_str = str(self.balance)
        return '$' + b_str[:-2] + '.' + b_str[-2:]

    def increment_and_get_num_items(self):
        self.p.num_items += 1
        return self.p.num_items

    def read(self, filename):
        # Read in XML file, and put it into datastructure

        for transaction in self.p.parse_xml(filename):
            if transaction.trans_type == "expense":
                self.add_expense(transaction)

            elif transaction.trans_type == "income":
                self.add_income(transaction)

            else:
                print("Transaction type not known")

    def add_transaction(self, transaction):
        key = transaction.year

        if (key not in self.data_d):
            self.data_d[key] = []

        self.data_d[key].append(transaction)
        #self.data_d[key].sort()

    def add_expense(self, expense):
        ''' takes expense of type Transaction '''
        self.balance -= Currency.dollars_to_cents(expense.amount)
        self.add_transaction(expense)

    def add_income(self, income):
        ''' takes income of type Transaction '''
        self.balance += Currency.dollars_to_cents(income.amount)
        self.add_transaction(income)

    def range(self, start, end):
        start_day, start_month, start_year = start.split('/')
        end_day, end_month, end_year = end.split('/') 

        start_trans = Transaction(start_year, start_month, start_day)
        end_trans = Transaction(end_year, end_month, end_day)

        for year in range(int(start_year), int(end_year) + 1):

            if year not in self.data_d:
                continue

            for trans in self.data_d[year]:
                if (start_trans < trans) and (trans < end_trans):
                    yield trans

if __name__ == "__main__":

    d = Database()
    d.read("example.xml")
    print(d.data_d)
    print(d.get_balance_str())
