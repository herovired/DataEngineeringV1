## Demonstrate reading a pipe delimited file
import csv 
cnt = 0
with open("../../data/tweets_assignment.txt","r") as f:
    reader = csv.reader(f,delimiter="|")
    for row in reader: ## there was no need to do an explicit split based on |
        print(row) ## The quoted text seems to have been automatically handled
        cnt+=1
        if cnt==10:
            break

## Demonstrate dict-reader
cnt = 0
with open("../../data/tweets_assignment.txt","r") as f:
    reader = csv.DictReader(f,delimiter="|")
    for row in reader:
        print(row['Tweet_Date']) ## this is now even simpler as column values can be accessed as dictionay key-value pairs
        cnt+=1
        if cnt==10:
            break