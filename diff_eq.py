import matplotlib.pyplot as pl 
import matplotlib.pyplot as p2
import numpy as np 
from scipy.integrate import odeint
import math

def func (z, t):
    phi, ro = z
    print (z,t)
    curvature = abs((-math.cos(ro) * math.sin(ro)) / (-math.cos(ro)**3)); #curvature = || d * d2 || / || d || ^ 3
    #current curvature equation not correct; ask about this in meeting
    #return [-math.sin(ro), (math.cos(ro) * curvature)/(1 + (curvature * phi))]
    return [-math.sin(ro), (math.cos(ro))/(1 + (phi))]

def euler(f, x0, t):
    x = np.zeros(len(t))
    x[0] = x0;
    for n in range (0, len(t)-1):
        x[n+1] = x[n] + f(x[n], t[n]) * (t[n+1] - t[n])
    return x

#Solving diff equations
t = np.linspace(0,10,501)   
z0 = [1,0]
xx=odeint(func, z0, t)
pl.figure(1)
pl.plot(t, xx[:,0],t,xx[:,1])
pl.xlabel('Time')
pl.legend(['phi', 'ro'])
pl.grid(True)
pl.show()

#Euler approx method
t2 = np.linspace(0,2,21);
x0 = 1
f = lambda x,t: x
x = euler(f,x0,t)
x_true = np.exp(t2)
p2.plot(t,x,'b.-',t2,x_true,'r-')
p2.legend(['Euler','True'])
p2.axis([0,2,0,9])
p2.grid(True)
p2.show()
