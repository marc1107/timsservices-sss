import numpy as np
from windowing import getSpectrum
import matplotlib.pyplot as mpl


def main():
    calcPrototype("hoch")
    calcPrototype("runter")
    calcPrototype("links")
    calcPrototype("rechts")
    
    saveSignals("hoch")
    saveSignals("runter")
    saveSignals("links")
    saveSignals("rechts")
   
    
def saveSignals(command):
    spec = np.load("AudioSamples/" + command + "1_ref.npy")
    
    f = []
    for index in range(0, len(spec), 1):
        f.append(index)
    f = np.array(f)
    
    mpl.title('Signal: ' + command)    
    mpl.ylabel('Amplitude')
    mpl.xlabel('Frames')
    #mpl.plot(f, np.abs(specAverage))
    mpl.xlim(0, 20000)
    mpl.gcf().subplots_adjust(left=0.15)
    mpl.plot(f[:len(f)], spec[:len(spec)])
    mpl.savefig("Images/" + command + "_signal" + ".png", dpi=900)
    mpl.show()

def calcPrototype(command):
    
    for i in range(1, 6):
        pathSave = "WindowedSamples/" + command + str(i) + "_ref_windowed"
        np.save(pathSave, getSpectrum("AudioSamples/" + command + str(i) + "_ref.npy"))
        
    
    specAverage = np.load("WindowedSamples/" + command + "1_ref_windowed.npy")
    
    for i in range(2, 6):
        specAverage += np.load("WindowedSamples/" + command + str(i) + "_ref_windowed.npy")
    
    
    specAverage = specAverage / 5
    np.save("AudioSamples/" + command + "Proto", specAverage)
    
    f = []
    for index in range(0, len(specAverage), 1):
        f.append(index)
    f = np.array(f)
    
    mpl.title('Prototype: ' + command)    
    mpl.ylabel('Amplitude')
    mpl.xlabel('Frequency(Hz)')
    mpl.grid(True)
    #mpl.plot(f, np.abs(specAverage))
    mpl.xlim(0, 1500)
    mpl.plot(f[:len(f) // 2], np.abs(specAverage[:len(specAverage) // 2]))
    mpl.savefig("Images/" + command + "_proto" + ".png", dpi=900)
    mpl.show()
    

main()