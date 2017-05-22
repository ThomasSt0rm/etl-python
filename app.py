import sys

sys.path.append('extractor')
sys.path.append('loader')
sys.path.append('transformer')

import extractor
import loader
import transformer

raw_number = input("Enter the number to transform: ")
extracted_number = extractor.Extract(raw_number)
extracted_number.extract(raw_number)
transformed_number = transformer.Transform(extracted_number)
transformed_number.transform(extracted_number)
loaded_number = loader.Load()
loaded_number.load(transformed_number)
print loaded_number
