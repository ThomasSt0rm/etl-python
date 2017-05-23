import csv


class Extract_Basic:
    def __init__(self):
        pass

    def extract(self, number):
        self.number = number
        return number

class Extract_CSV:
    def __init__(self):
        pass

    def extract(self, inputcsv):
        self.inputcsv = inputcsv
        reader = csv.DictReader(open(inputcsv))
        #print type(reader)
        return reader
                
