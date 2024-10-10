# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:11:38 2022

@author: jhsol
"""

import serial
import time
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np

UNO = serial.Serial('COM10', 9600, timeout=2)

UNO.write('1'.encode())
df = pd.DataFrame()

for i in range(29):
    data = str(UNO.readline())
    data = data.replace('b\'','')
    data = data.replace('\\r\\n\'','')
    print(data)
    if i in range(2,8):
        df.loc['Sample 1', i-2]=int(re.search(r'\d+', data).group())
    if i in range(9,15):
        df.loc['Sample 2', i-9]=int(re.search(r'\d+', data).group())
    if i in range(16,22):
        df.loc['Sample 3', i-16]=int(re.search(r'\d+', data).group())
    if i in range(23,29):
        df.loc['Sample 4', i-23]=int(re.search(r'\d+', data).group())
    
    time.sleep(0.12)
   
df= df.T
print(df)

sample = ['Sample 1','Sample 2','Sample 3', 'Sample 4']
x=[1,2,3,4,5,6]
plt.figure(1)
for samples in sample:
    dfs=df.loc[:,samples]
    plt.plot(x, dfs)
plt.legend(sample)
plt.show()
    
    
    
