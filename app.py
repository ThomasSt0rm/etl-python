import os
import yaml
import extractor
import loader
import transformer


with open("settings.yaml", 'r') as stream:
    settings = yaml.load(stream)


for infile in os.listdir(settings['ftp_csv']['datasource']):
    if infile.endswith('.csv'):
        ExtractInstance = extractor.ExtractCSV()
        ExtractedData = ExtractInstance.extract(settings['ftp_csv']['datasource'] + "/" + infile)
        TransformInstance = transformer.TransformCSV()
        TransformedData = TransformInstance.ProcessCSV(ExtractedData)
        LoadInstance = loader.LoadCSV()
        LoadData = LoadInstance.load(TransformedData, settings['ftp_csv']['datadest'] + "/output.csv")

