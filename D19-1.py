import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,180)
y=np.cos(x*np.pi/180.0)

plt.plot(x,y)
plt.show()

# 畫出完整的sin圖形
x1=np.arange(0,3*np.pi,0.1)
y_sin=np.sin(x1)

plt.plot(x1,y_sin)
plt.show()

# 畫出完整的cos圖形
x2=np.arange(0,3*np.pi,0.1)
y_cos=np.cos(x2)

plt.plot(x2,y_cos)
plt.show()
