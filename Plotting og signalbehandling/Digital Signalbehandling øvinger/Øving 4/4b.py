import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal



A_x = 0.25
A_y = 0.25
f_x = 0.04
f_y = 0.10
L = 500

num_x = np.poly([1, -1])
den_x = np.poly([0.99*np.exp(1j*2*math.pi*f_x), 0.99*np.exp(-1j*2*math.pi*f_x)])
print(den_x)
num_y = np.poly([1, -1])
den_y = np.poly([0.99*np.exp(1j*2*math.pi*f_y), 0.99*np.exp(-1j*2*math.pi*f_y)])

zeros_x = np.roots(num_x)
poles_x = np.roots(den_x)

zeros_y = np.roots(num_y)
poles_y = np.roots(den_y)

w_x, H_x = signal.freqz(zeros_x, poles_x)

w_y, H_y = signal.freqz(zeros_y, poles_y)

n = np.arange(0, L-1, 1)

d = A_x*np.cos(2*math.pi*f_x*n) + A_y*np.cos(2*math.pi*f_y*n)
e = np.random.normal(size=(L-1))
g = d + e


# fig , ax = plt . subplots ()

# # plot circle
# theta = np . linspace ( - np . pi , np . pi , 1000)
# ax . plot ( np . sin ( theta ) , np . cos ( theta ) , '--k')
# ax . set_aspect (1)

# plot poles and zeros
# ax . plot ( np . real ( poles ) , np.imag(poles) ,'Xb ', label ='Poles ')

# ax . plot ( np . real ( zeros ) , np . imag ( zeros ) ,'or ', label ='Zeros ')
# ax . set_xlabel ('Real part ')
# ax . set_ylabel ('Imaginary part ')

fig = plt.figure()
ax1 = fig.add_subplot(211)

plt.plot(w_x/(math.pi),abs(H_x),'b')
plt.xlabel('w')
plt.ylabel('$|H_x(w)|$')
plt.grid(True, which = 'both')
plt.axhline(y=0, color='k')
plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(211)

plt.plot(w_y/(math.pi),abs(H_y),'b')
plt.xlabel('w')
plt.ylabel('$|H_y(w)|$')
plt.grid(True, which = 'both')
plt.axhline(y=0, color='k')
plt.show()

q_x = signal.lfilter(zeros_x, poles_x, g)
q_y = signal.lfilter(zeros_y, poles_y, g)

f = plt.figure()
f.set_figwidth(7)
f.set_figheight(2)

plt.plot(n,q_x,'b')
plt.xlabel('n')
plt.ylabel('$q_x(n)$')
plt.grid(True, which = 'both')
plt.axhline(y=0, color='k')
plt.show()


f = plt.figure()
f.set_figwidth(7)
f.set_figheight(2)

plt.plot(n,q_y,'b')
plt.xlabel('n')
plt.ylabel('$q_y(n)$')
plt.grid(True, which = 'both')
plt.axhline(y=0, color='k')
plt.show()

f = plt.figure()
f.set_figwidth(7)
f.set_figheight(2)

plt.plot(np.abs(np.fft.fft(q_x, 2048)))
plt.xlabel('n')
plt.ylabel('$|Q_x(n)|$')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()

f = plt.figure()
f.set_figwidth(7)
f.set_figheight(2)

plt.plot(np.abs(np.fft.fft(q_y, 2048)))
plt.xlabel('n')
plt.ylabel('$|Q_y(n)|$')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()




def add(p1,p2):
    x = [0]*(max(p1[0][1],p2[0][1])+1)
    for i in p1+p2:
        x[i[1]]+=i[0]
    res =  [(x[i],i) for i in range(len(x)) if x[i]!=0]
    res.sort(key = lambda r: r[1], reverse= True)
    return res

def mul(p1,p2):
    x = [0]*(p1[0][1]*p2[0][1]+1)
    for i in p1:
        for j in p2:
            x[i[1]+j[1]]+=i[0]*j[0]
    res = [(x[i],i) for i in range(len(x)) if x[i]!=0]
    res.sort(key = lambda r: r[1], reverse= True)
    return res




zeros = zeros_x, np.roots(np.polyadd(den_x, den_y))
poles = poles_x, poles_y

fig , ax = plt . subplots ()

# plot circle
theta = np . linspace ( - np . pi , np . pi , 1000)
ax . plot ( np . sin ( theta ) , np . cos ( theta ) , '--k')
ax . set_aspect (1)

# plot poles and zeros
ax . plot ( np . real ( poles ) , np.imag(poles) ,'Xb ', label ='Poles ')

ax . plot ( np . real ( zeros ) , np . imag ( zeros ) ,'or ', label ='Zeros ')
ax . set_xlabel ('Real part ')
ax . set_ylabel ('Imaginary part ')



q = signal.lfilter(zeros, poles, g)

f = plt.figure()
f.set_figwidth(7)
f.set_figheight(2)

plt.plot(n,q,'b')
plt.xlabel('n')
plt.ylabel('$q(n)$')
plt.grid(True, which = 'both')
plt.axhline(y=0, color='k')
plt.show()

f = plt.figure()
f.set_figwidth(7)
f.set_figheight(2)

plt.plot(np.abs(np.fft.fft(q, 2048)))
plt.xlabel('n')
plt.ylabel('$|Q(n)|$')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()


