import csv

class Load_CSV:
    def __init__(self):
        pass

    def load(self, data, outfile):
        self.outfile = outfile
        self.data = data
        with open(outfile, 'w') as f:
            fields = ['ORDER_ID', 'ORDER_LINE_ID', 'ORDER_LINE_ITEM_ID','GROSS_MARGIN']
            w = csv.DictWriter(f, fieldnames=['ORDER_ID', 'ORDER_LINE_ID', 'ORDER_LINE_ITEM_ID','GROSS_MARGIN'], extrasaction='ignore', delimiter = ',')
            w.writeheader()
        #    print(data)
            for item in data:
                w.writerow(item)
        #    count = 0
        #    writer = csv.writer(f, dialect="excel-tab")
        #    for row in data:
        #        if count == 0:
        #            header=row.keys()
        #            writer.writerow(header)
        #            count=+1
        #        writer.writerow(row.values())
        #CSV ="\n".join([k+','+",".join(v) for k,v in data.items()]) 
        #print CSV
        #with open(outfile, "w") as file:
        #    file.write(CSV)