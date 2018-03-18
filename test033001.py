filter
def f(x): return x % 2 !=0 and x % 3 != 0
print filter(f, range(2, 10))
#map
def cube(x): return x*x*x
print map(cube, range(1, 11))
#reduce
def add(x, y): return x+y
print map(add, range(1, 10),range(2, 11))
print reduce(add,range(1,11))
print reduce(add,range(1,2),0)


def make_inc(n):
    return lambda x:x+n

f = make_inc(40)
print f(0)

#def add1(a,b):
#    return lambda a,b:a+b

#f1 = add1(1,2)
#print f1


squares = [x**2 for x in range(10)]
print squares

print [(x,y) for x in [1,2,3] for y in [1,2,3] if x !=y ]
print [(x,x**2) for x in range(6)]


vec = [[1,2,3],[4,5,6],[7,8,9]]
print [num for elem in vec for num in elem]

import math
print [round(math.pi,i) for i in range(1,6)]

