import numpy as np
from scipy.linalg import eigh_tridiagonal

#Méthode d'Euler
def euler( f, a, b, N, y0, params = None, Norm = True):
    h = (b-a)/N
    y = np.zeros((N, np.size(y0)), dtype=complex)
    y[0] = y0
    i = 0
    while(i< N-1): 
        y[i+1] = y[i] + h*(f( y[i], params))
        i = i +1
        if Norm : y[i] /= np.sqrt(sum(np.abs(y[i])**2)*params[0])
    return y #retourne un tableau des N valeurs prise par y avec un pas h



#On sait que la solution de l'equation d'onde doit respecter des conditions de normalisation
#Elle doit etre de carré sommable égale à 1
#Ayant discrétisé l'espace, on traduit la condition de normalisation avec la méthode suivante  :


def normalize(m,delta_x):
    m /= np.linalg.norm(m, axis=0) # normaliser les colonnes
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


