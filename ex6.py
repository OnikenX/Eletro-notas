import os

import numpy as np
from si_prefix import si_format
from si_prefix import si_format as si

#
#
#                                                                                            .,.     x.
#                                                                                           ::Kk     W;   .'
#                                                                                           . kk     W; .co,
#                                                                                             kk     Wl kk
#                                                                                             kk     Wx ok'
#                                                                                          .;;00 ;;  W;  ,kl
#                                                                                          .,,,, ,,  ,.    ,
#
#                                                                        ... ...... ...... ..... ...... ...... ...... ......
#                                                                        lll llllll llllll lllll llllll llllll llllll llllll .
#                                                                        lll :;;;;; ;;;;;; ;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;lll .
#                                                                        lll ,                                          'lll .                                          ....
#                         .. ..... ...... ...... ...... ...... ...... ...lll ,                                          'lll ...... ...... ...... ...... ...... ..... ,kKXXK x'.... ...... ...... ...... ...... ...... ....
#                        ,cc ccccc cccccc cccccc cccccc cccccc cccccc ccclll ;                                          ;lll cccccc cccccc cccccc cccccc cccccc ccccc XMMMMM MKcccc cccccc cccccc cccccc cccccc cccccc cclc.
#                        :ll lllll llllll llllll llllll llllll llllll llllll ;                                          ;lll llllll llllll llllll llllll llllll lllll NMMMMM MKllll llllll llllll llllll llllll llllll llll'
#                        ;ll l.... ...... ...... ...... ...... ...... ...lll ,                                          'lll ...... ...... ...... ...... ...... ..... :0WMMW 0;.... ...... ...... ...... ...... ...... 'lll.
#                        ;ll l                                           lll ,                                          'lll .                                         .dxxo                                           .lll.
#                        ;ll l                                           lll :;;;;; ;;;;;; ;;;;; ;;;;;; ;;;;;; ;;;;;; ;;:lll .                                          cll:                                           .lll.
#                        ;ll l                                           lll llllll llllll lllll llllll llllll llllll llllll .                                          cll:                                           .lll.
#                        ;ll l                                           ''' '''''' '''''' ''''' '''''' '''''' '''''' ''''''                                            cll:                                           .lll.
#                        ;ll l                                                                                                                                          cll:                                           .lll.
#                        ;ll l                                                                                                                                          cll:                                           .lll.
#                        ;ll l                                                                                                                                          cll:                                           .lll.
#                        ;ll l                                                                                                                                          cll:                                           .lll.
#                        ;ll l                                                                                                                                . ..... ..lllc ...... ..                        . ...... ,lll;. ..... .
#                        ;ll l                                                                                                                                ' lllll llllll llllll l.                        c llllll llllll lllll l
#                        ;ll l                                                           ' ;;;;, .    , .                                                     ' lll,, ,,,;;, ,,,,ll l.                        c llc,,, ,;:;,, ,,:ll l
#                        ;ll l                                                           o l...' o. .'o :                                                     ' lll.            .ll l.                        c ll:             ;ll l
#                        ;ll l                                                           o l...' l.   : :                                                     ' lll.            .ll l.                        c ll:             ;ll l
#                        ;ll l                                                           o l..:x .    : :                                                     ' lll.            .ll l.                        c ll:             ;ll l
#                        ;ll l                                                           o ;   l c    : :                                                     ' lll.            .ll l.                        c ll:             ;ll l
#                        ;ll l                                                           ; .     :. ..: :..                                                   ' lll.            .ll l.                        c ll:             ;ll l
#                        ;ll l                                                                                                                                ' lll.            .ll l.                        c ll:             ;ll l
# .',,, ,,,,,, ,,,,,, ,,,cll l,,,, ,,,,,, ,,,,,, ,,,.                                                                                                         ' lll.            .ll l.                        c ll:             ;ll l
# :llll llllll llllll llllll lllll llllll llllll lllc                                                                                                         ' lll.            .ll l.                        c ll:             ;ll l
# .'''' '''''' '''''' '''''' ''''' '''''' '''''' '''.                                                                                                         ' lll.            .ll l.       ',     x.        c ll:             ;ll l       .,.    .k
#                                                                                                                                                             ' lll.            .ll l.     ,:xN     W;   .'   c ll:             ;ll l      ::W:    .M    '.
#                                                                                                                                                             ' lll.            .ll l.     . :N     W; . Ol   c ll:             ;ll l      . N:    .M  ; 0;
#                                                                                                                                                             ' lll.            .ll l.       :N     Wccd ;    c ll:             ;ll l        N:    .M'oo '
#          ',, ,,,,,, ,,,,,; ,,,,, ,,,,,, ,,.                                                                                                                 ' lll.            .ll l.       :N     Wxok '    c ll:             ;ll l        N:    .Moxd .
#         .:cc cccccc ccclll lcccc cccccc c:.                                                                                                                 ' lll.            .ll l.     ;;xW;; . W; , kl   c ll:             ;ll l    . ;;Wx;;  .M. : k:
#          ... ...... ...:ll l.... ...... ..                                                                                                                  ' lll.            .ll l.     llllll . l.   .l.  c ll:             ;ll l    , llllll   l    'c
#                        ;ll l                                                                                                                                ' lll.            .ll l.                        c ll:             ;ll l
#                        ;ll l                                                                                                                                ' lll.            .ll l.                        c ll:             ;ll l
#                        ;ll l                                                                                                                                ' lll.            .ll l.                        c ll:             ;ll l
#                        ;ll l                                                                                                                                ' lll.            .ll l.      ;;;;; '    , ;,.  c ll:             ;ll l
#                        ;ll l            c      ;. .'c .             .,:    c      ;.                                                                        ' lll.            .ll l.      O;... ,o  :' .'o  c ll:             ;ll l      ...... .   .. ..
#                        ;ll l            ;o   . d  ..x .   .. ....   .'x    ;o   . d                                                                         ' lll.. ...... ....ll l.      O;..' ,l      'o  c ll:... ...... ..;ll l      ;d...' c' .:' .;l
#                        ;ll l             l: .d .    x .   .. ....    .x     l: .d .                                                                         ' lllcc cccllc ccccll l.      O;..l o    ' ,'   c llcccc ccllcc cccll l      ;d...' c'   . '::
#                        ;ll l              k c:      x .  .;; ;;;'    .x      k c:                                                                           ' lllcl llllll clllcl l.      O.    d,  ::      c llclll llllll llcll l      ;x;;ck .    . :c;
#                        ;ll l              ;lo     ..k :.  .. .... . .:k..    ;lo                                                                              ..... ..cllc ...... .       l     .:  c, ...  . ...... 'lll,. ..... .      ;o   c :  .'   .k
#                        ;ll l               ..     ... ..          . .....     ..                                                                                      cll:                                           .lll.               .;     :. .;. .',
#                        ;ll l                                                                                                                                          cll:                                           .lll.
#                        ;ll l                                                                                                                                          cll:                                           .lll.
#                        ;ll l                                                                                                                                          cll:                                           .lll.
#                        ;ll l                                                                                                                                          cll:                                           .lll.
#                        ;ll l                                                                                                                                          cll:                                           .lll.
#                        ;ll l                                                                                                                                          cll:                                           .lll.
#                        ;ll l                                                                                                                                         'kOOk .                                         .lll.
#                        :ll l'''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' ''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' ''''' oNMMMM Nl'''' '''''' '''''' '''''' '''''' '''''' ,lll.
#                        cll lllll llllll llllll llllll llllll llllll llllll llllll llllll lllll llllll llllll llllll llllll llllll llllll llllll llllll llllll lllll NMMMMM MXllll llllll llllll llllll llllll llllll llll,
#                        ';: ;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;; 0MMMMM MO;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;;;;; ;;:;.
#                                                                                                                                                                     .lkOOx l.
#
#
#
#
#


