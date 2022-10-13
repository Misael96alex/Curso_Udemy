# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:34:07 2022

@author: majuchan
"""

# La Simulacion de Monte Carlo

# Generamos dos numeros aleatorios x e y entre 0 y 1

# Calcularemos raiz(x*x*+y*y)

# Si el valor es inferioa 1 estamos dentro del circulo
# Si el valor es superor a 1 estamos fuera del curculo

# Calculamos el numero de veces que estan dentro del circulo y lo dividimos entre
# el numero total de intentos para obtener una aproximacion de la probabilidad de caer dentro del circulo

#usamos dicha probabilidad para calcular una aproximacion del numero PI

#Repetimos el experimento unnumero suficiente de veces para obtener diferentes aproximaciones de PI

# Calculamos el promedio de los 1000 experimentos anteriores para dar un valor final de PI

import numpy as np
import matplotlib.pyplot as plt

def pi_montecarlo (n, n_exp):
    pi_avg = 0
    pi_value_list = []
    for i in range(n_exp):
        value=0
        x=np.random.uniform(0,1,n).tolist()
        y=np.random.uniform(0,1,n).tolist()
        for j in range(n):
            z=np.sqrt(x[j]*x[j]+y[j]*y[j])
            if z<=1:
                value+=1
        float_value=float(value)
        pi_value= float_value*4 /n
        pi_value_list.append(pi_value)
        pi_avg+=pi_value

        pi=pi_avg/n_exp
        fig=plt.plot(pi_value_list)

    return(pi,fig)        
    
pi_montecarlo(10000, 200)
