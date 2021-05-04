import numpy as np
from si_prefix import si_format as si
from eletro_help import *

V1 = 1
I1 = 1E-3
R1 = R4 = 2E3
R2 = R3 = 1E3


# i1 + i2 + i3 = 0
# -I1 + i2 + i3 = 0
# -I1 + (VA - V1)/R4 + (VA -0)/(R2 + R3) = 0
# -I1*(R4)*(R2+R3)/(R4)*(R2+R3) + (VA - V1)*(R2+R3)/R4*(R2+R3) + (VA -0)*R4/(R2 + R3)*R4 = 0
# -I1*(R4)*(R2+R3) + (VA - V1)*(R2+R3) + (VA -0)*R4 = 0
# -I1*(R4)*(R2+R3) + VA*(R2+R3) - V1*(R2+R3) + VA*R4 = 0
#  VA* ((R2+R3) + R4) = V1*(R2+R3) + I1*(R4)*(R2+R3)
Vth  = (V1*(R2+R3) + I1*(R4)*(R2+R3))/((R2+R3) + R4)
print(f"Vth = {si(Vth)}V")
Rth = calcRth([R2+R3, R4])
print(f"Rth = {si(Rth)}Ω")

# i1 + i2 = 0

iI1 = R4/(R1 + (R2+R3)) * I1
print(f"iI1 = {si(iI1)}A")

V_R3 = (R3 * V1) / (R2 + R3 + R4)
print(f"V_R3 = {si(V_R3)}A")
print(f"I_R3  = V_R3 * R3 = {si(V_R3 / R3)}A")

# do lado de a
# i1 + i2 + i3 = 0
# Vth + R6 + V2 = 0




