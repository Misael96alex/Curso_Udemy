# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:08:51 2022

@author: Alexander
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("../datasets/Customer Churn Model.txt")
len(data)

## -----  Dividimos utilizando la distribuicon normal

a= np.random.randn(len(data))
fig1=plt.hist(a)

chek = (a<0.8)
fig2=plt.hist(chek.astype(int))
fig2

training = data[chek]
testing = data[~chek]

print("Distribucion Normal ",len(training),len(testing))

## -----  con la libreria Sklearn

from sklearn.model_selection import train_test_split

test, train = train_test_split(data, test_size = 0.8 ) 
print("Libreria Sklearn:",len(train),len(test))

## -----  usando una funicon de Shuffe

import sklearn

data.head()

data2=sklearn.utils.shuffle(data)

cut_id=int(0.75*len(data))
train_data=data2[:cut_id]
test_data=data2[cut_id+1:]
print("Funcion Shuffe",len(train_data),len(test_data))


