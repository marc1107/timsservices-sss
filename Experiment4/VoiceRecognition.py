import numpy as np
import matplotlib.pyplot as mpl
from scipy import stats

hochProto = np.load("AudioSamples/hochProto.npy")
runterProto = np.load("AudioSamples/runterProto.npy")
linksProto = np.load("AudioSamples/linksProto.npy")
rechtsProto = np.load("AudioSamples/rechtsProto.npy")

prototypes = [hochProto , runterProto, linksProto, rechtsProto]

commands = ["hoch", "runter", "links", "rechts"]

def main():
    speechRecognizer()
    
    
    
def speechRecognizer():    
    names = []
    for c in commands:
        for n in range(1, 6):
            names.append(c + str(n) + "_")
            
            
    for n in names:
        spec = np.load("AudioSamples/" + n + "Roland" + ".npy")[:19968]
        spec = np.abs(np.fft.fft(spec))
        
        maximum = np.zeros(4)

        maximum[0] = stats.pearsonr(spec, hochProto)[0]
        maximum[1] = stats.pearsonr(spec, runterProto)[0]
        maximum[2] = stats.pearsonr(spec, linksProto)[0]
        maximum[3] = stats.pearsonr(spec, rechtsProto)[0]
        
        if(np.max(maximum) == maximum[0]):
            print(n + "Roland: hoch")
        elif(np.max(maximum) == maximum[1]):
            print(n + "Roland: runter")
        elif(np.max(maximum) == maximum[2]):
            print(n + "Roland: links")
        elif(np.max(maximum) == maximum[3]):
            print(n + "Roland: rechts")
    
    
    for n in names:
        spec = np.load("AudioSamples/" + n + "Tim" + ".npy")[:19968]
        spec = np.abs(np.fft.fft(spec))
        
        maximum = np.zeros(4)
        
        maximum[0] = stats.pearsonr(spec, hochProto)[0]
        maximum[1] = stats.pearsonr(spec, runterProto)[0]
        maximum[2] = stats.pearsonr(spec, linksProto)[0]
        maximum[3] = stats.pearsonr(spec, rechtsProto)[0]
        
        if(np.max(maximum) == maximum[0]):
            print(n + "Tim: hoch")
        elif(np.max(maximum) == maximum[1]):
            print(n + "Tim: runter")
        elif(np.max(maximum) == maximum[2]):
            print(n + "Tim: links")
        elif(np.max(maximum) == maximum[3]):
            print(n + "Tim: rechts")


main()