class Database:
    ''' Reads from and stores transactions to an XML file '''

    def __init__(self):

        # data_d stores dates as keys, and holds lists of
        # the values from the XML file
        self.data_d = {}

    def read(self, filename):
        # Read in XML file, and put it into datastructure
        for line in open(filename, "r"):

            # parse each xml line, for each new date, create
            # a new dictionary key
            # each key will be associated with a value that holds 
            # the values from the XML file

            parsed = Parser.parse_xml(line)



    def add_expense(self, expense):
        ''' takes expense of type Transaction '''
        pass

    def add_income(self, income):
        ''' takes income of type Transaction '''
        pass
