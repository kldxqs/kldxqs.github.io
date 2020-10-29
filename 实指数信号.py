import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(-8.0,8.0,1000)
plt.ylim(0,10)
f=2*np.exp((complex(-0.5,8))*t)
plt.subplot(111)
plt.title(u'绝对值')
plt.plot(t,np.abs(f))
plt.title(u'绝对值')
plt.plot(-t,np.abs(f))
plt.show()