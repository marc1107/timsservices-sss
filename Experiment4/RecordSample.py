import pyaudio
import numpy
import matplotlib.pyplot as plt
FORMAT = pyaudio.paInt16
SAMPLEFREQ = 20000
FRAMESIZE = 20
NOFFRAMES = 1000

p = pyaudio.PyAudio()
print('running')
stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,input=True,frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES*FRAMESIZE)
decoded = numpy.fromstring(data, 'Int16')
      
stream.stop_stream()
stream.close()
p.terminate()
print('done')

# Skip first few frames due to weird behaviour
decoded = decoded[500:]

# Trigger when threshold is reached 
for i in range(len(decoded)):
    if decoded[i] > 500:
        decoded = decoded[i:]
        break

# Filling up array with zeros to get 1s length
for i in range((SAMPLEFREQ - len(decoded)) + 500):
    decoded = numpy.append(decoded, 0)

print(decoded)
print(len(decoded))

numpy.save('links5_tim', decoded)
plt.plot(decoded)
plt.show()  