import numpy as np
import matplotlib.pyplot as plt

Fig1 = plt.figure(1)
F1ax1 = Fig1.add_subplot(111)
Fig2 = plt.figure(2)
ax1 = Fig2.add_subplot(211)
ax2 = Fig2.add_subplot(212)
Fig3 = plt.figure(3)

x=np.linspace(0,3,100)

for i in xrange(5):
    #plt.figure(1)
    F1ax1.plot(x,np.exp(i*x/3))

    #plt.sca(ax1)
    ax1.plot(x,np.sin(i*x))
    #plt.sca(ax2)
    ax2.plot(x,np.cos(i*x))

#plt.figure(3)
for idx,color in enumerate("rgbyck"):
    Fig3.add_subplot(321+idx,axisbg=color)

#Fig1.show()
#Fig2.show()
#Fig3.show()
plt.show()
