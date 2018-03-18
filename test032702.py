#!/usr/bin/python

dict = {'Name':'Zara','Age':7,'Class':'First'};
print dict
#print "dict['Name']:",dict['Name'];
#print "dict['Age']:",dict['Age'];

dict['Name'] = 'Liyong'
dict['School'] = 'BIT'

print dict

del dict['Class']
print dict

dict.clear()
print dict

del dict
print dict

dict = {1:15}
print dict[1]


