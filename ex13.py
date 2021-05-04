import numpy as np
from si_prefix import si_format as si
from eletro_help import *

I1 = 1e-3
I2 = 2e-3
R1 = R3 = R5 = R6 = 1e3
R2 = 2e3
R4 = 250
V1 = 2
V2 = 1

# obter o equivalente thevenin nos terminais de r4 considerando R4 como a carga

IA = -I1
IC = I2
# V2 + R3*(IB -IA) + V1 + R2* (IB - IC) + R6 * IB = 0
# V2 + R3*IB -R3*IA + V1 + R2*IB - R2*IC + R6 * IB = 0
# R3*IB + R2*IB  + R6 * IB = -V2 +R3*IA -V1 + R2*IC
# IB = -V2 +R3*IA -V1 + R2*IC
top =(-V2 +R3*IA -V1 + R2*IC)
buttom =(R3 + R2 + R6)
IB = top/buttom
print(top)
print(buttom)
print(IB)