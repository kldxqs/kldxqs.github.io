import matplotlib.pyplot as plt
import numpy as np 
x = np.linspace(0, 3 * np.pi, 100)
y = np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 
plt.subplot(1,2,1)
plt.title(r'$f(x)=sin(x)$') 
plt.plot(x, y)

x1 = [t*0.375*np.pi for t in x]
y1 = np.sin(x1)
plt.subplot(1,2,2)
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') 
plt.plot(x1, y1)



import numpy as np
import matplotlib.pyplot as plt1

def rect_wave(x,c,c0):     
     if x>=(c+c0):
          r=0.0
     elif x<c0:
          r=0.0
     else:
          r=1
     return r

x=np.linspace(-2,4,1000)
y=np.array([rect_wave(t,2.0,-1.0) for t in x])
plt1.ylim(-0.5,1.5)
plt1.plot(x,y)




import tkinter as tk  
window = tk.Tk()
window.title('各个信号显示器')
window.geometry('500x300') 
l = tk.Label(window, text='各类信号显示器' )
l.pack()

def sin信号():
    plt.show()
b = tk.Button(window, text='sin信号', command=sin信号)
b.pack()
def 矩形信号():
    plt1.show()
c = tk.Button(window, text='矩形信号', command=矩形信号)
c.pack()

window.mainloop()

