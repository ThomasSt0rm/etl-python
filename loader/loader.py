import csv


class Load:
    def __init__(self):
        pass

    def load(self, data, outfile):
        self.outfile = outfile
        self.data = data
        key = data[0].keys()
        with open(outfile, 'w') as outfile:
            dict_writer = csv.DictWriter(outfile, key, delimiter=',', lineterminator='\n')
            dict_writer.writeheader()
            dict_writer.writerows(data)
        return 0
