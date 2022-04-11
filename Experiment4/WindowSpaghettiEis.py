import numpy as np
import matplotlib.pyplot as mpl
from windowing import getSpectrum


def main():
    displayAndSave(getSpectrum("AudioSamples/SpaghettiEis_cuted.npy"))

def displayAndSave(wordWindowed):
    print(len(wordWindowed))
    word = np.load("AudioSamples/SpaghettiEis_cuted.npy")[:20000-32]
    
    f = []
    for index in range(0, len(word), 1):
        f.append(index/(len(word) * 0.00001))
    f = np.array(f)
    
    mpl.title('Fouriertransform')    
    mpl.ylabel('Amplitude')
    mpl.xlabel('Frequency(Hz)')
    mpl.grid(True)
    mpl.xlim(0, 2000)
    mpl.gcf().subplots_adjust(left=0.15)
    mpl.plot(f[:len(f) // 2], np.abs(wordWindowed[:len(wordWindowed) // 2]))
    #mpl.plot(data, abs(wordWindowed))
    mpl.savefig("Images/" + 'SpaghettiEisWindowed.png', dpi=900)
    mpl.show()
    
    
main()