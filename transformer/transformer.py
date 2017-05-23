from collections import defaultdict

class Transform_CSV:
    def __init__(self):
        pass

    def process_CSV(self, csvdata):
        self.csvdata = csvdata
        transformdict = defaultdict(list)
        #print type(transformdict)
        temp_list = []
        for row in csvdata:
            temp_list.append(row)
        for dictionary in temp_list:
            transformdict['ORDER_ID'].append(dictionary['ORDER_ID'])
            transformdict['ORDER_LINE_ID'].append(dictionary['ORDER_LINE_ID'])
            transformdict['ORDER_LINE_ITEM_ID'].append(dictionary['ORDER_LINE_ITEM_ID'])
            transformdict['GROSS_MARGIN'].append(int(float(dictionary['SALES_PRICE'])) - int(float(dictionary['BASE_PRICE'])))
        return transformdict
