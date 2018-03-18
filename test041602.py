import numpy as np
import pylab as pl

data = np.random.normal(5.0,3.0,1000)
bins = np.arange(-5.,16.,1.)
f1 = pl.figure(1)
pl.subplot(221)
pl.subplot(222)
pl.title(r'$\alpha > \beta$')
pl.hist(data)
pl.subplot(212)
#pl.hist(data)
pl.hist(bins)
#pl.xlabel('data')
pl.xlabel(r"$\frac{x^2}{y^4}$")
pl.title('alpha > beta')
pl.text(0,0,'test', position=(5,3),size='50',rotation=45, fontname='fantasy',color='b')
pl.show()
