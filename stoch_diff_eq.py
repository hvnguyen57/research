import matplotlib
import numpy as np
import matplotlib.pyplot as plt

#testing stochastic differential equation modeling
sigma = 1.
mu = 10.
tau = 0.05

dt = 0.001
T = 1.
n = int(T / dt)
t = np.linspace(0, T, n)

sigma_bis = sigma * np.sqrt(2.0 / tau)
sqrtdt = np.sqrt(dt)

x = np.zeros(n)

#Euler-Maruyama method
for i in range (n-1):
    x[i + 1] = x[i] + dt * (-(x[i] - mu) / tau) + \
        sigma_bis * sqrtdt * np.random.randn()

fig, ax = plt.subplots(1, 1, figsize=(8,4))
ax.plot(t, x, lw=2)
plt.show()

ntrials = 10000
X = np.zeros(ntrials)

bins = np.linspace(-2., 14., 100)
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
for i in range(n):
    X += dt * (-(X - mu) / tau) + \
        sigma_bis * sqrtdt * np.random.randn(ntrials)
    if i in (5, 50, 900):
        hist, _ = np.histogram(X, bins=bins)
        ax.plot((bins[1:] + bins[:-1]) / 2, hist,
                {5: '-', 50: '.', 900: '-.', }[i],
                label=f"t={i * dt:.2f}")
    ax.legend()
plt.show()