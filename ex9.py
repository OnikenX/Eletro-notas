import numpy as np
from si_prefix import si_format as si

R1 = 4e3
R2 = 6e3
R3 = 1e4
R4 = 1e4
I1 = 5e-3
V1 = 5

# R2
#
A = np.array([
#    i1  i2  i3            currentes/malhas
    [1,   0,             0],   #   I1
    [-R2, R1 + R2 + R3, -R3],  #   I2
    [-R4, -R3,          R4 + R3]])#I3
b = np.array([I1, 0, -V1])  #voltagens
# como já sabemos o valor de i1/currente na
# malha I1 podemso meter uma resistemcia teorica
# de 1 para meter o valor de I1 no campo da voltagem


X = np.linalg.solve(A, b)
for i in range(X.size):
    print("i{} : {}A".format(i+1, si(X[i])))

V_R2 = (X[0]-X[1])*R2
V_R4 = (X[0]-X[2])*R4
V_I1 = (V_R4 + V_R2)
P_I1 = V_I1 * I1
print("V_R2: {}V ; V_R4: {}V ;  V_I1:  {}V ; P_I1: {}W".format( si(V_R2), si(V_R4), si(V_I1), si(P_I1)))