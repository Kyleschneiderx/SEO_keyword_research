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
def createDataWithPositionSpecs(min_p,max_p, percent):
    cp = dataset.loc[(dataset['Position'] >= min_p) & (dataset['Position'] <= max_p)]
    total = cp['Search Volume'].sum()
    newData = []
    for value in cp['Search Volume']:
        if (value/total)*100 >= percent:
            newData.append(True)
        else:
            newData.append(False)

    search_volume_ratio = (cp['Search Volume']/total)*100
    cp['Volume Ratio'] = search_volume_ratio
    cp['Look into']= newData
    finalist = cp.loc[cp['Look into'] == True]
    
    return finalist.to_csv(r'Desktop\keyword_research\cody_keyword_research10.csv')



createDataWithPositionSpecs(20,40,.5)



