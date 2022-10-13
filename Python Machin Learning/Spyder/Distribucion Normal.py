# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:15:14 2022

@author: majuchan
"""

# FUNCIONES DE DISTRIBUCION DE PROBABILIDADES
# Distribucion Nomral

import numpy as np
import matplotlib.pyplot as plt

data=np.random.randn(10000)
x= range(1,101)

#matplotlib in line

#plt.plot(x,data)

#plt.hist(data)

#plt.plot(x,sorted(data))

mu=5.5

sd=2.5
z_10000=np.random.randn(10000)
data1= mu + sd * z_10000 #z=(X-mu)/sd  ->  N(0,1)m X=mu + sd*Z
plt.hist(data1)


data2=np.random.randn(2,4)
data2
