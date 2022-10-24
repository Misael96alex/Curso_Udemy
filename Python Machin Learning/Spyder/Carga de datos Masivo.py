# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:51:24 2022

@author: Alexander
"""

import pandas as pd

# url
filepath="../datasets/distributed-data/"

data = pd.read_csv("../datasets/distributed-data/001.csv")

for i in range(2,16):
    if i < 10:
        filename = "00"+str(i)
    if  10 <= i < 100:
        filename="0"+str(i)
    file = filepath+filename+".csv"
    temp_data = pd.read_csv(file)
    
    data=pd.concat([data,temp_data], axis = 0)
        