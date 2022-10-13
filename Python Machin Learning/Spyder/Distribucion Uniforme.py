# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:23:37 2022

@author: majuchan
"""

# FUNCIONES DE DISTRIBUCION DE PROBABILIDADES
# Distribucion Uniforme

import numpy as np
import matplotlib.pyplot as plt

a=1
b=100
n=1000000
data= np.random.uniform(a,b,n)


# %matplotlib in line
plt.hist(data)
