## One can use csv module without using the with statement as shown below
import csv
f = open("../../data/tweets_assignment.txt","r")
reader = csv.reader(f,delimiter="|")
cnt = 0
for row in reader: ## there was no need to do an explicit split based on |
        print(row) ## The quoted text seems to have been automatically handled
        cnt+=1
        if cnt==10:
            break
f.close() ## Manually close the connection

## No need to do that as with will close the connection automatically
cnt = 0
with open("../../data/tweets_assignment.txt","r") as f:
    reader = csv.reader(f,delimiter="|")
    for row in reader: ## there was no need to do an explicit split based on |
        print(row) ## The quoted text seems to have been automatically handled
        cnt+=1
        if cnt==10:
            break
