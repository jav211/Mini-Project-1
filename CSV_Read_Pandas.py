#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:13:12 2020

@author: danielshapiro
"""

#Column headers are category names
    #outputs a list of lists
    # each list is the questions (or answers) from each category
#columnns are questions (or answers) divided by category
        
import pandas
#Dont forget to import Pandas

def CSV_Read_Pandas(filename):
    data = pandas.read_csv(filename) #Reads csv into python, data type is dataframe
    Column_Headers=[] #creates empty list for column headers
        #Column headers will be the categories
    columns = [] #creates empty list for the columns of array
        #Columns are either questions or answers
    for col in data.columns:
        Column_Headers.append(col) #Creates list of column headers
    for header in Column_Headers:
        whole_column_raw = data[[header]]
        whole_column = whole_column_raw.to_numpy().tolist()
        column = []
        for element in whole_column:
            string_element = str(element[0])
            column.append(string_element)
        columns.append(column)
    return(Column_Headers,columns)