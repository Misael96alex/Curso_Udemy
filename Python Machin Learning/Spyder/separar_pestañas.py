# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 23:15:56 2023

@author: Alexander
"""

import pandas as pd
import os
#from openpyxl import load_workbook

# Load the Excel file
main_page = os.getcwd()
core = os.getcwd()
file_name = core + '\\excel\\Estados de Cuenta.xlsx'
##file_name = 'Estados de Cuenta.xlsx'
xl = pd.ExcelFile(file_name)

# For each sheet in the Excel file, create a new Excel file
for sheet_name in xl.sheet_names:
    # Load the sheet as a DataFrame
    df = xl.parse(sheet_name)
    df = df.iloc[3:]
    print(sheet_name)
    if sheet_name=="148619":
        df['Unnamed: 1'] = pd.to_datetime(df['Unnamed: 1'])
    #df['Unnamed: 1'] = pd.to_datetime(df['Unnamed: 1'], format='%d/%m/%Y')
    #df.reset_index(drop=True, inplace=True)
    # Create a new Excel file with the sheet name
    new_file_name = core+'\\excel\\'+f"{sheet_name}.xlsx"
    writer = pd.ExcelWriter(new_file_name, engine='openpyxl')
    
    # Write the DataFrame to the new Excel file
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    writer.save()
    print(df.columns)
    print(f"{new_file_name} created successfully!")