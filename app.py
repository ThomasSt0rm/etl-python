import sys
import os

sys.path.append('extractor')
sys.path.append('loader')
sys.path.append('transformer')

import extractor
import loader
import transformer


OutFile = 'data-playground/output/out.csv'
InFile = 'data-playground/input/input.csv'
#CSVFile = raw_input("Enter the path to CSV file: ")
ExtractInstance = extractor.Extract_CSV()
ExtractedData = ExtractInstance.extract(InFile)
TransfromInstance = transformer.Transform_CSV()
TransformedData = TransfromInstance.process_CSV(ExtractedData)
LoadInstance = loader.Load_CSV()
LoadData = LoadInstance.load(TransformedData, OutFile)
