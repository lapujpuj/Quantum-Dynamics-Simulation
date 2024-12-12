import numpy as np
import math


def barrière_de_potentiel(x, d = 5, U0 = 10000000):
    res = np.zeros(np.size(x))
    for i in range(np.size(x)):
        if x[i] >= -d/2 and x[i] <= d/2:
            res[i] = U0
    return res

def barrière_de_potentiel_amortie(x, d = 5, U0 = 4):
    res = np.zeros(np.size(x))
    for i in range(np.size(x)):
        if x[i] >= -d/2 and x[i] <= d/2:
            res[i] = U0*((np.cos(2*np.pi*x[i]/d))**2)
    return res


def double_puits_de_potentiel(x, a = 5):
    res = np.zeros(np.size(x))
    for i in range(np.size(x)):
        res[i] = a*(x[i]-1)*(x[i]+1)*(x[i]-1)*(x[i]+1)
    return res

def potentiel_periodique(x,U0 = 10, d = 5):
    return U0*(np.cos(2*np.pi*x/d))**2

def potentiel_electronique(x, V0 = 3e2, n =5):
    pos_atomes = np.linspace(-5,5,n)
    p = 0.5
    V = 0
    for i in pos_atomes : V += -V0*np.exp(-np.abs(x-i)/p)
    return V

def puit_de_potentiel(x):
    return np.zeros(np.size(x))

def potentiel_harmonique(x, k = 1e3/25):
    return 0.5*k*(x**2)

def gauss(x, x0, sigma, k0, A =1):
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-((x-x0)**2)/(2*sigma**2))*np.exp(1j*k0*x)

def potentiel_puit(x, d = 5, U0 = 1000000):
    res = np.ones(np.size(x))*U0
    for i in range(np.size(x)):
        if x[i] >= -d/2 and x[i] <= d/2:
            res[i] = 0
    return res

