'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : Parser.py
License         : GPLv3 (See LICENSE.txt)
'''

from xml.dom import minidom
from Transaction import Transaction

def parse_xml(filename):
    doc = minidom.parse(filename)
    transactions = doc.getElementsByTagName("transaction")

    for transaction in transactions:
        #date       = transaction.getElementsByTagName("date")[0].firstChild.data
        year       = transaction.getElementsByTagName("year")[0].firstChild.data
        month      = transaction.getElementsByTagName("month")[0].firstChild.data
        day        = transaction.getElementsByTagName("day")[0].firstChild.data

        trans_type = transaction.getElementsByTagName("type")[0].firstChild.data
        name       = transaction.getElementsByTagName("name")[0].firstChild.data
        amount     = transaction.getElementsByTagName("amount")[0].firstChild.data
        currency   = transaction.getElementsByTagName("currency")[0].firstChild.data
        trans_id   = transaction.getElementsByTagName("id")[0].firstChild.data

        yield Transaction(year, month, day, trans_type, name, amount, currency, trans_id)
