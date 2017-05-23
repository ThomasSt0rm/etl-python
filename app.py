import sys
import os

sys.path.append('extractor')
sys.path.append('loader')
sys.path.append('transformer')

import extractor
import loader
import transformer

#raw_number = input("Enter the number to transform: ")
#structure = extractor.Extract_Basic()
#extracted_number = structure.extract(raw_number)
#transform_step = transformer.Transform()
#transformed_number = transform_step.transform(extracted_number)
#loading_step = loader.Load()
#loaded_number = loading_step.load(transformed_number)
#print loaded_number

#while True:
#    for file in os.listdir('data-playground/input/'):
#        if file.lower().endswith('.csv'):
#            extract_step = extractor.Extract_CSV()
#            extracted_data = extract_step.read_csv(file)


CSVFile = raw_input("Enter the path to CSV file: ")
ExtractInstance = extractor.Extract_CSV()
ExtractedData = ExtractInstance.read_csv(CSVFile)
TransfromInstance = transformer.Transform_CSV()
TranformedData = TransfromInstance.process_CSV(ExtractedData)
print TranformedData
print type(TranformedData)