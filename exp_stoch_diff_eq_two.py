#another attempt
import numpy as np
import matplotlib as plt
import math

#curvature at closest point
k = 1
#number of steps
n = 1000
#bearing between robot and curve
phiInit = 1
#relative distance
rhoInit = 1
#time
T = 1
#number of simulations
M = 1000
#random inital value
r = 1

#calc for each time step
dt = T/n
#simulation
St = np.exp( k * math.cos(np.random.normal(0, np.sqrt(dt), size = (M - 1, n)).T) / (1 + k * rhoInit) )

#array of 1s
St = np.vstack([np.ones(M), St])
#multiple through with r
St = r * St.cumprod(axis = 0)
St[1]