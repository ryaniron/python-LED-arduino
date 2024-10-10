import serial
import time
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np

def arduino_capture():
    UNO = serial.Serial('COM7', 9600, timeout=2)

    UNO.write('1'.encode())
    df = pd.DataFrame()
    N = 5 #number of readings
    T = 0.4 #time should match arduino sketch
    x = np.linspace(1, N, num = N)
    c = 0
    index = 0

    for i in range(N*4):
        c += 1
        data = str(UNO.readline())
        data = data.replace('b\'', '')
        data = data.replace('\\r\\n\'', '')

        if (c == 1):
            df.loc['Sample 1', index] = int(re.search(r'\d+', data).group())
        if (c == 2):
            df.loc['Sample 2', index] = int(re.search(r'\d+', data).group())
        if (c == 3):
            df.loc['Sample 3', index] = int(re.search(r'\d+', data).group())
        if (c == 4):
            df.loc['Sample 4', index] = int(re.search(r'\d+', data).group())
            c = 0
            index += 1
        
        time.sleep(T) 
    df = df.T
    UNO.close()

    sample = ['Sample 1','Sample 2','Sample 3', 'Sample 4']

    values = pd.DataFrame.to_numpy(df)

    reading_mean = np.mean(values, axis = 0)

    return reading_mean
    
