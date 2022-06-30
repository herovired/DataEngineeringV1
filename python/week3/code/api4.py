import os
import requests
key = os.environ.get('nyt_key')
url = f"https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={key}"
resp = requests.get(url).json()
print(resp)