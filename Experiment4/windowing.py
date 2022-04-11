import numpy as np
from scipy import signal
import math

sampleFreq = 20000-32 # -32 because it has to be divisible by 256
        
def getSpectrum(file):        
    data = np.load(file)[:sampleFreq]
    return windowed_fft(data)

def windows(arr, window_function, window_size):
    
    for i in range(0, len(arr) - window_size + 1, math.floor(window_size / 2)):
        yield np.concatenate([[0]*i, list(window_function(arr[i:i+window_size])), [0]*(len(arr) - (i + window_size))])


def windowed_fft(data):
    
    gauss_window = np.array(signal.gaussian(512, 512 / 4))

    window = np.array(list(windows(data, lambda d: d * gauss_window, 512)))

    return np.fft.fft(window).mean(0)

