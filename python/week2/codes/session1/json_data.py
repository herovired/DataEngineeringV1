## show the json data read, you can discuss the nested tree structure of json files
import json
with open("../..data/sample_json.json","r",encoding="utf-8") as f:
    data = json.loads(f.read())
print(data.keys())
print(data['features'][0])