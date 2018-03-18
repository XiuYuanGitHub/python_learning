import cv2
from numpy import *


a = arange(6)
print a
print a.strides

b = arange(12).reshape(3,4)
print b
print b.strides

c = arange(27).reshape(3,3,3)
print c
print c.strides

