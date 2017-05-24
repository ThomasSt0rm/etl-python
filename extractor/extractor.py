import csv
import json


class ExtractCSV:
    def __init__(self):
        pass

    def extract(self, inputcsv):
        self.inputcsv = inputcsv
        reader = csv.reader(open(inputcsv))
        return reader

class ExtractJSON:
    def __init__(self):
        pass

    def extract(self, inputjson):
        self.inputjson = inputjson
        with open(inputjson) as inputjson:
            data = json.load(inputjson)
        return data

