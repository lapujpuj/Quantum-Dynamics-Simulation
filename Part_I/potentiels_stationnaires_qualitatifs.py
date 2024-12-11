'''Dans ce programme on discutera de la précision la résolution numérique
On discutera en particulier des cas du puit de potentiel infini et du du potentiel harmonique,
qui sont les cas les plus simples et les plus faciles à résoudre analytiquement.
On mettra en évidence les effets de la discrétisation dans ces cas'''

'''On commence par importer les modules nécessaires'''
import numpy as np
import matplotlib.pyplot as plt
from resol import *
from potentiels import *

'''On définit les paramètres de la simulation'''
L = 10
n = 1000
x = np.linspace(-L/2, L/2, n)

'''Résolution numérique du puit de potentiel infini'''
x, w,v = resol(L,n,puit_de_potentiel, Norm = True)

'''Résolution analytique du puit de potentiel infini'''
def psi_puit_infini(x, n):
    return np.sqrt(2/L)*np.sin(n*np.pi*(x+L/2)/L)


'''On trace la différence entre la solution numérique et la solution analytique'''
plt.figure()
plt.plot(x, psi_puit_infini(x, 1) - v[:,0], label = "Analytique p = " + str(1))
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.title("Différence entre la solution numérique et la solution analytique du puit de potentiel infini , p = 1, n =1000")
plt.legend()
plt.savefig("PartieI_puit_infini_n1000.png")
#plt.show()
plt.close()

'''On définit les paramètres de la simulation'''
n = 10000
x = np.linspace(-L/2, L/2, n)

'''Résolution numérique du puit de potentiel infini'''
x, w,v = resol(L,n,puit_de_potentiel, Norm = True)

'''On trace la différence entre la solution numérique et la solution analytique'''
plt.figure()
plt.plot(x,np.abs( psi_puit_infini(x, 1) - v[:,0]), label = "Analytique p = " + str(1))
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.title("Différence entre la solution numérique et la solution analytique du puit de potentiel infini")
plt.legend()
#plt.savefig("PartieI_puit_infini_n10000.png")
#plt.show()
plt.close()

'''On suit le même raisonnement pour le potentiel harmonique'''

'''On définit les paramètres de la simulation'''
L = 10
n = 1000
x = np.linspace(-L/2, L/2, n)

'''Résolution numérique du potentiel harmonique'''
x, w,v = resol(L,n,potentiel_harmonique, Norm = True)

'''Résolution analytique du potentiel harmonique'''

def psi_harmonique(x):
    return ((2**-1/8) * (np.pi**-1/4))*np.exp(-(x**2)/(2*np.sqrt(2)))


'''On trace la différence entre la solution numérique et la solution analytique'''
plt.figure()
plt.plot(x, np.abs(normalize(psi_harmonique(x), L/n) - v[:,0]), label = "Analytique p = " + str(1))
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.title("Différence entre la solution numérique et la solution analytique du potentiel harmonique")
plt.legend()
plt.savefig("PartieI_potentiel_harmonique_n1000.png")
#plt.show()
plt.close()

'''On définit les paramètres de la simulation'''
n = 10000
x = np.linspace(-L/2, L/2, n)

'''Résolution numérique du potentiel harmonique'''
x, w,v = resol(L,n,potentiel_harmonique, Norm = True)

'''On trace la différence entre la solution numérique et la solution analytique'''
plt.figure()
plt.plot(x, np.abs(normalize(psi_harmonique(x), L/n) - v[:,0]), label = "Analytique p = " + str(1))
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.title("Différence entre la solution numérique et la solution analytique du potentiel harmonique")
plt.legend()
plt.savefig("PartieI_potentiel_harmonique_n10000.png")
#plt.show()
plt.close()
