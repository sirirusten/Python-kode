import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

a_1 = 0.5
a_2 = 0.7
a_3 = 0.9
K_1 = 3
K_2 = 3
K_3 = 3

w, H_11 = signal.freqz([1+a_1 + K_1*(1-a_1), -(1+a_1)+K_1*(1-a_1)],[2, -2*a_1])
w, H_12 = signal.freqz([1+a_2 + K_2*(1-a_2), -(1+a_2) + K_2*(1-a_2)],[2, -2*a_2])
w, H_13 = signal.freqz([1+a_3 + K_3*(1-a_3), -(1+a_3) + K_3*(1-a_3)],[2, -2*a_3])

w, H_21 = signal.freqz([K_1*(1-a_1), K_1*(1-a_1)], [2, -(2*a_1)])
w, H_22 = signal.freqz([K_2*(1-a_2), K_2*(1-a_2)], [2, -(2*a_2)])
w, H_23 = signal.freqz([K_3*(1-a_3), K_3*(1-a_3)], [2, -(2*a_3)])

fig = plt.figure()
ax1 = fig.add_subplot(211)

plt.plot(w,abs(H_11),w,abs(H_12),w,abs(H_13),'b')
plt.xlabel('Frekvens, w')
plt.ylabel('Amplitude')
plt.grid(True, which = 'both')
plt.axhline(y=0, color='k')
plt.show()



# fig = plt.figure()
# ax1 = fig.add_subplot(211)

# plt.plot(w,abs(H_21),w,abs(H_22),w,abs(H_23),'b')
# plt.xlabel('Frekvens, w')
# plt.ylabel('Amplitude')
# plt.grid(True, which = 'both')
# plt.axhline(y=0, color='k')
# plt.show()

