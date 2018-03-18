import time
ticks = time.time()
print("Number of ticks since 12:00am,Jan 1,1970:",ticks)

#!/usr/bin/python
localtime1 = time.localtime(time.time())
print("localtime1:",localtime1)

#!/usr/bin/python
asctime1 = time.asctime(time.localtime(time.time()))
print("asctime1 : ", asctime1)

#!/usr/bin/python
import calendar
cal = calendar.month(2016,3)
print ("Here is the calendar:")
print cal

