import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as figure
import math

A_x = 0.25
A_y = 0.25
f_x = 0.04
f_y = 0.10
L = 500

n = np.arange(0, L-1, 1);

d = A_x*np.cos(2*math.pi*f_x*n) + A_y*np.cos(2*math.pi*f_x*n)
e = np.random.normal(size=(L-1))
g = d + e

f = plt.figure()
f.set_figwidth(7)
f.set_figheight(2)

plt.plot(n, d)
plt.xlabel('n')
plt.ylabel('d(n)')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()

f = plt.figure()
f.set_figwidth(7)
f.set_figheight(2)

plt.plot(n, g)
plt.xlabel('n')
plt.ylabel('g(n)')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()

f = plt.figure()
f.set_figwidth(7)
f.set_figheight(2)

plt.plot(np.abs(np.fft.fft(g, 2048)))
plt.xlabel('n')
plt.ylabel('|G(n)|')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()