'''Dans ce programme on souhaite apprécier la résolution numérique de l'équation de Schrödinger.
On ne discutera pas ici de la précision de la résolution numérique mais on cherchera plutôt à retrouver les résultats habituels.
A savoir : La quantification de l'énergie et les formes souvent sinusoidales des fonctions d'onde.
Pour cela on tracera une dizaines de fonctions d'ondes espacées par leurs énergies propres pour des potentiels usuels.'''

'''On commence par importer les modules nécessaires'''
import matplotlib.pyplot as plt
from resol import * 
from potentiels import *

'''On définit les paramètres de la simulation'''''
L = 10
n = 1000

'''Résolution numérique d'un puit de potentiel'''
x, w,v = resol(L,n,puit_de_potentiel, Norm = True)

'''On trace les 10 premières fonctions d'onde'''
plt.figure()
for p in range(10): 
    plt.plot(x, ((v[:,p])**2)*np.abs(w[p])+ w[p] )#, label = "Probalitité de présence pour p = " + str(p) + " E = " + str(w[p]))
    plt.plot(x, x*0 + w[p])#, label = "Energie propre= " + str(p) + " E = " + str(w[p]))
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Probabilité de présence dans un puit de potentiel")
plt.legend()
plt.savefig("Puit_de_potentiel.png")
#plt.show()
plt.close()

'''Résolution numérique d'une barrière de potentiel'''
x, w,v = resol(L,n,barrière_de_potentiel, Norm = True)

'''On trace les 10 premières fonctions d'onde'''
plt.figure()
for p in range(10): 
    plt.plot(x, ((v[:,p])**2)*np.abs(w[p])+ w[p] )#, label = "Probalitité de présence pour p = " + str(p) + " E = " + str(w[p]))
    plt.plot(x, x*0 + w[p])#, label = "Energie propre= " + str(p) + " E = " + str(w[p]))
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Probabilité de présence dans une barrière de potentiel")
plt.legend()
plt.savefig("Barrière_de_potentiel.png")
#plt.show()
plt.close()


'''Résolution numérique d'une barrière de potentiel amortie'''
x, w,v = resol(L,n,barrière_de_potentiel_amortie, Norm = True)

'''On trace les 10 premières fonctions d'onde'''
plt.figure()
for p in range(10): 
    plt.plot(x, ((v[:,p])**2)*np.abs(w[p])+ w[p] )#, label = "Probalitité de présence pour p = " + str(p) + " E = " + str(w[p]))
    plt.plot(x, x*0 + w[p])#, label = "Energie propre= " + str(p) + " E = " + str(w[p]))
plt.xlabel("x")
plt.ylabel("ρ(x)")
plt.title("Densité de probabilité de présence dans une barrière de potentiel amortie")
plt.legend()
plt.savefig("Barrière_de_potentiel_amortie.png")
#plt.show()
plt.close()

'''Résolution numérique du double puits de potentiel'''
x, w,v = resol(L,n,double_puits_de_potentiel, Norm = True)

'''On trace les 10 premières fonctions d'onde'''
plt.figure()
for p in range(10): 
    plt.plot(x, ((v[:,p])**2)*np.abs(w[p])+ w[p] )#, label = "Probalitité de présence pour p = " + str(p) + " E = " + str(w[p]))
    plt.plot(x, x*0 + w[p])#, label = "Energie propre= " + str(p) + " E = " + str(w[p]))
plt.xlabel("x")
plt.ylabel("ρ(x)")
plt.title("Densité de probabilité de présence dans un double puits de potentiel")
plt.legend()
plt.savefig("Double_puits_de_potentiel.png")
#plt.show()
plt.close()

'''Résolution numérique du puit d'une barrière de potentiel périodique'''
x, w,v = resol(L,n,potentiel_periodique, Norm = True)

'''On trace les 10 premières fonctions d'onde'''
plt.figure()
for p in range(10): 
    plt.plot(x, ((v[:,p])**2)*np.abs(w[p])+ w[p] )#, label = "Probalitité de présence pour p = " + str(p) + " E = " + str(w[p]))
    plt.plot(x, x*0 + w[p])#, label = "Energie propre= " + str(p) + " E = " + str(w[p]))
plt.xlabel("x")
plt.ylabel("ρ(x)")
plt.title("Densité de probabilité de présence dans un potentiel périodique")
plt.legend()
plt.savefig("Potentiel_périodique.png")
#plt.show()
plt.close()


'''Résolution numérique d'un potentiel electronique'''
x, w,v = resol(L,n,potentiel_electronique, Norm = True)

'''On trace les 10 premières fonctions d'onde'''
plt.figure()
for p in range(10): 
    plt.plot(x, ((v[:,p])**2)*np.abs(w[p])+ w[p] )#, label = "Solution numerique p = " + str(p) + " E = " + str(w[p]))
    plt.plot(x, x*0 + w[p])#, label = "Energie propre= " + str(p) + " E = " + str(w[p]))
plt.xlabel("x")
plt.ylabel("ρ(x)")
plt.title("Densité de probabilité de présence dans un potentiel electronique")
plt.legend()
plt.savefig("Potentiel_electronique.png")
#plt.show()
plt.close()