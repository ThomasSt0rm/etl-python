import sys
import os
import yaml

sys.path.append('extractor')
sys.path.append('loader')
sys.path.append('transformer')

import extractor
import loader
import transformer

with open("settings.yaml", 'r') as stream:
    settings = yaml.load(stream)

print settings['ftp_csv']['datatype']


for file in os.listdir(settings['ftp_csv']['datasource']):
    if file.endswith('.csv'):
        ExtractInstance = extractor.Extract_CSV()
        ExtractedData = ExtractInstance.extract(settings['ftp_csv']['datasource'] + "/" + file)
        TransformInstance = transformer.Transform_CSV()
        TransformedData = TransformInstance.process_CSV(ExtractedData)
        LoadInstance = loader.Load_CSV()
        LoadData = LoadInstance.load(TransformedData, settings['ftp_csv']['datadest'] + "/output.csv")

