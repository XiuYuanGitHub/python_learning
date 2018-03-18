"""
Example 1-3
===============

Introduces Python Programming Langauge to novices
"""

# Python Numbers
age = 26   #Integer
pi = 3.13159  #Floating point number

#Python Strings
string = 'Adnan Umer'
tokens=string.split() #splits string on space and return parts

#List Indexing
firstName = tokens[0]
lastName = tokens[1]

#String Concatination
my_name = firstName + ' '+lastName
if(string == my_name):
    print('Yes! Both strings are same')
else:
    print('No,not same')

#Python List
students = ['Li', 'zhang', 'He']
students.append('Zhao')  #insert another item in list

#for loop
for student in students:
    print ('Hello!',student)

ages = (19, 22, 18)

uniqueAges = set(ages)
uniqueAges.add(18)
uniqueAges.remove(22)

for thisage in ages:
    print(thisage)

if 18 in uniqueAges:
    print('There is an 18-year-old present!')
    
students.sort()
orderedUniqueAges = sorted(uniqueAges)

print(students)
print(uniqueAges)

netWorth = { }
netWorth['A'] = 100
netWorth['B'] = 10000
netWorth['C'] = 200
netWorth['D'] = 500

for (person, worth) in netWorth.items():
    if worth < 500:
        print(person,'is less than 500')

if 'D' in netWorth:
    print('D is in the netWorth!')

    
