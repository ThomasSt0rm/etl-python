from collections import defaultdict

class Transform_CSV:
    def __init__(self):
        pass

    def process_CSV(self, csvdata):
        self.csvdata = csvdata
        transformedlist = []
        count = 0
        for row in csvdata:
            if count == 0:
                count = count + 1
            else:
                x = {'ORDER_ID': row[0], 'ORDER_LINE_ID': row[1], 'ORDER_LINE_ITEM_ID': row[2], 'GROSS_MARGIN': int(float(row[10])) - int(float(row[9]))}
                transformedlist.append(x)
        return transformedlist
