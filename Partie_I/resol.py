import numpy as np
from scipy.linalg import eigh_tridiagonal
import matplotlib.pyplot as plt

#On sait que la solution de l'equation d'onde doit respecter des conditions de normalisation
#Elle doit etre de carré sommable égale à 1
#Ayant discrétisé l'espace, on traduit la condition de normalisation avec la méthode suivante  :
def normalize(m,delta_x):
    m /= np.linalg.norm(m, axis=0) # Normaliser les colonnes
    m /= np.sqrt(delta_x) # diviser par 1/sqrt(dx)
    return m



def resol(L,n, potentiel, Norm = False) : 
    delta  = L/n
    x = np.linspace(-L/2, L/2, n)
    d = potentiel(x) + 2/(delta**2) # diagonale principale de la matrice
    e = np.ones(n-1)*(-1/(delta**2)) # diagonale juste au-dessus
    w, v = eigh_tridiagonal(d,e)
    if Norm :
        v = normalize(v, delta)
    return x, w, v

