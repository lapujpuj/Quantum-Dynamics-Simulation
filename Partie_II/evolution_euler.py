'''Dans ce programme, on résout l'équation de Schrödinger par la méthode de Runge Kutta d'ordre 4
La dérivé temporelle de la fonction d'onde est contenu dans l'Hamiltonien
En discrétisant l'espace et le temps, on obtient une équation différentielle
La dérivé temporelle de la fonction au rend n+1 est calculé par la fonction deriv
Cette méthode etant plus performante, on calculera aussi l'evolution de la probabilité de présence d'une paquet d'onde gaussien'''

'''On importe les bibliothèques nécessaires'''''

from resol import *
from matplotlib.animation import FuncAnimation
from euler import * 
from potentiels import * 
from deriv import *

import matplotlib
matplotlib.use('Agg')  # Utilise un backend non interactif (pour enregistrer des figures)


'''On définit les variables nécessaires'''
n_espace, n_temps, debut, fin, L= 100, 100000, 0, 10,  10
#x = np.linspace(-L/2, L/2, n_espace)
sigma,k0 = 0, 0

x,w, v= resol(L,n_espace, puit_de_potentiel, Norm = True)
y1 = v[:, 7]
y2 = (v[:,7]  +v[:,14] + v[:, 21])/np.sqrt(3)
params = [L/n_espace, puit_de_potentiel(x)] 


res = euler(deriv, debut, fin, n_temps, y1,params)

'''On trace l'evolution de l'erreur sur l'etat stationnaire pour plusieurs valeurs de delta_t'''
temps1 =np.linspace(debut, fin, n_temps)
error1 = np.zeros(n_temps)
for i in range(n_temps): error1[i] = np.sum(np.abs(res[i]- res[0]))
error1 *= fin/n_temps


'''On définit les variables nécessaires'''
n_temps = 1000

x,w, v= resol(L,n_espace, puit_de_potentiel, Norm = True)
y1 = v[:, 7]
params = [L/n_espace, puit_de_potentiel(x)] 
res = euler(deriv, debut, fin, n_temps, y1, params)

'''On trace l'evolution de l'erreur sur l'etat stationnaire'''
temps2 = np.linspace(debut, fin, n_temps)
error2 = np.zeros(n_temps)
for i in range(n_temps): error2[i] = np.sum(np.abs(res[i]- res[0]))
error2 *= fin/n_temps



'''On définit les variables nécessaires'''
n_temps = 100

x,w, v= resol(L,n_espace, puit_de_potentiel, Norm = True)
y1 = v[:, 7]
params = [L/n_espace, puit_de_potentiel(x)] 
res = euler(deriv, debut, fin, n_temps, y1, params )

'''On trace l'evolution de l'erreur sur l'etat stationnaire'''
error3 = np.zeros(n_temps)
for i in range(n_temps): error3[i] = np.sum(np.abs(res[i]- res[0]))
error3 *= fin/n_temps
temps3 = np.linspace(debut, fin, n_temps)



plt.figure(figsize=(16,5))
plt.subplot(1,3,1)
plt.plot(temps3, error3)
plt.xlabel('x')
plt.ylabel('erreur de totale de la solution')
plt.title('Evolution_euler_delta_t=1e-2')
plt.subplot(1,3,2)
plt.plot(temps2, error2)
plt.xlabel('x')
plt.ylabel('erreur de totale de la solution')
plt.title('Evolution_euler_delta_t=1e-3')
plt.subplot(1,3,3)
plt.plot(temps1, error1)
plt.xlabel('x')
plt.ylabel('erreur de totale de la solution')
plt.title('Evolution_euler_delta_t=1e-4')
plt.savefig('Euler_Precision')
plt.show()
plt.close()
