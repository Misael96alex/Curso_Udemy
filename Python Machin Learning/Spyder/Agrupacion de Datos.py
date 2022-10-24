# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:14:51 2022

@author: Alexander
"""

# Agregacion de Datos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gender= ["Male", "Female"]
income=["Poor", "Middle Class", "Rich"]

n=500

gender_data=[]
income_data=[]

for i in range(0,500):
    gender_data.append(np.random.choice(gender))
    income_data.append(np.random.choice(income))

gender_data[1:10]

#N(m,s)  --  m+s*Z
height = 160+30*np.random.randn(n)
weight = 65 + 25*np.random.randn(n)
age= 30+12 * np.random.randn(n)
income= 18000+3500*np.random.randn(n)

data= pd.DataFrame(
    {
     'Gender':gender_data,
     'Economic Status':income_data,
     'Height': height,
     'Weight': weight,
     'Age': age,
     'Income':income
     }
    )


## Agrupacion de Datos

gruper_gender = data.groupby("Gender")
double_gruper= data.groupby(["Gender","Economic Status"])
gruper_gender.groups

for names, groups in gruper_gender:
    print(names)
    print(groups)

    
gruper_gender.sum()
double_gruper.sum()

double_gruper.mean()

double_gruper.size()

double_gruper.aggregate(
    {
     'Age': np.sum,
     'Income': np.mean,
     'Height': np.std
     }
    )


double_gruper.aggregate(
    {
     'Age': np.mean,
     'Income': np.mean,
     'Height': lambda h : np.mean(h)/np.std(h)
     }
    )


double_gruper.aggregate({np.sum, np.mean})

double_gruper.aggregate({lambda x: np.mean(x)/np.std(x)})

# filtrado de datos

double_gruper["Age"].filter(lambda x: x.sum()>2400)

zscore=lambda x : (x- x.mean()/x.std())

z_group=double_gruper.transform(zscore)

plt.hist(z_group['Age'])

fill_na_mean = lambda x : x.fillna(x.mean())

double_gruper.transform(fill_na_mean)

# ordenar el dataset

data.sort_values(["Age"])

