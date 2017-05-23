import csv

class Load_CSV:
    def __init__(self):
        pass

    def load(self, data, outfile):
        self.outfile = outfile
        self.data = data
        #print data
        key = data[0].keys()
        with open(outfile, 'w') as file:
            dict_writer = csv.DictWriter(file, key)
            dict_writer.writeheader()
            dict_writer.writerows(data)
