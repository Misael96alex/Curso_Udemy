# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 22:52:55 2022

@author: Alexander
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_ads= pd.read_csv("../datasets/ads/Advertising.csv")

#se usa para construir la funcion
#data_ads["corrnumTV"]=(data_ads["TV"]-np.mean(data_ads["TV"]))*(data_ads["Sales"]-np.mean(data_ads["Sales"]))
#data_ads["corr1TV"]=pow((data_ads["TV"]-np.mean(data_ads["TV"])),2)
#data_ads["corr2TV"]=pow((data_ads["Sales"]-np.mean(data_ads["Sales"])),2)
#correlacionTV = sum(data_ads["corrnumTV"])/pow((sum(data_ads["corr1TV"]))*(sum(data_ads["corr2TV"])),(1/2))

def corr_coeff(df, var1, var2):
    numerador=sum((data_ads[var1]-np.mean(data_ads[var1]))*(data_ads[var2]-np.mean(data_ads[var2])))
    denominadorf1=sum(pow((data_ads[var1]-np.mean(data_ads[var1])),2))
    denominadorf2=sum(pow((data_ads[var2]-np.mean(data_ads[var2])),2))
    coef=numerador/pow(denominadorf1*denominadorf2,(1/2))
    return coef

correlacionTV=corr_coeff(data_ads,"TV","Sales")
correlacionRadio=corr_coeff(data_ads,"Radio","Sales")
correlacionNews=corr_coeff(data_ads,"Newspaper","Sales")

cols=data_ads.columns.values

for x in cols:
    for y in cols:
        print(x + ", "+ y + " : "+str(corr_coeff(data_ads,x,y)))
        
grafo1=plt.plot(data_ads["TV"],data_ads["Sales"],"ro")
grafo1=plt.title("Gasto en TV vs Ventas del Producto") 

grafo2=plt.plot(data_ads["Radio"],data_ads["Sales"],"go")
grafo2=plt.title("Gasto en Radio vs Ventas del Producto") 

grafo3=plt.plot(data_ads["Newspaper"],data_ads["Sales"],"bo")
grafo3=plt.title("Gasto en Newspaper vs Ventas del Producto")   

data_ads.corr()

plt.matshow(data_ads.corr())
plt.imshow(data_ads.corr())


     