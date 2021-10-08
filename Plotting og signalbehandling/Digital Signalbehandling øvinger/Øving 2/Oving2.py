import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

w, H_1 = signal.freqz([0.1, 0.1],[2, -1.8])

fig = plt.figure()
ax1 = fig.add_subplot(211)

plt.plot(w,abs(H_1),'b')
plt.xlabel('Frekvens, w')
plt.ylabel('Amplitude')
plt.grid(True, which = 'both')
plt.axhline(y=0, color='k')
plt.show()

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(H_1))
plt.plot(w, angles, 'g')
plt.xlabel('Frekvens, w')
plt.ylabel("Fase")

plt.grid(True, which = 'both')
plt.axhline(y=0, color='k')
plt.show()