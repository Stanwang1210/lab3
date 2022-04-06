#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 21:55:43 2022

@author: wangshihang
"""

from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

# df = pd.read_csv('data.csv', encoding='utf-8')
# df = df.dropna()
PTT = '350.0  313.0  360.0  323.0  346.0  355.0  326.0  338.0  346.0  341.0  321.0  330.0  250.0  355.0  295.0  311.0  286.0  293.0  342.0  295.0  361.0  315.0  300.0  313.0  303.0  355.0  326.0  338.0  346.0  341.0  301.0  300.0  315.0  328.0  273.0  311.0  309.0  321.0  297.0  281.0'
SBP = '116.0  117.0  116.0  117.0  117.0  116.0  117.0  117.0  116.0  116.0  117.0  116.0  119.0  116.0  118.0  116.0  116.0  117.0  118.0  117.0  116.0  117.0  117.0  117.0  118.0  116.0  117.0  117.0  116.0  116.0  118.0  118.0  118.0  117.0  118.0  116.0  117.0  117.0  118.0  116.0'
DBP = '71.0   70.0   71.0   70.0   71.0   70.0   71.0   71.0   71.0   70.0   70.0   70.0   70.0   71.0   71.0   71.0   70.0   71.0   71.0   70.0   71.0   71.0   68.0   70.0   71.0   70.0   71.0   71.0   71.0   70.0   70.0   71.0   72.0   71.0   69.0   71.0   70.0   72.0   70.0   70.0'

PTT = PTT.split('  ')
SBP = SBP.split('  ')
DBP = DBP.split('  ')

PTT = np.array([float(x) for x in PTT])
SBP = np.array([float(x) for x in SBP])
DBP = np.array([float(x) for x in DBP])
print(PTT)

for i in range(0, 40, 10):
    model = LinearRegression()
    model.fit(PTT[i:i+10].reshape(-1, 1), SBP[i:i+10])
    a = model.coef_[0]
    b = model.intercept_
    
    model = LinearRegression()
    model.fit(PTT[i:i+10].reshape(-1, 1), DBP[i:i+10])
    c = model.coef_[0]
    d = model.intercept_
    print(f"a = {a}, b = {b}, c = {c}, d = {d}")