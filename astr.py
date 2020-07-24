import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax= fig.gca(projection='3d') 
t=np.arange(-2*np.pi,2*np.pi, 0.1)

z=0
a=1
b=0.99
x=a*np.cos(t)
y=b*np.sin(t)

i_m=15
a_m=0.387
b_m=0.374
alpha=1.36
x2=a_m*np.cos(t)*np.cos(alpha)-b_m*np.sin(t)*np.sin(alpha)
y2=(a_m*np.cos(t)*np.sin(alpha)+b_m*np.sin(t)*np.cos(alpha))*np.cos(i_m)
z2= (a_m*np.cos(t)*np.sin(alpha)+b_m*np.sin(t)*np.cos(alpha))*np.sin(i_m)


a_v=0.723
b_v=0.722
alpha=2.3
x3=a_v*np.cos(t)*np.cos(alpha)-b_v*np.sin(t)*np.sin(alpha)
y3=a_v*np.cos(t)*np.sin(alpha)+b_v*np.sin(t)*np.cos(alpha)

a_mars=1.524
b_mars=1.517
alpha=0.87
x4=a_mars*np.cos(t)*np.cos(alpha)-b_mars*np.sin(t)*np.sin(alpha)
y4=a_mars*np.cos(t)*np.sin(alpha)+b_mars*np.sin(t)*np.cos(alpha)

a_j=5.2
b_j=5.196
alpha=0.28
x5=a_j*np.cos(t)*np.cos(alpha)-b_j*np.sin(t)*np.sin(alpha)
y5=a_j*np.cos(t)*np.sin(alpha)+b_j*np.sin(t)*np.cos(alpha)

a_s=9.582
b_s=9.567
alpha=1.57
x6=a_s*np.cos(t)*np.cos(alpha)-b_s*np.sin(t)*np.sin(alpha)
y6=a_s*np.cos(t)*np.sin(alpha)+b_s*np.sin(t)*np.cos(alpha)

a_y=19.224
b_y=19.18
alpha=2.97
x7=a_y*np.cos(t)*np.cos(alpha)-b_y*np.sin(t)*np.sin(alpha)
y7=a_y*np.cos(t)*np.sin(alpha)+b_y*np.sin(t)*np.cos(alpha)

a_n=30
b_n=29.998
alpha=0.69
x8=a_n*np.cos(t)*np.cos(alpha)-b_n*np.sin(t)*np.sin(alpha)
y8=a_n*np.cos(t)*np.sin(alpha)+b_n*np.sin(t)*np.cos(alpha)

ax.plot(x8,y8,z, color='steelblue')
ax.plot(x7,y7,z, color='deepskyblue')
ax.plot(x6,y6,z,color='y')
ax.plot(x5,y5,z, color='burlywood')
ax.plot(x4,y4,z, color='orangered')
ax.plot(x3,y3,z, color='maroon')

ax.plot(x2,y2, z2, color='orange')
ax.plot(x,y, z, color='b')

plt.show()