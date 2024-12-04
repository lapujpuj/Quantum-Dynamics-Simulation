# -*- coding: utf-8 -*- 

import numpy as np
from numba import njit


def rk4(dt, y, deriv,params):
    """
      /*-----------------------------------------
      sous programme de resolution d'equations
      differentielles du premier ordre par
      la methode de Runge-Kutta d'ordre 4
      x = abscisse, une valeur scalaire, par exemple le temps
      dx = pas, par exemple le pas de temps
      y = valeurs des fonctions au temps t(i), c'est un tableau numpy de taille n
      avec n le nombre d'équations différentielles du 1er ordre
      
      rk4 renvoie les nouvelles valeurs de y pour t(i+1)
      
      deriv = variable contenant le nom du
      sous-programme qui calcule les derivees
      deriv doit avoir trois arguments: deriv(x,y,params) et renvoyer 
      un tableau numpy dy de taille n 
      ----------------------------------------*/
    """
    #  /* d1, d2, d3, d4 = estimations des derivees
    #    yp = estimations intermediaires des fonctions */  
    #        #         /* demi-pas */
    d1 = deriv(y,params)   #       /* 1ere estimation */          
    yp = y + d1*dt
    #    for  i in range(n):
    #        yp[i] = y[i] + d1[i]*ddx
    d2 = deriv(yp,params)     #/* 2eme estimat. (1/2 pas) */
    yp = y + d2*dt    
    d3 = deriv(yp,params)  #/* 3eme estimat. (1/2 pas) */
    yp = y + d3*dt    
    d4 = deriv(yp,params)     #  /* 4eme estimat. (1 pas) */
    #/* estimation de y pour le pas suivant en utilisant
    #  une moyenne ponderee des derivees en remarquant
    #  que : 1/6 + 1/3 + 1/3 + 1/6 = 1 */
    res = y + dt*( d1 + 2*d2 + 2*d3 + d4 )/6 
    return res


#Methode qui retourne un tableau de N valeurs de X(t) avec X(t) la solution de l'équation différentielle en utlisant la méthode de Runge-Kutta d'ordre 4
def RK4(f, a, b, N, y0, params):
    dt = (b-a)/N
    y = np.zeros((N, np.size(y0)), dtype = complex)
    y[0] = y0
    i = 0
    while(i< N-2):
        y[i+1] = rk4(dt, y[i], f, params)
        i = i +1
        y[i] /= np.sqrt(np.sum(abs(y[i])**2)*params[0])
    return y