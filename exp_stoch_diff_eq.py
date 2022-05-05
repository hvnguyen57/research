import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math

curvature = 1
k = 1
ro = 1
phi = 1
z = math.sin(phi)
roInitial = 1
positiveInfinity = math.inf

dt = 0.001
T = 1.
n = int(T / dt)
t = np.linspace(0, T, n)
sqrtdt = np.sqrt(dt)

K1, K2 = 0, positiveInfinity
zDot = K1(ro - roInitial) - (K2 * z)
dPhi = -(k / 1 + (k * ro)) * math.sin(phi)
u2 = (1 / math.sqrt(1 - z**2)) * (((k*(1-z^2)) / (1 + k * ro)) - zDot)

x = np.zeros(n)

#Euler-Maruyama method
for i in range (n-1):
    x[i + 1] = x[i] + dt * dPhi - u2 * sqrtdt * np.random.randn()

fig, ax = plt.subplots(1, 1, figsize=(8,4))
ax.plot(t, x, lw=2)
plt.show()

