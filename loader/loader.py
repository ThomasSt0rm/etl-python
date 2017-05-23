import csv


class Load:
    def __init__(self):
        pass

    def load(self, number):
        return number
class Load_CSV:
    def __init__(self):
        pass

    def load(self, data, outfile):
        self.outfile = outfile
        self.data = data
        with open(outfile, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in data.items():
                writer.writerow([key, value])
