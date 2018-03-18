import numpy as np
import pylab as pl

x1= [1,2,3,4,5]
y1= [1,4,9,16,25]
x2= [1,2,4,6,8]
y2= [2,4,8,12,16]
#pl.plot(x,y)
plot1, = pl.plot(x1,y1,'-.r*')
plot2, = pl.plot(x2,y2,'--gs')
#give the title
pl.title('plot of y vs. x')  
#make the axis labels
pl.xlabel('x axis')
pl.ylabel('y axis')
#set the axis limits
pl.xlim(0.0,7.5)
pl.ylim(0.0,27.5)
#set the legend
pl.legend([plot1, plot2], ['red line', 'green circles'])# make legend
pl.show()


