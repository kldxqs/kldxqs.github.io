# -*- coding: UTF-8 -*-
#coding=utf-8


import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

t=np.linspace(-10.0,10.0,1000)
plt.ylim(0,10)
f=2*np.exp((complex(-0.5,8))*t)
plt.subplot(111)
plt.title(u'绝对值')
plt.plot(t,np.abs(f))

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


x = [t*0.2*np.pi for t in x]
y = np.sin(x)
plt.subplot(111)
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x)*f), \omega = \frac{1}{5} \pi$') 
plt.plot(x, y)
plt.show()