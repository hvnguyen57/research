#Marine Robot Movement Simulation using Euler-Maryama Method

import matplotlib.pyplot as plt
import numpy as np
import argparse
    
def metaHPrime(alpha : float, rho0: float) -> callable:
    def hPrime(rho : float) -> float:
        return alpha * (1 - rho0 ** 2 / rho ** 2)
    return hPrime

def run_simulation(args):
    #paramaters for 
    initialTime = 0
    endTime = 1
    n = 1000
    timeStep = np.linspace(initialTime, endTime, n)
    
    #numerical parameters for the "math" of the simulation
    mu = args.mu
    sigma = 1
    alpha = 1
    rho0 = args.initialRho
    
    hPrime = metaHPrime(alpha, rho0)
    deltaT = float(endTime - initialTime) / n
    rhos = np.zeros(n)
    phis = np.zeros(n)
    
    rhos[0] = 1
    phis[0] = 0
    
    for i in range (1, timeStep.size):
        t = timeStep[i] #not needed, time invariant SDE
        rho = rhos[i - 1]
        phi = phis[i - 1]
        
        rhos[i] = rho + -1 * np.sin(phi) * deltaT
        phis[i] = phi + (hPrime(rho) * np.cos(phi) - mu * np.sin(phi)) * deltaT + sigma * np.random.normal(loc=0.0, scale=np.sqrt(deltaT))
        
    return ((timeStep, rhos), (timeStep, phis))

def run_and_plot_simulations(num_sims: int, args) -> None:
    fig, axs = plt.subplots(2, 1)
    axs[0].set_title("rho")
    axs[1].set_title("phi")
    
    for _ in range(num_sims):
        output = run_simulation(args)
        axs[0].plot(*output[0])
        axs[1].plot(*output[1])
        
    plt.show()    

def main():
    parser = argparse.ArgumentParser(description= "Run and ploit simulations of SDE")
    parser.add_argument("-m", "--mu", type = float, default = 1, help = "mu")
    parser.add_argument("-r", "--rho-init", dest = "initialRho", type = float, default = 1, help = "mu")
    parser.add_argument("-p", "--phi-init", dest = "initialPhi", type = float, default = 1, help = "mu")
    args = parser.parse_args()

    NUM_SIMS = 5
    run_and_plot_simulations(NUM_SIMS, args)
    
if __name__ == "__main__":
    main()