"""
Example1-5
======================

Tokenizing string to exact specific infomations from string.
Requisite: String pattern must be know

"""

'''
input string with known pattern
string pattern:
    First Name
    Last Name
    Year of Birth
    Month of Birth
    Day of Birth
    Gender
'''

input = 'Li,Yong,1990,10,11,male'

tokens = input.split(',')

firstName = tokens[0]
lastName = tokens[1]

bithdate = (int(tokens[2]),int(tokens[3]),int(tokens[4]))
isMale = (tokens[5] == 'male')

print('Hello',firstName,lastName,bithdate,isMale)
