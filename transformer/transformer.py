

class TransformCSV:
    def __init__(self):
        pass

    def ProcessCSV(self, data):
        self.data = data
        newdata = []
        count = 0
        for row in data:
            if count == 0:
                count = count + 1
            else:
                x = {'ORDER_ID': row[0], 'ORDER_LINE_ID': row[1], 'ORDER_LINE_ITEM_ID': row[2], 'GROSS_MARGIN': int(float(row[10])) - int(float(row[9]))}
                newdata.append(x)
        return newdata
