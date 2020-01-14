#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:51:02 2019

@author: kyleschneider
"""

import pandas as pd
import numpy as np

# Where you load in CSV file
dataset = pd.read_csv('bestbath.com_organic_keywords.csv',encoding = 'unicode_escape')

#Creates a dataframe filtered to the position you'd like

def createDataWithPositionSpecs(min_p,max_p):
    cp = dataset.loc[(dataset['Position'] >= min_p) & (dataset['Position'] <= max_p)]
    return cp

cp = createDataWithPositionSpecs(11,29)

# Creates the total volume for 'Search Volume' column
def totalVolume(x):
    total = x['Search Volume'].sum()
    return total
totV = totalVolume(cp)

# Turns search volume into a percentage
k = (cp['Search Volume']/totV)*100


# Make booleans for filter parameters, change if statement for choice parameters
newData = []
for value in cp['Search Volume']:
    if (value/totV)*100 >= .5:
        newData.append(True)
    else:
        newData.append(False)
  

# add new columns variables to data frame      
cp['Volume Ratio'] = k
cp['Look into']= newData

# creates final dataframe
finalist = cp.loc[cp['Look into'] == True]

# Exports final dataframe to a csv file
# Use: finalist.to_csv(r'Path where you want to store the exported CSV file\File Name.csv')
# to select file path
finalist.to_csv(r'Desktop\keyword_research\cody_keyword_research3.csv')




