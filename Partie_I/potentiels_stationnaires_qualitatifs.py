
'''In this program, we will discuss the precision and numerical resolution.
We will particularly discuss the cases of the infinite potential well and the harmonic potential,
which are the simplest and easiest to solve analytically.
We will highlight the effects of discretization in these cases.'''

import matplotlib
matplotlib.use('Agg')  # Utilise un backend non interactif (pour enregistrer des figures)

'''We start by importing the necessary modules'''
import numpy as np
import matplotlib.pyplot as plt
from resol import *
from potentiels import *

'''We define the simulation parameters'''
L = 10
n = 1000
x = np.linspace(-L/2, L/2, n)

'''Numerical solution for the infinite potential well'''
x, w, v = resol(L, n, puit_de_potentiel, Norm=True)

'''Analytical solution for the infinite potential well'''
def psi_puit_infini(x, n):
    return np.sqrt(2/L) * np.sin(n * np.pi * (x + L/2) / L)

'''We plot the difference between the numerical solution and the analytical solution'''
plt.figure(figsize=(15, 9))
plt.plot(x, psi_puit_infini(x, 1) - v[:, 0], label="Analytical p = 1")
plt.xlabel("x (nm)")
plt.ylabel("ψ(x)")
plt.title("Difference between the numerical and analytical solutions for the infinite potential well, p = 1, n = 1000")
plt.legend()
plt.savefig("PartieI_puit_infini_n1000.png")
# plt.show()
plt.close()

'''We define the simulation parameters'''
n = 10000
x = np.linspace(-L/2, L/2, n)

'''Numerical solution for the infinite potential well'''
x, w, v = resol(L, n, puit_de_potentiel, Norm=True)

'''We plot the difference between the numerical solution and the analytical solution'''
plt.figure(figsize=(15, 9))
plt.plot(x, np.abs(psi_puit_infini(x, 1) - v[:, 0]), label="Analytical p = 1")
plt.xlabel("x (nm)")
plt.ylabel("ψ(x)")
plt.title("Difference between the numerical and analytical solutions for the infinite potential well, n = 10000")
plt.legend()
# plt.savefig("Infinite_Potential_Well_n10000.png")
# plt.show()
plt.close()

'''We follow the same reasoning for the harmonic potential'''

'''We define the simulation parameters'''
L = 10
n = 1000
x = np.linspace(-L/2, L/2, n)

'''Numerical solution for the harmonic potential'''
x, w, v = resol(L, n, potentiel_harmonique, Norm=True)

'''Analytical solution for the harmonic potential'''
def psi_harmonique(x):
    return ((2**-1/8) * (np.pi**-1/4)) * np.exp(-(x**2) / (2 * np.sqrt(2)))

'''We plot the difference between the numerical solution and the analytical solution'''
plt.figure(figsize=(15, 9))
plt.plot(x, np.abs(normalize(psi_harmonique(x), L/n) - v[:, 0]), label="Analytical p = 1")
plt.xlabel("x (nm)")
plt.ylabel("ψ(x)")
plt.title("Difference between the numerical and analytical solutions for the harmonic potential, n = 1000")
plt.legend()
plt.savefig("PartieI_potentiel_harmonique_n1000.png")
# plt.show()
plt.close()

'''We define the simulation parameters'''
n = 10000
x = np.linspace(-L/2, L/2, n)

'''Numerical solution for the harmonic potential'''
x, w, v = resol(L, n, potentiel_harmonique, Norm=True)

'''We plot the difference between the numerical solution and the analytical solution'''
plt.figure(figsize=(15, 9))
plt.plot(x, np.abs(normalize(psi_harmonique(x), L/n) - v[:, 0]), label="Analytical p = 1")
plt.xlabel("x (nm)")
plt.ylabel("ψ(x)")
plt.title("Difference between the numerical and analytical solutions for the harmonic potential, n = 10000")
plt.legend()
plt.savefig("PartieI_potentiel_harmonique_n10000.png")
# plt.show()
plt.close()
