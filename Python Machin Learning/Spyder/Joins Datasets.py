# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:10:20 2022

@author: Alexander
"""

import pandas as pd
import numpy as np
from IPython.display import Image

fillpath = "../datasets/athletes/"
data_main = pd.read_csv(fillpath+"Medals.csv", encoding = "ISO-8859-1")

# CONTAR VALORES UNICOS
a= data_main["Athlete"].unique().tolist()
len(a)

data_country = pd.read_csv(fillpath +"Athelete_Country_Map.csv", encoding = "ISO-8859-1" )

# tarea: contar los valores repetidos de un Dataframe
data_country[data_country["Athlete"]=="Aleksandar Ciric"]

data_sports=pd.read_csv(fillpath+"Athelete_Sports_Map.csv", encoding = "ISO-8859-1")

#ELIMINAR DUPLICDOS
data_country_dp=data_country.drop_duplicates(subset="Athlete")
data_sports_dp=data_sports.drop_duplicates(subset="Athlete")

# uso de  INNER JOINS
data_main_country = pd.merge(left = data_main, right=data_country, 
                             left_on="Athlete", right_on="Athlete")

# uso de   JOINS
"""
**Inner Joins**

"""
Image(filename="../Resources/inner-join.png")
data_main_country_inner = pd.merge(left = data_main, right=data_country_dp,
                              how="inner",
                             left_on="Athlete", right_on="Athlete")

data_main_country_sports_inner = pd.merge(left=data_main_country_inner, right=data_sports_dp,
                                     how="inner",
                                     left_on="Athlete", right_on="Athlete")

"""
**left Joins**

"""
Image(filename="../Resources/inner-join.png")
data_main_country_left = pd.merge(left = data_main, right=data_country_dp, 
                              how="left",
                             left_on="Athlete", right_on="Athlete")

data_main_country_sports_left = pd.merge(left=data_main_country_inner, right=data_sports_dp,
                                     how="left",
                                     left_on="Athlete", right_on="Athlete")

"""
**Right Joins**

"""
Image(filename="../Resources/inner-join.png")
data_main_country_right = pd.merge(left = data_main, right=data_country_dp, 
                              how="inner",
                             left_on="Athlete", right_on="Athlete")

data_main_country_sports_right = pd.merge(left=data_main_country_inner, right=data_sports_dp,
                                     how="inner",
                                     left_on="Athlete", right_on="Athlete")

# Elegir y eliminar athletes aleatoriamente

out_athletes=np.random.choice(data_main["Athlete"], size = 6, replace = False)

data_country_dlt= data_country[(~data_country["Athlete"].isin(out_athletes))&
                               (data_country["Athlete"]!="Michael Phelps")]
