import redlab as rl
import numpy as np
from time import sleep

rl.cbVOut(0,0,101, 1)

sin = []

for i in range(40):
    sin.append(np.sin(2*np.pi / 40 * i) + 1)
    
print(len(sin))

while True:
    for x in sin:
        rl.cbVOut(0,0,101, x)
        sleep(0.1)