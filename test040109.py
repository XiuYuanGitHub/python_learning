class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(sef):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print 'My exception occurred , value:', e.value


with open("textfile.txt") as f:
    for line in f:
        print line


class Complex:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag

x = Complex(3.0,4.5)
print x.r, x.i

x.counter = 1
print x.counter

print "===================="
class B:
    print 'BB'
    pass
    print 'BB1'
class C(B):
    print 'CC'
    pass
    print 'CC1'
class D(C):
    print 'DD'
    pass
    print 'DD1'

print "_____________________"
for c in [B,C,D]:
    try:
        raise c()
    except D:
        print "D"
    except C:
        print "C"
    except B:
        print "B"

print "===================="

class Reverse:
    """Iterator for looping over a seq backwards"""
    print 'nothing'
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        self.num = 0
        print 'init'
    def __iter__(self):
        self.num +=1
        print 'iter',self.num
        return self
    def next(self):
        print 'next'
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')

iter(rev)
for char in rev:
    print char
