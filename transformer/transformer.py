

class TransformCSV:
    def __init__(self):
        pass

    def process(self, data):
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

class TransformJSON:
    def __init__(self):
        pass

    def process(self, data):
        self.data = data
        newdata = []
        for item in data:
            x = {'ORDER_ID': item['order_id'], 'ORDER_LINE_ID': item['order_line_id'], 'ORDER_LINE_ITEM_ID': item['order_line_item_id'], 'GROSS_MARGIN': int(item['sales_price']) - int(item['base_price'])}
            newdata.append(x)
        return newdata