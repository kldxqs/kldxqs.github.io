import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(-3.0,3.0,1000)
plt.ylim(0,4)
f=2*np.exp((complex(-0.5,8))*t)

plt.subplot(221)
plt.title(u'实部')
plt.plot(t,np.real(f))

plt.subplot(222)
plt.title(u'虚部')
plt.plot(t,np.imag(f))

plt.subplot(223)
plt.title(u'绝对值')
plt.plot(t,np.abs(f))
plt.title(u'绝对值')
plt.plot(-t,np.abs(f))
plt.show()