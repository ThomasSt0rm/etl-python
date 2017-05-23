import sys
import os

sys.path.append('extractor')
sys.path.append('loader')
sys.path.append('transformer')

import extractor
import loader
import transformer



CSVFile = raw_input("Enter the path to CSV file: ")
ExtractInstance = extractor.Extract_CSV()
ExtractedData = ExtractInstance.extract(CSVFile)
TransfromInstance = transformer.Transform_CSV()
TransformedData = TransfromInstance.process_CSV(ExtractedData)
#print TransformedData
#print type(ExtractedData)
#print TranformedData
print TransformedData