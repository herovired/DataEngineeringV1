import requests
import logging
import random
import csv
categories_url = "https://api.chucknorris.io/jokes/categories"
logging.basicConfig(filename="log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class Noris():
    def __init__(self,write_path:str):
        self.write_path = write_path
        self.created_at = []
        self.updated_at = []
        self.jokes = []
        self.categories = []
        self.counter = 0
        self.tries = 0

    def _get_categories(self):
        self.cats = requests.get(categories_url).json()
    def _get_category_joke(self,category:str):
        category_url = f"https://api.chucknorris.io/jokes/random?category={category}"
        resp = requests.get(category_url).json()
        return resp 
    def _parse_result(self,resp:dict):
        created_at = resp['created_at']
        updated_at = resp['updated_at']
        joke = resp['value']
        return (created_at,updated_at,joke)
    
    def _create_memory_store(self,category:str,res:tuple):
        self.tries+=1
        created_at,updated_at,joke = res
        if joke  not in self.jokes:
            self.jokes.append(joke)
            self.created_at.append(created_at)
            self.updated_at.append(updated_at)
            self.categories.append(category)
            self.counter+=1
            logger.debug(f"Joke added to in memory db, num jokes: {self.counter}")
        else:
            logger.debug(f'Duplicate joke found, num tries: {self.tries} and num jokes: {self.counter}')

    def _fetch_controller(self,num_rows = 30):
        self._get_categories()
        logger.debug("Categories endpoint hit")
        while self.counter<num_rows:
            category = random.choice(self.cats)
            logger.debug(f'Category {category} chosen for fetch')
            resp = self._get_category_joke(category=category)
            res = self._parse_result(resp)
            self._create_memory_store(category=category,res=res)
    def write_data(self):
        logger.debug(f'Writting data at {self.write_path}')
        with open(self.write_path,"w") as con:
            writer = csv.DictWriter(con,delimiter=",",
                                    fieldnames=['updated_at','created_at','joke'])
            writer.writeheader()
            for u_a,c_a,j in zip(self.updated_at,self.created_at,self.jokes):
                writer.writerow({'updated_at':u_a,'created_at':c_a,'joke':j})

    def fetch(self,num_rows=30):
        self._fetch_controller(num_rows=num_rows)
        logger.debug('Finished creating in memory db')
        self.write_data()


if __name__=="__main__":
    path = "jokes.csv"
    n = Noris(path)
    n.fetch(num_rows=30)
        

