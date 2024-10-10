import serial
import time
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import bluetooth

UNO = serial.Serial('COM7', 9600, timeout=2)

# UNO.write('1'.encode())

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(("00:21:08:35:1B:BD", 1))
sock.send('1'.encode())

while(True):
   print(sock.recv(10))