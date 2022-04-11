import redlab as rl

def readVoltage():
    voltage = input()
    return float(voltage)

while True:
    print("Enter Voltage:")
    rl.cbVOut(0,0,101,readVoltage())
