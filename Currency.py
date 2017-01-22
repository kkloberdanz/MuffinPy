'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : Currency.py
License         : GPLv3 (See LICENSE.txt)
'''

def dollars_to_cents(amount):
    if '.' not in amount:
        amount += ".00"
    return int(amount.replace('.', ''))
