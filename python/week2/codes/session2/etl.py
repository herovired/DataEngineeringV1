'''
A simple class to load json data 
flatten it and write it out as csv
file
'''
import json

class ETL():
    def __init__(self,input_path):
        self.input_path = input_path

    def read_json(self):
        with open(self.input_path,"r") as con:
            self.data = json.loads(con.read())