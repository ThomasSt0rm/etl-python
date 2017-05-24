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
        TransformedData = TransformInstance.process(ExtractedData)
        LoadInstance = loader.Load()
        LoadData = LoadInstance.load(TransformedData, settings['ftp_csv']['datadest'] + "/outputCSV.csv")
for infile in os.listdir(settings['ftp_json']['datasource']):
    if infile.endswith('.json'):
        ExtractInstance = extractor.ExtractJSON()
        ExtractedData = ExtractInstance.extract(settings['ftp_csv']['datasource'] + "/" + infile)
        TransformInstance = transformer.TransformJSON()
        TransformedData = TransformInstance.process(ExtractedData)
        LoadInstance = loader.Load()
        LoadData = LoadInstance.load(TransformedData, settings['ftp_csv']['datadest'] + "/outputJSON.csv")


#jsondata = 'data-playground/input2.json'
#Extract = extractor.ExtractJSON()
#ExtractedData = Extract.extract(jsondata)
#Transform = transformer.TransformJSON()
#TransformedData = Transform.process(ExtractedData)
#LoadStep = loader.LoadJSON()
#LoadData = LoadStep.load(TransformedData, 'data-playground/output/output2.csv')
