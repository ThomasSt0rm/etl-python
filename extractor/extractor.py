import csv


class Extract_CSV:
    def __init__(self):
        pass

    def extract(self, inputcsv):
        self.inputcsv = inputcsv
        reader = csv.DictReader(open(inputcsv))
        return reader

