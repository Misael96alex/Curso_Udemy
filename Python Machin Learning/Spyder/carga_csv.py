# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 22:46:55 2022

@author: Alexander
"""
# Carga de datos a travez de la funcion read_csv

import pandas as pd
# import os

#url
titaniccsv= "../datasets/titanic3.csv"
titanicxls= "../datasets/titanic3.xls"
titanicxlsx= "../datasets/titanic3.xlsx"
titanicgit = "https://raw.githubusercontent.com/joanby/python-ml-course/master/datasets/titanic/titanic3.csv"

#lecturas
data1 = pd.read_csv(titaniccsv)
data2 = pd.read_excel(titanicxls, "titanic3")
data3 = pd.read_excel(titanicxlsx, "titanic3")
data4 = pd.read_csv(titanicgit)

#encabezados
data1.shape
data2.shape
data3.shape
data4.shape

# con F9 logras ver los outputs
pd.isnull(data4["body"]).values.ravel().sum()

