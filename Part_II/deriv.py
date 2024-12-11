import numpy as np 

def deriv(y,params ): # params = [delta_x, V]
    dy = np.zeros(np.size(y), dtype= complex)
    for k in range(1, np.size(y)-1): #Comme la particule est confiné on peut imposé comme condition limite que la sa probabilité de présence est nulle au bord   
            dy[k]= complex(0,(1/(2*(params[0]**2)))*(y[k+1] + y[k-1] - 2*y[k]) + params[1][k]*y[k])          
            #dy[k]= complex(0,(1/(params[0]**2))*(y[k+1] + y[k-1] - 2*y[k]) + 2*params[1][k]*y[k])
    return dy
