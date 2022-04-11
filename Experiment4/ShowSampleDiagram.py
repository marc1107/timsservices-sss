import sys
import numpy
import matplotlib.pyplot as plt

if(len(sys.argv) != 2):
    print("Usage: python " + sys.argv[0] + " [File]")
    sys.exit(-1)
    
img = numpy.load(str(sys.argv[1]) + ".npy")
plt.title('Signal')    
plt.ylabel('Amplitude')
plt.xlabel('Frames')
plt.plot(img)
plt.show()