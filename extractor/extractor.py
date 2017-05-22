import csv
import numpy

class Extract_Basic:
    def __init__(self):
        pass

    def extract(self, number):
        self.number = number
        return number

class Extract_CSV:
    def __init__(self):
        pass

    def read_csv(self, csvfile):
        self.csvfile = csvfile
        reader = csv.reader(open(csvfile, 'rb'), delimiter=',')
        x = list(reader)
        result = numpy.array(x).astype(float)