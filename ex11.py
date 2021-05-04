import numpy as np
from si_prefix import si_format as si

# temos um circuito com os seguintes valores
V1 = V2 = 1
R1 = R2 = R3 = R4 = 1E3

# e temos de fazer a equivalencia de th sendo que R3 é a resistencia de carga

# primeiro com Vth
# valos primeiro considerar o ponto A
# i1 +i2 + i3 = 0
# i1 = (va - v1) / r1
# i2 = (VA - 0) / R3
# I3 = (VA - V2) /R4
# (VA - V1) / R1 + (VA - 0) / R3 + (VA - V2) /R4 = 0
# (VA - V1 + VA - 0 + VA - V2) /R4 = 0
# VA - V1 + VA - 0 + VA - V2 = 0
# 3VA - V1   - 0  - V2 = 0
# 3VA = V1 + V2
Vth = (V1 + V2)/3
print(f"Vth = {si(Vth)}V")
"boas maltinha"
Rth = 1/(1/R1 + 1/R3 + 1/R4)
print(f"Rth = {si(Rth)}Ω")
Rsum = Rth + R2
I_r2 = Vth/(Rsum)
print(f"I_r2 : {si(I_r2)}A")
# I_r2/2 = Vth/(Rth + R3_novo)
# R3_novo = Vth/I_r2/2 - Rth
R2_novo = Vth / (I_r2 / 2) - Rth
print(f"R3_novo : {R2_novo}Ω")
#1/sum(1/Ri) = Rth

# sabe-se que Vth é a soma das tensões por isso

## agora considerando que o r3 faz parte do circuito a equivalar e como tal o resistencia da carga n está visivel no circuinos nos apresentada

# i1 + i2 + i3 + i4  = 0
# (Vth - V1)/R1 + (Vth - 0)/R2 + (Vth - 0)/R3 + (Vth - V2)/R4 = 0
# Vth - V1 + Vth - 0 + Vth - 0 + Vth - V2 = 0
# 4Vth =  V1 + V2
Vth =  (V1 + V2)/4
print(f"Vth = {si(Vth)}V")
Rth = 1/(1/R1 + 1/R2 +1/R3 + 1/R4)
print(f"Rth = {si(Rth)}V")
from eletro_help import *
Rth = calcRth([R1, R2, R3, R4])
print(f"Rth = {si(Rth)}V")