import requests
category = 'animal'
url = f"https://api.chucknorris.io/jokes/random?category={category}"
resp = requests.get(url).json()
print(resp)
 