# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:05:44 2022

@author: Alexander
"""
import pandas as pd
import numpy as np
# Dummy Data Setss
data=pd.DataFrame(
    {
     'A':np.random.rand(10),
     'B': 1.5 +2.5 * np.random.rand(10),
     'C': np.random.uniform(5,32,10)
     }
    )