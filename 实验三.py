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




import tkinter as tk  
window = tk.Tk()
window.title('My Window')
window.geometry('500x300') 
l = tk.Label(window, text='各类信号显示器' )
l.pack()
def sin信号():
    plt.show()
b = tk.Button(window, text='sin信号', command=sin信号)
b.pack()

window.mainloop()
