import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math

#testing stochastic differential equation modeling
sigma = 1.
mu = 10.
tau = 0.05

initRho = 1
initPhi = 0
k = 1

dt = 0.001 #time step
T = 1.0 #total time
n = int(T / dt) #number of steps
t = np.linspace(0, T, n) #vector of times

sigma_bis = sigma * np.sqrt(2.0 / tau) #constant from online forum
sqrtdt = np.sqrt(dt) #constant from online forum

rho = -math.sin(initPhi)
phi = (k * math.cos(initPhi)) / (1 + k * initRho)

x = np.zeros(n)

#Euler-Maruyama method
for i in range (n-1):
    x[i + 1] = x[i] + dt * (-(x[i] - mu) / tau) + \
        sigma_bis * (sqrtdt * np.random.randn())

#plotting simulation
fig, ax = plt.subplots(1, 1, figsize=(8,4))
ax.plot(t, x, lw=2)
plt.show()

# ntrials = 10000
# X = np.zeros(ntrials)

# bins = np.linspace(-2., 14., 100)
# fig, ax = plt.subplots(1, 1, figsize=(8, 4))
# for i in range(n):
#     X += dt * (-(X - mu) / tau) + \
#         sigma_bis * sqrtdt * np.random.randn(ntrials)
#     if i in (5, 50, 900):
#         hist, _ = np.histogram(X, bins=bins)
#         ax.plot((bins[1:] + bins[:-1]) / 2, hist,
#                 {5: '-', 50: '.', 900: '-.', }[i],
#                 label=f"t={i * dt:.2f}")
#     ax.legend()
# plt.show()