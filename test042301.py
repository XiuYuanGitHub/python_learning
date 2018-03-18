from numpy import *

def test(m,n):
    print "++++++++++++++++++++++++++"
    m.shape = 3,4
    print n.shape

    m[0,1] = 99
    print n

    print "m is n:",m is n
    print "m.base is n:",m.base is n

if __name__ == '__main__':
    a= arange(12);    b=a;    test(b,a)
    a= arange(12);  c= a.view();    test(c,a)
    a= arange(12);  d= a.copy();    test(d,a)








