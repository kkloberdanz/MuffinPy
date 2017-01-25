'''
Programmer: Kyle Kloberdanz
Date Created: 25 Jan 2017
License: GPLv3 (see LICENSE.txt)
File: Trie.py
'''

class Trie:

    def __init__(self):
        self.data = None
        self.parent = None
        self.branches = []


    def find(self):
        if self == None:
            return None

        if self.data == item:
            return self

        elif len(self.branches) > 0:
            for branch in self.branches:
                if item in branch:
                    return 
                if found != None:
                    return found
        return None

    def insert(self):
        pass

    def clear(self):
        pass
