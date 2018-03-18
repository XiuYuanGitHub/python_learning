#!/usr/bin/python

#Open a file
fo = open("foo.txt","wb")
print "Name of the file:",fo.name
print "Closed or not:", fo.closed
print "Opening mode:",fo.mode
print "Softspace flag:",fo.softspace
print "++++++++++++++++++++++++++++++"

fo.write("Python is a great lauguage.\n Yeah its great!\n")
fo.write("li yong is best!\n+++++++++++++++++")

fo.close()

fo = open("foo.txt","r+")
pos = fo.seek(10,0);
str = fo.read(10)
print "Read :", str

pos = fo.tell()
print "Current pos", pos

fo.close()

print "Closed or not:", fo.closed


import os
os.remove("foo.txt")  #delete files


os.mkdir("newdir")  # make dir
os.rmdir("newdir")  # remove dir
#os.chdir("newdir") # change dir
os.mkdir("newdir3")  
str = os.getcwd()
print str


