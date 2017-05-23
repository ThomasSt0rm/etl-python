import csv

class Load_CSV:
    def __init__(self):
        pass

    def load(self, data, outfile):
        self.outfile = outfile
        self.data = data
        with open(outfile, 'wb') as f:
            w = csv.DictWriter(f, data.keys())
            w.writeheader()
            w.writerow(data)