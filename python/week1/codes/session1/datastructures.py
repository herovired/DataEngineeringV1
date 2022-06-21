## Numbers
a = 3
b = 3.0
print(a)
print(b)

## What will happen if we divide the two
print(a/b)

##Strings
s1 = "This is a string"
s2 = "This is also a string"
s3 = '''This too is a string''' ## you can write multiline strings using ''' triple quotes '''

s1[0]
s1[2]
s1[-1]

for s in s1:
    print(s)

a = 4 
print(a) ## you can change numbers at place

print(s1)
s1 = 'This is not a string'
print(s1) ## you can overwrite the whole string


s1[0]="h" #but you can't change the strings in place


print(s1)
print(s2)

print(s1+s2) # you can concatenate two strings 

print(dir(s1)) 
### this prints out all the methods, functions and attributes supported by python classes. Ignore the names that have this form __name__ 

##Lists
l1 = [1,2,3,4,'a','b',[99,24,11]]
l1[0]
for i in l1:
    print(i)

##Tuples
t = (1,2,3,4,(56,78,'a'),[7,8,9])
l1 = [1,2,3,4,(56,78,'a'),[7,8,9]]
for i in t:
    print(i)

l1[0]
l1[0]=100

print(l1)
t[0] = 100

## Sets
set_a = set(['a','b','c'])
set_b = {'b','c','d'}

print(dir(set_a))

for i in set_a:
    print(i)
set_a[0]

set_a.intersection(set_b)
set_a.difference(set_b)

## Dictionaries
d = {'name':'a','age':29,'prev_companies':['abc','def']}
d[0]
d['name']
d['prev_companies']
for i in d:
    print(i)
for i in d:
    print(d[i])
d['new_key'] = 'value'

print('value' in d)

print('new_key' in d)



 