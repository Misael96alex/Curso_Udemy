# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 22:46:55 2022

@author: Alexander
"""
# Carga de datos a travez de la funcion read_csv

import pandas as pd
# import os

titaniccsv= "../datasets/titanic3.csv"
titanicxls= "../datasets/titanic3.xls"
titanicxlsx= "../datasets/titanic3.xlsx"

data1 = pd.read_csv(titaniccsv)

data1.head()
data2 = pd.read_excel(titanicxls, "titanic3")
data2 = pd.read_excel(titanicxlsx, "titanic3")

