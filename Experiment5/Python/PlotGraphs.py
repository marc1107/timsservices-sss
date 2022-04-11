import matplotlib.pyplot as mpl
import numpy as np

def readAndDisplay(file):    
    data = np.genfromtxt(file, delimiter=';', skip_header=100, skip_footer=100)

    file = file.replace("../", "")
    file = file.replace(".csv", "")

    mpl.title(file)    
    mpl.ylabel('Volt(V)')
    mpl.xlabel('Zeit(ms)')

    mpl.plot(data[:,0], data[:,1])
    mpl.savefig("../Images/" + file + ".png", dpi=900)
    mpl.show() 
    

readAndDisplay("../1752Hz.csv")
readAndDisplay("../2000Hz.csv")
readAndDisplay("../3000Hz.csv")
readAndDisplay("../4000Hz.csv")
readAndDisplay("../5000Hz.csv")
readAndDisplay("../6000Hz.csv")
readAndDisplay("../7000Hz.csv")