import numpy as np

V1 = 1
V2 = 6
V3 = -10
R1 = 1894
R2 = 1212
R3 = 1724
IC = -0.628e-3

# IA = ?
# IB = ?
# R4 = ?

# V=IR
# V/I = R

# R1*IA + R2*(IA - IB) = - V1
# R2*(IB - IA)+ R3(IB - IC) +V2 -V3 = 0
# V3 +R3*(IC-IB)+R4*IC = 0

# IA           IB           R4
# IA*(R1+R2) - R2*IB      + 0     = -V1
# -R2*IA     + IB*(R2+R3) + 0     = -V2 + V3 + R3*IC
# 0          - R3*IB      + R4*IC = -V3 - R3*IC

A = np.array([[R1 + R2, R2, 0],
              [-R2, R2 + R3, 0],
              [0, R3, IC]])
b = np.array([-V1, -V2 + V3 + R3 * IC, -V3 - R3 * IC])
x = np.linalg.solve(A, b)
IA = x[0]
IB = x[1]
R4 = x[2]
print(f"IA:{IA} A\nIB:{IB} A\nR4:{R4} Omh")

# R4 = (-V3 -R3*(IC-IB))/IC


# print("R4: ", R4)
# # pela lei das malhas
# A = np.array([[R1+R2, -R2, 0], [-R2, R2+R3, -R3], [0, 0, 1]])
# b = np.array([V1, V2-V3, -0.628])
# X = np.linalg.solve(A, b)
# print("Ix: ", X )
