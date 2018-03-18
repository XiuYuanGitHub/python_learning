tup1 = ('phy','chem',1997,2000)
tup2 = (1,2,3,4)
print tup1[0]
print tup2[1:4]
print tup1 + tup2

#del tup1
print tup1

import re

line = "Cats are smarter than dogs";
matchObj = re.match(r'(.*)are(\.*)',line,re.M)
if matchObj:
    print matchObj.group()

else:
    print "No match!!"

import smtplib
sender = '386976876@qq.com'
receivers = ['qcxyliyong@163.com']

messages = """ From: From person <386976876@qq.com>
To : To person <qcxyliyong@163.com>
Subject:SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message)
    print "Successfully"

except:
    print "Error!"
        
