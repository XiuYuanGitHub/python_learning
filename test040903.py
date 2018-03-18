import pprint
t=[[['a','b'],'c'],['d']]
print t
pprint.pprint(t,width=10)

from string import Template
t=Template('${village}folk send $$10 to $cause.')
x = t.substitute(village = 'Nottingham', cause = 'the ditch fund')
print x
y = t.safe_substitute(village = 'Nottingham')
print y


import time,os.path
photofiles = ['img_1074.jpg','img_1076.jpg','img_1077.jpg']
class BathchRename(Template):
    delimiter = '%'

fmt = raw_input('Enter rename style (%d-data %n-seqnum %f-format)')

t=BathchRename(fmt)
date = time.strftime('%d%b%y')
for i,filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date,n=i,f=ext)
    print '{0} --> {1}'.format(filename, newname)

print '----------------'

import logging
logging.debug('Debugging information')
logging.info('Information')
logging.warning('Warning: config file %s not found','server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

"""Generate a set of random numbers based on the number requested."""
import random

try:
    numbers = input("How many numbers do you want generated? ")
    for num in range(int(random.random() + 1), int(numbers) + 1):
        print(random.randint(num, num * 10))
except ValueError:
    print("Input is invalid!")
