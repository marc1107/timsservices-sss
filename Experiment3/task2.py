import numpy as np
import matplotlib.pyplot as mpl


#Frequenz, Amplitude in mV, Phasenverschiebung in ms    
bigSpeaker = np.array([[100, 44, 5.233], [200, 100, 4.526], [300, 62, 3.383], [400, 45, 2.757],
                       [500, 36, 2.335], [700, 29.23, 1.662], [850, 27.32, 1.376], [1000, 28.71, 1.185],
                       [1200, 27.14, 1.029], [1500, 25.4, 0.8385], [1700, 24.36, 0.7636], [2000, 24.71, 0.6752],
                       [3000, 23.32, 0.466], [4000, 33.41, 0.3963], [5000, 20.88, 0.3572], [6000, 25.4, 0.3044],
                       [10000, 22.1, 0.2534]])

smallSpeaker = np.array([[100, 10.79, 4.063], [200, 18.62, 3.083], [300, 26.45, 2.213], [400, 46.98, 1.886],
                         [500, 106, 1.777], [700, 59.16, 1.6], [850, 41.76, 1.396], [1000, 32.36, 1.219],
                         [1200, 26.27, 1.022], [1500, 34.28, 0.8181], [1700, 29.58, 0.7432], [2000, 29.23, 0.6412],
                         [3000, 37.76, 0.4677], [4000, 40.02, 0.3997], [5000, 20.71, 0.3402], [6000, 19.49, 0.3316],
                         [10000, 14.96, 0.250]])

def main():
    plotBodeDiagramm(bigSpeaker, "Big Speaker", "BigSpeaker")
    plotBodeDiagramm(smallSpeaker, "Small Speaker", "SmallSpeaker")
    plotReadings(bigSpeaker, "Big Speaker", "BigSpeaker")
    plotReadings(smallSpeaker, "Small Speaker", "SmallSpeaker")
    
def plotBodeDiagramm(speaker, plotTitle, fileName):    
    freq = speaker[:, :1]# * 2 * np.pi
    phase = (speaker[:, 2:3] / -1000) * speaker[:, :1] * 360
    amp = speaker[:, 1:2] / 1000
    
    mpl.figure()
    mpl.subplot(211)
    mpl.title('Bode Diagram ' + plotTitle)    
    mpl.xlabel('frequency f')
    mpl.ylabel('Amplitude (dB)')
    mpl.semilogx(freq, 20 * np.log10(abs(amp)))
    #mpl.xlim(speaker[0,0] * 2 * np.pi, speaker[16,0] * 2 * np.pi)
    mpl.xlim(speaker[0,0], speaker[16,0])
    mpl.grid(True)

    mpl.subplot(212)  
    mpl.xlabel('frequency f')
    mpl.ylabel('Phase angle')
    mpl.semilogx(freq, phase)
    #mpl.xlim(speaker[0,0] * 2 * np.pi, speaker[16,0] * 2 * np.pi)
    mpl.xlim(speaker[0,0], speaker[16,0])
    mpl.grid(True)
    
    mpl.show
    mpl.savefig('BodeDiagram' + fileName + '.png', dpi=900)
    
def plotReadings(speaker, plotTitle, fileName):
    freq = speaker[:, :1]
    phase = speaker[:, 2:3]
    amp = speaker[:, 1:2]
    
    mpl.figure()
    mpl.subplot(211)
    mpl.title('Measuring readings ' + plotTitle)    
    mpl.xlabel('frequency f')
    mpl.ylabel('Amplitude (mV)')
    mpl.plot(freq, amp)
    mpl.xlim(speaker[0,0], speaker[16,0])
    mpl.grid(True)

    mpl.subplot(212)  
    mpl.xlabel('frequency f')
    mpl.ylabel('Phase (ms)')
    mpl.plot(freq, phase)
    mpl.xlim(speaker[0,0], speaker[16,0])
    mpl.grid(True)
    
    mpl.show
    mpl.savefig('MeasurementPlot' + fileName + '.png', dpi=900)

main()