import sys

sys.path.append('extractor')
sys.path.append('loader')
sys.path.append('transformer')

import extractor
import loader
import transformer

raw_number = input("Enter the number to transform: ")
structure = extractor.Extract(raw_number)
structure.print_value()

extracted_number = structure.extract(raw_number)
#print(extracted_number)
transform_step = transformer.Transform(extracted_number)
transformed_number = transform_step.transform(extracted_number)
loading_step = loader.Load(transformed_number)
loaded_number = loading_step.load(transformed_number)
print loaded_number
