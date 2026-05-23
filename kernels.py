#taken from OpenPlanetary's Intro to SPICE #1 YouTube series

import os
import spiceypy as spice
from datetime import datetime

#define kernels path
kernelsPath = os.path.join(os.path.dirname(os.getcwd()), "kernels")

#define path to leap second kernel
leapSecondsKernelPath = os.path.join(kernelsPath, "naif0012.tls")

#load leap second kernel
spice.furnsh(leapSecondsKernelPath)

#Defining the concept of "now"
now = str(datetime.now())
print(now)

#converting "now" into ET
nowET = spice.str2et(now)
print(nowET)

#define path to solat system ephemeris kernel
solarSystemEpheremisKernelPath = os.path.join(kernelsPath, "de405.bsp")

#load kernel
spice.furnsh(solarSystemEpheremisKernelPath)

#define frames
target = "EARTH"
observer = "SUN"
reference = "J2000"

#get earth positions
earthPositions - spice.spkpos(target, nowET, reference, 'NONE', observer)
print(earthPositions)

#unload kernels
spice.kclear()