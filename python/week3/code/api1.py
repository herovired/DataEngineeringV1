import requests 
url = "https://api.chucknorris.io/jokes/categories"
resp1 = requests.get(url).json()
resp2 = requests.get(url).text
print(resp1)
print(type(resp1))
print("*"*100)
print(resp2)
print(type(resp2))