'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : Parser.py
License         : GPLv3 (See LICENSE.txt)
'''

from xml.dom import minidom
from Transaction import Transaction
import os

class Parser:

    def __init__(self):
        self.num_items = 0

    def correct_xml(self, filename):
        input_file = open(filename, "r")
        output_file = open(filename + ".tmp", "w")
        output_file.write('<?xml version="1.0" encoding="utf-8"?>\n')
        output_file.write("<transactions>\n")

        for line in input_file:
            output_file.write("\t" + line)

        output_file.write("</transactions>")
        output_file.close()

    def parse_xml(self, filename):
        self.correct_xml(filename)
        doc = minidom.parse(filename + ".tmp")
        transactions = doc.getElementsByTagName("transaction")

        for transaction in transactions:
            self.num_items += 1

            year       = transaction.getElementsByTagName("year")[0].firstChild.data
            month      = transaction.getElementsByTagName("month")[0].firstChild.data
            day        = transaction.getElementsByTagName("day")[0].firstChild.data

            trans_type = transaction.getElementsByTagName("type")[0].firstChild.data
            name       = transaction.getElementsByTagName("name")[0].firstChild.data
            amount     = transaction.getElementsByTagName("amount")[0].firstChild.data
            currency   = transaction.getElementsByTagName("currency")[0].firstChild.data
            trans_id   = transaction.getElementsByTagName("id")[0].firstChild.data

            yield Transaction(year, month, day, trans_type, name, amount, currency, trans_id, written_to_file=True)

    def write(self, filename, transaction):
        input_file = open(filename, "a")

        input_file.write("\n<transaction>\n")
        input_file.write("\t<year>" + str(transaction.year) + "</year>\n")
        input_file.write("\t<month>" + str(transaction.month) + "</month>\n")
        input_file.write("\t<day>" + str(transaction.day) + "</day>\n")
        input_file.write("\t<type>" + str(transaction.trans_type) + "</type>\n")
        input_file.write("\t<name>" + str(transaction.name) + "</name>\n")
        input_file.write("\t<amount>" + str(transaction.amount) + "</amount>\n")
        input_file.write("\t<currency>" + str(transaction.currency) + "</currency>\n")
        input_file.write("\t<id>" + str(transaction.trans_id) + "</id>\n")
        input_file.write("</transaction>\n")

        input_file.close()
        

    def clear_tmp(self, tmp_filename):
        tmp = open(tmp_filename, "w")
        tmp.close()

    def remake_file(self, filename, transactions):

        # clear tmp file
        output_file = open(filename + ".tmp", "w")
        output_file.close()

        # write each transaction to tmp file
        for transaction in transactions:
            self.write(filename + ".tmp", transaction)


        # replace original file with tmp file
        os.rename(filename + ".tmp", filename)

    def rename_file(self, old_name, new_name):
        os.rename(old_name, new_name)

