'''Dans ce programme, on résout l'équation de Schrödinger par la méthode de Runge Kutta d'ordre 4
La dérivé temporelle de la fonction d'onde est contenu dans l'Hamiltonien
En discrétisant l'espace et le temps, on obtient une équation différentielle
La dérivé temporelle de la fonction au rend n+1 est calculé par la fonction deriv
Cette méthode etant plus performante, on calculera aussi l'evolution de la probabilité de présence d'une paquet d'onde gaussien'''

'''On importe les bibliothèques nécessaires'''''

from resol import *
from matplotlib.animation import FuncAnimation
from rk4 import * 
from potentiels import * 
from deriv import *
import matplotlib.animation as animation

'''On définit les variables nécessaires'''
n_espace, n_temps, debut, fin, L= 100,10000, 0, 1,  10
x = np.linspace(-L/2, L/2, n_espace)
sigma,k0, x0 = 0.5, 1e10, 0



#x,w, v= resol(L,n_espace, double_puits_de_potentiel, Norm = True)
y1 = gauss(x, x0, sigma, k0)
params = [L/n_espace, potentiel_harmonique(x)] 
res1 = RK4(deriv, debut, fin, n_temps, y1, params = params)


'''
def animate(i):
    etat1.set_data(x,abs(res1[i*10])**2)
    potentiel.set_data(x, potentiel_harmonique(x)*1e-3)

    return  etat1, potentiel,

fig=plt.figure()
plt.xlim(-5, 5)
plt.ylim(0, 1)
etat1 ,potentiel = plt.plot([], [],  [], [])
anim = FuncAnimation(fig,animate,blit=False, interval = 1)
plt.show()
'''


'''Je trace la valeur moyenne de la position dans le temps'''

plt.figure()
for i in range(10):
    plt.subplot(2,5, i +1)
    plt.plot(x, res1[int(i*(n_temps/10))])
    plt.plot(x, potentiel_harmonique(x)*1e-3)
plt.savefig("Dynamique_Paquet_Onde_Potentiel_Harmonique.png")
plt.show()
plt.close()

pos_moyenne = []
for i in range(n_temps) :
    pos_moyenne += [np.sum((np.abs(res1[i])**2) * x)]
plt.figure()
plt.plot(range(n_temps), pos_moyenne)
#plt.savefig("Position_Moyenne_Paquet_Onde_Potentiel_Harmonique.png")
plt.show()
plt.plot()