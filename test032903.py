#filter function
def f(x):return x % 2 != 0 and x % 3 !=0
a = filter(f, range(2, 25))
print a

#map function 1 input
def cube(x): return x*x*x
b = map(cube,range(1,11))
print b

#map function-2 input
seq = range(8)
def add(x,y): return x+y
c = map(add, seq, seq)
print c

#reduce function 
def add(x,y): return x+y
d = reduce(add,range(1,11))
print d

