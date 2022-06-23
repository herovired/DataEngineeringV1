## Class Excercise:

Extract the information about each earthquake event's:

1. Magnitude 
2. Location
3. Url

Create three lists with information on the three parameters listed above. Then write this information in a csv file.

**Rough Solution**

```python
import csv
magnitude = [f['properties']['mag'] for f in data['features']]
location = [f['properties']['place'] for f in data['features']]
url = [f['properties']['url'] for f in data['features']]

with open("../../data/json_data.csv","w",encoding='utf-8') as f:
    fieldnames = ['magnitude','location','url']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for mag,loc,u in zip(magnitude,location,url):
        writer.writerow({'magnitude': mag, 'location': loc,'url':u})
```
