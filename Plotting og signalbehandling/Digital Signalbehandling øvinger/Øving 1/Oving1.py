import numpy as np
import sounddevice as sd
import math

import soundfile as sf
import matplotlib.pyplot as plt



# filename = 'test_waw.wav'
# # Extract data and sampling rate from file
# data, fs = sf.read(filename, dtype='float32')  
# sd.play(data, fs)


# def createX(f,f_s):
#     ns = np.arange(f_s * 4)
#     for i in range(1, len(ns) + 1):
#         ns[i - 1] = i
#     x = [math.cos(math.pi * 2 * (f/f_s) * n) for n in ns]   
#     return x

# f_s = 8000
# sd.play(createX(1000, f_s), f_s)
# status = sd.wait()  # Wait until file is done playing'
# # #Collapse

# y_1 = [1,3,6,5,3]
# h_2 = []


# for n in range(11):
#     h_2.append((0.9)**n)
    
# y_2 = np.convolve(h_2,y_1)

# x = []
# for n in range(len(y_2)):
#     x.append(n)

# plt.stem(x,y_2)
# plt.show()

x = []
for n in range(0,3):
    x.append(n+1)
    
h_1 = []

for n in range(11):
    h_1.append((0.9)**n)
    
y_1 = np.convolve(h_1,x)

n = []
for i in range(len(y_1)):
    n.append(i)

plt.stem(n,y_1)
plt.show()

h_2 = []

for n in range[]



