import numpy as np
import matplotlib.pyplot as mpl
import math

data = []
dataAvrg = []
dataStdAbweichung = []

dataAvrgLog = []
distancesLog = []

a = 0
b = 0

data2 = [] #1. Liste lange Seite; 2. Liste kurze Seite
averageLongSide = 0 #Durchschnitt der Messungen der langen Seite in Volt
averageShortSide = 0 #Durchschnitt der Messungen der kurzen Seite in Volt

stdDeviationAvrgLong = 0 #Standardabweichung vom Mittelwert (Lange Seite)
stdDeviationAvrgShort = 0 #Standardabweichung vom Mittelwert (kurze Seite)

mistakeLong95 = 0
mistakeShort95 = 0
mistakeLong68 = 0
mistakeShort68 = 0

CORRECTION_FACTOR_68 = 1
CORRECTION_FACTOR_95 = 1.96


def main():
    getData()
    calculateAverage()
    calculateLogData()
    plotGraph()
    plotLogGradient()
    calcStdDeviationFirst()
    printStdDeviation()
    
    getData2()
    calcMistakes()


def getData():
    for x in range(13, 73, 3):
        data.append(np.genfromtxt("C:\\Users\\Rolan\\OneDrive\\Dokumente\\sss\\Messwerte1\\" + str(x) + ".csv", delimiter=";", skip_header=1000, usecols=([1]), max_rows=10000))
        #data.append(np.genfromtxt("/home/tim/Downloads/Versuch1/" + str(x) + ".csv", delimiter=";", skip_header=1000, usecols=([1]), max_rows=10000))

def getData2():
    for x in ('langeSeite', 'kurzeSeite'):
        data2.append(np.genfromtxt("C:\\Users\\Rolan\\OneDrive\\Dokumente\\sss\\" + str(x) + ".csv", delimiter=";", skip_header=1000, usecols=([1]), max_rows=10000))
        #data.append(np.genfromtxt("/home/tim/Downloads/Versuch1/" + str(x) + ".csv", delimiter=";", skip_header=1000, usecols=([1]), max_rows=10000))
    global averageLongSide
    global averageShortSide
    global stdDeviationAvrgLong
    global stdDeviationAvrgShort
    
    averageLongSide = np.average(data2[0])
    averageShortSide = np.average(data2[1])
    
    stdDeviationAvrgLong = calcStdDeviation(averageLongSide, 0) #lange Seite
    stdDeviationAvrgShort = calcStdDeviation(averageShortSide, 1) #kurze Seite

def calculateAverage():
    for x in range(0, 20):
        dataAvrg.append(np.average(data[x]))

def plotGraph():
    mpl.title('Messwerte')
    mpl.xlabel('Abstand(cm)')
    mpl.ylabel('Spannung(V)')
    mpl.grid(True)
    a = calculateGradientLinearRegression()
    plotExponentialRegression(a, calculateOffsetLinearRegression(a))
    
    index = 0
    labelVar = 'Measured Value Averages'
    for x in range(13, 73, 3):
        if(x >= 16):
            labelVar = ''
        mpl.plot(x, dataAvrg[index], '.b', label = labelVar)
        index += 1
    
    mpl.legend(loc='upper right')
    
    mpl.savefig('ExpRegr.png', dpi=900)
    
    mpl.show()

def plotLogGradient():
    mpl.title('Log-Messwerte')    
    mpl.xlabel('Abstand(cm)')
    mpl.ylabel('Spannung(V)')
    mpl.grid(True)

    a = calculateGradientLinearRegression()
    b = calculateOffsetLinearRegression(a)
    
    x = np.linspace(2.5, 4.25, 20)
    y = a * x + b

    mpl.plot(x, y, '-r', label = 'Linear Regression')

    x = np.linspace(13, 73, 20)
    mpl.plot(np.log(x), np.asarray(dataAvrgLog), '.b', label = 'Measured Log Value Averages')
    
    mpl.legend(loc='upper right')
    
    mpl.savefig('LinearRegr.png', dpi=900)
    
    mpl.show()
    
    print("a: " + str(a))
    print("b: " + str(b))

def calculateLogData():
    for x in range(13, 73, 3):
        distancesLog.append(np.log(x))

    for x in range(0, 20):
        dataAvrgLog.append(np.log(dataAvrg[x]))

def calculateGradientLinearRegression():
    top = 0
    bottom = 0
        
    for x in range(1, 20):
        top += (distancesLog[x] - np.average(distancesLog)) * (dataAvrgLog[x] - np.average(dataAvrgLog))

    for x in range(1, 20):
        bottom += ((distancesLog[x] - np.average(distancesLog))) ** 2

    return (top / bottom)

def calculateOffsetLinearRegression(a):
    return np.average(dataAvrgLog) - (a * np.average(distancesLog))

def plotExponentialRegression(aLocal, bLocal):
    global a
    global b
    a = aLocal
    b = bLocal
    x = np.linspace(13, 73, 20)
    y = math.exp(b) * (x ** a)

    mpl.grid(True)
    mpl.plot(x, y, '-r', label = 'Exponential Regression')
    
def calcStdDeviationFirst(): #StandardAbweichung vom Mittelwert
    sum = 0
    for x in range(0, 20):
        for z in range(0, 10000):    
            sum += ((dataAvrg[x] - data[x][z]) ** 2)
        s = ((1 / 9999) * sum) ** (1 / 2)
        dataStdAbweichung.append(s / (10000 ** (1 / 2)))
        
def calcStdDeviation(average, longOrShort): #StandardAbweichung vom Mittelwert
    output = 0
    sum = 0
    for x in range(1, 10000):
        sum += ((average - data2[longOrShort][x]) ** 2)
        
    s = math.sqrt((1 / 9999) * sum)
    
    output = s / math.sqrt(10000)
    return output
    

def printStdDeviation():
    for x in range(0, 20):
        print("Standardabweichung: " + str(dataStdAbweichung[x]))
        
def calcMistakes():
    global mistakeLong68
    global mistakeLong95
    global mistakeShort68
    global mistakeShort95
    
    mistakeLong68 = calcAbsoluteMistakeInCM(averageLongSide, stdDeviationAvrgLong * CORRECTION_FACTOR_68)
    mistakeShort68 = calcAbsoluteMistakeInCM(averageShortSide, stdDeviationAvrgShort * CORRECTION_FACTOR_68)
    mistakeLong95 = calcAbsoluteMistakeInCM(averageLongSide, stdDeviationAvrgLong * 2 * CORRECTION_FACTOR_95)
    mistakeShort95 = calcAbsoluteMistakeInCM(averageShortSide, stdDeviationAvrgShort * 2 * CORRECTION_FACTOR_95)
    
def calcAbsoluteMistakeInCM(x, AbsoluteMistakeVolt):
    return ((math.exp((np.log(x) - b) / a) / (a * x)) * AbsoluteMistakeVolt)

def getDistanceFromVolt(volt):
    return math.exp((np.log(volt) - b) / a)

def getReproductionError():
    firstMistakeSquared = (getDistanceFromVolt(averageShortSide) * mistakeLong95) ** 2
    secondMistakeSquared = (getDistanceFromVolt(averageLongSide) * mistakeShort95) ** 2
    measureMistake = math.sqrt(firstMistakeSquared + secondMistakeSquared)
    return measureMistake
    

main()