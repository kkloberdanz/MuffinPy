#!/usr/bin/python3

'''
Programmer      : Kyle Kloberdanz
Date Created    : 21 Jan 2017
File            : app.py
License         : GPLv3 (See LICENSE.txt)
'''

import sys
import Interface 
from Error import Error

if __name__ == "__main__":

    usage = sys.argv[0] + " [XML_FILE] OPTION\n" +\
            "\tOptions:\n" +\
            "\t\t--cli      Launch shell\n"

    e = Error(sys.argv[0], usage)
    if len(sys.argv) < 3:
        e.throw("Not enough input arguments")

    filename = sys.argv[1]
    interface = Interface.Interface()
    interface.read(filename)
    for arg in sys.argv[2:]:
        if arg == "--cli": 
            interface.launch_cli()
