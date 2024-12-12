'''Dans ce programme on souhaite apprécier la résolution numérique de l'équation de Schrödinger.
On ne discutera pas ici de la précision de la résolution numérique mais on cherchera plutôt à retrouver les résultats habituels.
A savoir : La quantification de l'énergie et les formes souvent sinusoidales des fonctions d'onde.
Pour cela on tracera une dizaines de fonctions d'ondes espacées par leurs énergies propres pour des potentiels usuels.'''

import matplotlib
matplotlib.use('Agg')  # Utilise un backend non interactif (pour enregistrer des figures)

'''On commence par importer les modules nécessaires'''
import matplotlib.pyplot as plt
from resol import * 
from potentiels import *


'''On définit les paramètres de la simulation'''''
L = 10
n = 1000

'''Résolution numérique d'un puit de potentiel'''
x, w,v = resol(L,n,puit_de_potentiel, Norm = True)



import matplotlib.pyplot as plt
import numpy as np

# Plot the first 10 wave functions
plt.figure(figsize=(15,9))
for p in range(10):
    plt.plot(x, ((v[:, p])**2) * np.abs(w[p]) + w[p], label=f"Probability of presence for p = {p}, E = {w[p]:.2f} eV")
    plt.plot(x, x*0 + w[p], label=f"Eigenenergy = {w[p]:.2f} eV")
plt.xlabel("x (nm)")
plt.ylabel("P(x)")
plt.title("Probability of Presence in a Potential Well")
plt.legend()
plt.savefig("Puit_de_potentiel.png")
plt.close()

# Numerical solution for a potential barrier
x, w, v = resol(L, n, barrière_de_potentiel, Norm=True)

# Plot the first 10 wave functions
plt.figure(figsize=(15,9))
for p in range(10):
    plt.plot(x, ((v[:, p])**2) * np.abs(w[p]) + w[p], label=f"Probability of presence for p = {p}, E = {w[p]:.2f} eV")
    plt.plot(x, x*0 + w[p], label=f"Eigenenergy = {w[p]:.2f} eV")
plt.xlabel("x (nm)")
plt.ylabel("P(x)")
plt.title("Probability of Presence in a Potential Barrier")
plt.legend()
plt.savefig("Barrière_de_potentiel.png")
plt.close()

# Numerical solution for a damped potential barrier
x, w, v = resol(L, n, barrière_de_potentiel_amortie, Norm=True)

# Plot the first 10 wave functions
plt.figure(figsize=(15,9))
for p in range(10):
    plt.plot(x, ((v[:, p])**2) * np.abs(w[p]) + w[p], label=f"Probability of presence for p = {p}, E = {w[p]:.2f} eV")
    plt.plot(x, x*0 + w[p], label=f"Eigenenergy = {w[p]:.2f} eV")
plt.xlabel("x (nm)")
plt.ylabel("ρ(x)")
plt.title("Probability Density of Presence in a Damped Potential Barrier")
plt.legend()
plt.savefig("Barrière_de_potentiel_amortie.png")
plt.close()

# Numerical solution for a double potential well
x, w, v = resol(L, n, double_puits_de_potentiel, Norm=True)

# Plot the first 10 wave functions
plt.figure(figsize=(15,9))
for p in range(10):
    plt.plot(x, ((v[:, p])**2) * np.abs(w[p]) + w[p], label=f"Probability of presence for p = {p}, E = {w[p]:.2f} eV")
    plt.plot(x, x*0 + w[p], label=f"Eigenenergy = {w[p]:.2f} eV")
plt.xlabel("x (nm)")
plt.ylabel("ρ(x)")
plt.title("Probability Density of Presence in a Double Potential Well")
plt.legend()
plt.savefig("Double_puits_de_potentiel.png")
plt.close()

# Numerical solution for a periodic potential barrier
x, w, v = resol(L, n, potentiel_periodique, Norm=True)

# Plot the first 10 wave functions
plt.figure(figsize=(15,9))
for p in range(10):
    plt.plot(x, ((v[:, p])**2) * np.abs(w[p]) + w[p], label=f"Probability of presence for p = {p}, E = {w[p]:.2f} eV")
    plt.plot(x, x*0 + w[p], label=f"Eigenenergy = {w[p]:.2f} eV")
plt.xlabel("x (nm)")
plt.ylabel("ρ(x)")
plt.title("Probability Density of Presence in a Periodic Potential")
plt.legend()
plt.savefig("Potentiel_périodique.png")
plt.close()

# Numerical solution for an electronic potential
x, w, v = resol(L, n, potentiel_electronique, Norm=True)

# Plot the first 10 wave functions
plt.figure(figsize=(15,9))
for p in range(10):
    plt.plot(x, ((v[:, p])**2) * np.abs(w[p]) + w[p], label=f"Numerical solution for p = {p}, E = {w[p]:.2f} eV")
    plt.plot(x, x*0 + w[p], label=f"Eigenenergy = {w[p]:.2f} eV")
plt.xlabel("x (nm)")
plt.ylabel("ρ(x)")
plt.title("Probability Density of Presence in an Electronic Potential")
plt.legend()
plt.savefig("Potentiel_electronique.png")
plt.close()
