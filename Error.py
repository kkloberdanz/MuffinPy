'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : app.py
License         : GPLv3 (See LICENSE.txt)
'''

class Error:
    def __init__(self, prog_name, usage=""):
        self.name = prog_name
        self.usage = usage

    def throw(self, message):
        print("error: " + message)
        if self.usage:
            print(self.usage)
        quit() 

    def warning(self, message):
        print("warning: " + message)
