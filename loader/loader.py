import csv


class LoadCSV:
    def __init__(self):
        pass

    def load(self, data, outfile):
        self.outfile = outfile
        self.data = data
        key = data[0].keys()
        with open(outfile, 'w') as outfile:
            dict_writer = csv.DictWriter(outfile, key)
            dict_writer.writeheader()
            dict_writer.writerows(data)

