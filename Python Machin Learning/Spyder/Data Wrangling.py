# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:44:50 2022

@author: Alexander
"""

# Data Wrangling - La cirugia de los datos
import pandas as pd

#la ruta de la data
titanicgit = "https://raw.githubusercontent.com/joanby/python-ml-course/master/datasets/customer-churn-model/Customer%20Churn%20Model.txt"
data = pd.read_csv(titanicgit)
data.head()

# Crear un subconjunto de datos
account_lenht = data["Account Length"]
account_lenht.head()

subset = data[["Account Length","Phone","Eve Charge","Day Calls"]]
subset.head()

type(subset),type(account_lenht)

desired_columns=["Account Length","Phone","Eve Charge","Day Calls"]
subset2 = data[desired_columns]
subset2.head()

data2=data[data["State"]== "NY"]
data2.head(10)

data7=data.iloc[1:51, 3:6]
data7.shape

#la i es de indice
data8=data.iloc[1:10,[2,5,7]]

#no hay i, es por nombre de columna
data8=data.loc[[1,5,8,10],["Area Code","Day Mins"]]

# agregar columnas

data["Total llamadas"]=data["Day Calls"]+data["Night Calls"]+data["Eve Calls"]

data["Total Minutos"]=data["Day Mins"]+data["Night Mins"]+data["Eve Mins"]


