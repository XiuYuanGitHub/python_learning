print range(3,6)

args = [3,6]
print range(*args)

def parrot(voltage, state = 'a stiff', action = 'voom'):
    print "___This parrot wouldn't ",action,
    print "if you put ",voltage, "volts through it ",
    print "E's", state, "!"

d= {"voltage":"four million","state":"bleedin' demised","action":"VOOM"}

parrot(**d)

basket = ['apple', 'orange','apple','bear','cat']
fruit = set(basket)

print ('apple' in fruit)
b= 'bear ' in fruit
print b

a = set("adsasdfgasd")
b= set('qwrvssdaseasas')
print a
print b
print a-b
print a|b
print a&b
print a^b

print dict([(x,x**2) for x in (2,4,6)])
m=dict([("a",1),('b',2),('c',3)])
print m
print dict(a=1,b=2,c=5)

for i,j in m.iteritems():
    print i,j

for k,v in enumerate(['a','b','v']):
    print k,v


que = ["name",'age','color']
ans = ['Jone', 5, 'blue']

for a,b in zip(que,ans):
    print 'What is {0}? It is {1}.'.format(a,b)

for i in reversed(range(1,10,1)):
    print i

for f in sorted(set(basket)):
    print f
    