R2 = R3 = 2000  # ohm
R1 = 1000  # ohm
V1 = 1  # v

R2R3 = 1 / (1 / R2 + 1 / R3)
Rreq = R2R3 + R1

# corrente do circuito
I1 = V1 / Rreq

# a)
# tensão do R1
V_R1 = V1 * R1 / Rreq


print("a) V_R1: {}V I1: {}A".format(si_format(V_R1), si_format(I1)))

# solução do stor
s_i1 = V1 / (R1 + R2R3)
s_V_R1 = s_i1 * R1
print("s_a) s_V_R1: {}V ; s_i1: {}A".format(si_format(s_V_R1), si_format(s_i1)))
print()

# b)
i1 = I1
# i1 = i2 + i3
# i1 = i2 + i2*R2/R3
# i1*R3 = i2*R3 + i2*R2
# i1*R3 = i2*R3*R2
# i1*R3/R3*R2 = i2

i3 = I1 * R3 / (R2 + R3)
v3 = V1 * R2R3 / Rreq
print("b) i3: {}A v3: {}V".format(si_format(i3), si_format(v3)))
print()

# c)

A = np.array([[1000, 2000, 0], [1, -1, -1], [0, -2000, -2000]])
b = np.array([1, 0, 0])
X = np.linalg.solve(A, b)
print(X)

print(
    "solução do stor c) ir1: {}A ir2: {}A ir3: {}A".format(si(X[0]), si(X[1]), si(X[2]))
)
print("c)")
print(
    "como já sabemos i1 com a formula de ohm (V=I.R) sabemos que a corrente de R1 é {}A".format(
        si_format(i1)
    )
)
print("pelo teorema de kirchhof:")
print("V_R1 = R1*V1/Rreq")
V_R1 = R1 * V1 / Rreq
print("V_R1: {}V".format(V_R1))
print()


# ou como deve ser feito pelo sistema de equalções


# d) Calcule a potência dissipada na resistência R1.
# P=I.V
print("P_R1: {}W".format(si_format(V_R1 * i1)))

# e) Indique como poderia medir a corrente em R1 e a tensão em R3.
# Represente o diagrama elétrico do circuito com os aparelhos de medida.
print("e) file://" + os.getcwd() + "/ex1.e.png")

print("f)")
pr1 = i1 * V_R1


pv1 = V1 * i1
pv2 = (X[1]**2)*R2
pv3 = i3 * v3
print(pv1, pv2, pv3)

