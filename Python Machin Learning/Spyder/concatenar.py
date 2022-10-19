# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:38:40 2022

@author: majuchan
"""

import pandas as pd

# DESCARGO LAS DATAS DEL REPOSITORIO DE GIT

# red_Wine = pd.read_csv("https://raw.githubusercontent.com/joanby/python-ml-course/master/datasets/wine/winequality-red.csv", sep = ";")
# red_Wine.head()
# red_Wine.to_csv("Vino_rojo.csv")

# white_wine = pd.read_csv("https://raw.githubusercontent.com/joanby/python-ml-course/master/datasets/wine/winequality-white.csv", sep = ";")
# white_wine.head()
# white_wine.to_csv("Vino_blanco.csv")

#Uso el archivo descargado 
red_wine = pd.read_csv("../datasets/Vino_rojo.csv")
red_wine.head()
red_wine.columns.values
red_wine.shape

white_wine = pd.read_csv("../datasets/Vino_blanco.csv")
white_wine.head()
white_wine.columns.values
white_wine.shape


""" 
concatenar horizontalmente, uno debado de otro
- axis = 0 denota el eje horizontal
- axis = 1 denota el eje vertical

"""

wine_data = pd.concat([red_wine,white_wine], axis = 0)

data1=wine_data.head(10)
data2=wine_data[300:310]
data3=wine_data.tail(10)

wine_scramble=pd.concat([data1,data2,data3], axis = 0)


