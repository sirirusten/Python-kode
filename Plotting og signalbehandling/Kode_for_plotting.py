import csv
import math
import matplotlib.pyplot as plt
import numpy as num


header = []
data = []

filename = 'Spectrumgreie.csv'

with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)
    for datapoint in csvreader:
        values=[float(value)for value in datapoint]
        data.append(values)


print(header)
print(data[0])

#freq=[(20*math.log10(p[0]))for p in data]
freq=[p[0]*1000for p in data]
ch1= [(p[1])for p in data]
ch2= [(p[2])for p in data]

for p in range(0, len(freq)):
    if freq[p] == 0:
        print(p)


#freq = freq[4095:]#gir alle verdier fra 1khz til 10khz
#ch1 = ch1[4095:]
#ch2 = ch2[4095:]

plt.plot(freq,ch2, freq, ch1)#,#time,ch2)
plt.xlabel('Time (ms)')
plt.ylabel('Volt (V)')
plt.legend(header[1:])
#plt.vlines(2025, -50, 0, colors='k', linestyles='dotted', label='')
#plt.vlines(2700, -50, 0, colors='k', linestyles='dotted', label='')
#plt.hlines(-3, 1000, 10000, colors='k', linestyles='dotted', label='')
#plt.hlines(-10, 1000, 10000, colors='k', linestyles='dotted', label='')
plt.show()