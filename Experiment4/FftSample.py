import numpy as np
import matplotlib.pyplot as mpl

data = np.load("AudioSamples/SpaghettiEis_cuted.npy")
#data = np.load("WindowedSamples/spaghettiEis_windowed.npy")
data = data[:100000]

f = []
for index in range(0, len(data), 1):
    f.append(index/(len(data) * 0.00001))
f = np.array(f)

four = np.fft.fft(data)*0.00001

mpl.title('Fouriertransform')
mpl.ylabel('Amplitude')
mpl.xlabel('Frequency(Hz)')
mpl.xlim(0, 2000)
mpl.ylim(0, np.max(four))
mpl.grid(True)

mpl.plot(f[:len(f) // 2], np.abs(four[:len(four) // 2]))
mpl.show()