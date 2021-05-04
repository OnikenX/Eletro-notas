import numpy as np
from si_prefix import si_format as si

#                                                                                                                                                        .
#                                                                                                                                                .c:;c. .o
#                                                                                                                                                ',  ll .o.;:
#                                                                                                                                                  'c:  .0Ko
#                                                                                                                                                :kxc'' .x.ll.
#                                                                                                                                                ,,,,,,  .  ..
#                                                                                                                                    ....................................
#                                                                                                                                    ooooooooooooooooooooooooooolllllllll
#                                                                                                                                    ooo.............................'lll
#                  ..........oooo;...........;oooc............cooo,...........:ooo;............oooo'...........cooo,...........,oool'ooo.       looo            ;ooo'.lll.......,oool............oooo............looo,...........;oooc............oooo............looo,...........:ooo:....
#                 .oollllllllXXXXklllllllllllxXXX0llllllllllll0XXXxlllllllllllOXXXkllllllllllllXXXXolllllllllll0XXXdllllllllllldXXXKlooo.       XXXX.           oXXX:.lllcccccccdXXX0ccccccccccclXXXXlccccccccccc0XXXdcccccccccccxXXXOccccccccccclXXXXccccccccccccKXXXdccccccccccckXXXkclll.
#                 dOOk.......;;;;'............;;;,............,;;;............';;;.............;;;;............,;;;.............;;;;.ooo.       ;;;;            ';;;..lll.      ';;;,           .;;;;.           ,;;;'           ';;;,           .;;;;            ;;;;.           ';;;' ,ll.
#                 XXXX                                                                                                               ooo'............................'lll                                                                                                               'll.
#                 lkko                                                                                                               oooooooooooooooooooooooooolollllllll                                                                                                               'll.
#                 .oo.                                                                                                               ....................................                                                                                                               :dd'
#                 .oo.                                                                                                                                                                                                                                                                 .XXX0
#                 .oo.                                                                                                                                                                                                                                                                 .0KKk
#                 .oo.                                                                                                                                                                                                                                                                  ,oo.
#                 .oo.                                                                                                                          .,....'  .'...                                                                                                                          'll.
#                 oOOo                                                                                                                          'l    dl ;;.'.                                                                                                                          'll.
#                 XXXX                                                                                                                          'd...;:. .'..;,                                                                                                                         'll.
#                 dOOd                                                                                                                          'l   ;;  ..  ;:                                                                                                                         'll.
#                 .oo.                                                                                                                          .'    ,.  '...                                                                                                                          ;oo.
#                 .oo.                                                                                                                                                                                                                                                                 .0KKO
#                 .oo.                                                                                                                                                                                                                                                                 .KXXO
#                 .oo.                                                            '.  .d                                                                                                                            ',,.  x.                                                            :dd'
#                 .oo.                                                           'x:  .X  '.                                                                                                                       ,,''x  W..;'                                                         'll.
#                 ckkl                                                            c:  .X'dl                                                                                                                          .:l  Wcd;                                                          'll.
#                 XXXX                                                            lc  .N;ol.                                                                                                                       .:;,   Wloc.                                                         'll.
#                 x00k                                                          .;ll;;.d  .:                                                                                                                       l:;;;  x. :l                                                         'll.
#                 .oo.                                              ...................................                                                                                                .................    .                                                           ,oo.
#                 .oo.                                             'lllllllllllllllllllllllllllllllllll.                                                                                              'lllllllllllllllllllllllllllllllllll.                                            .O00x
#                 .oo.                                             'ooc'''''''''''''''''''''''''''''loo.                                                                                              'ooc''''''''''''''''''''''''''''.;ll.                                            .XXX0
#                ,kXXk;        .'''.            ''''            '''coo;         .'''.            '''ooo'         ''''            .'''.           .'',dOOx,       .'''.            ''''            '''',oo:        .'''.            ''''.ll.        ''''            .'''.            '''lNWWK'
#                WMMMMWoccccccckXXXkcccccccccccoXXXKccccccccccccXXXXdo:         oXXX:           'XXXKooc:::::::::XXXXc:::::::::::OXXXd:::::::::::dXXWMMMMX:::::::OXXXd:::::::::::cXXXX::::::::::::KXXXoooc        :XXXo           .XXXK'llc::::::::KXXXl:::::::::::kXXXk:::::::::::oXXNMMMMMN
#                0MMMMK;'''''''lxxxl''''''''''':xxxd''''''''''''xxxOdo;         :xxx,           .xxxOoo:'''''''''xxxx,'''''''''''oxxxc'''''''''''cxxOWMMMk'''''''oxxx:''''''''''',xxxx''''''''''''dxxxloo:        ,xxx:           .xxxd'll;''''''''dxxx:'''''''''''lxxxl''''''''''':xxkXMMMMO
#                 xKKk.                                            'oo;         .....           ....coo.                                             ckkx                                             ,oo:        .....           .....'ll.                                            .lkk;
#                 XXXX                                             'oollclccccccccccccccccccccccccccloo.                                             'ooc                                             'oolccccccccccccccccccccccccccccccll.                                             cdd,
#                 k00k                                             .'''''''''''''''''''''''''''''''''''.                                             'ooc                                             .'''''''''''''''''''''''''''''''''''                                             .XXX0
#                 .oo.                                                                                                                               'ooc                                                                                                                              .0KKk
#                 .oo.                                                                                                                               'ooc                                                       ;'...'.    .;                                                           ,oo.
#                 .oo.                                                         l;''';,  .';.                                                         ;ddo                                                       0,   .k.  .:O.                                                          'll.
#                 .oo.                                                         0,   .O. ..;;                                                         kXXK.                                                      0c..;,:  ,; O.                                                          'll.
#                 .oo.                                                         0c''lc,    ,;                                                         xKKK.                                                      0,  ,l' ;c''O:.                                                         'll.
#                 ;xx:                                                         0,  .:;  ..cc.                                                        ,ddl                                                       ;.   .,     ;.                                                          'll.
#                 XXXX                                                         '     .  '''''.                                                       'ooc                                                                                                                               ;dd.
#                 OKKO                                                                                                                               'ooc                                                                                                                              .KKKO
#                 .oo'                                                                                                                               'ooc                                                                                                                              .KKKO
#                 .oo.                                                                                                                               'ooc                                                                                                                               ;dd'
#                 .oo.                                                                                                                               ,ool                                                                                                                               'll.
#                 .oo.                                                                                                                         .;;;;;OKKKc;;;;.                                                                                                                   ;;;;;;cll:;;;;;,
#                 .oo.                                                                                                                         ,oo:;;0KKKl;:oo.                                                                                                                   lll:;;;;;;;;lllc
#                 ,dd;                                                                                                                         ,oo.  ....  .oo.                                                                                                                   lll.        lllc
#                 KXXK                                                                                                                         ,ll.        .ll.                                                                                                                   lll.  '''.  lllc
#                 OKK0                                                                                                                         ,ll.        .ll.                                                                                                                   lll. .XXX0  cllc
#                 ,dd,                                                                                                                         'll.        .ll.                                                                                                                   lll. .xxxd  cllc
# .:ccccccccccccccloolccccccccccccccc,                                                                                                         'll.        .ll.                                                                                                                   lll.        cllc
# .,,,,,,,,,,,,,,,,,;,,,,,,,,,,,,,,,,.                                                                                                         'll.  ....  .ll.    ...   ,                                                                                                        lll.        cllc     '   .:
#                                           ;.    c. .,l           ;'',. ;.    c.                                                              'll.  kXXX. .ll.   dc;cO  k  .'                                                                                                    lll.        cllc   .cM.  cX  ,.
#                                           .c   ,:  ..0.  ......  ...:, .c   ,:                                                               'll.  okkk. .ll.   .  ;x  k;c:'                                                                                                    lll.        cllc     M.  cX.:;.
#       .;;;;;;;;;::c:;;;;;;;;;'             ,:  l    .0.  ......   .,:;  ,:  l                                                                'll.        .ll.   .:c,   Kok'                                                                                                     lll.        cllc     M.  cNcd
#       .,,,,,,,,,KKKK;,,,,,,,,.              l:o.   .,0,. ...... .,..,l   l:o.                                                                'll.        .ll.   do,''. l .l;                                                                                                    lll.  ....  cllc   .,0;' ;x .l.
#                 KXXK                         ..    .'''.         ....     ..                                                                 'll.        .ll.                                                                                                                   lll. .KKK0  cll:
#                 ,oo,                                                                                                                         'll.        .ll.                                                                                                                   lll. .OOOx  cll:
#                 .ll.                                                                                                                         'll.        .ll.                                                                                                                   lll.        cll:
#                 .ll.                                                                                                                         'll.  ....  .ll.   o;...':  ,'.':                                                                                                  lll.        cll:        ;'...,;  ,..';
#                 .ll.                                                                                                                         'll;,,OKKKc,;ll.   0,   .O. .  .x                                                                                                  lll;,,,,,,,,lll:        c.   'O.   .;:
#                 .ll.                                                                                                                         .,,,,,OKKKc,,,,.   0c..cl'   .''                                                                                                   ,,,,,,:ll;,,,,,,        c,..;l.    .,l
#                 .ll.                                                                                                                               ,ooc         0,   :l .do,''.                                                                                                       'll.              c.   l: .l,';l
#                 O00O                                                                                                                               .ll:         .     .  .....                                                                                                        ;oo.              .     .   ...
#                 XXXX                                                                                                                               .ll:                                                                                                                              .0KKO
#                 ;dd;                                                                                                                               .ll:                                                                                                                              .KKKO
#                 .ll.                                                                                                                               .ll:                                                                                                                               ;oo'
#                 .ll.                                                                                                                               ,ooc                                                                                                                               'll.
#                 .ll.                                                                                                                               xKK0.                                                                                                                              'll.
#                 .ll.                                                                                                                               kXXX.                                                                                                                              'll.
#                 .ll.                                                                                                                               ;ddo                                                                                                                               'll.
#                 k00k                                                                                                                               .ll:                                                                                                                               ,ll.
#                 XXXX                                                                                                                               .ll:                                                                                                                              .O00x
#                 :xxc                                                                                                                               .ll:                                                                                                                              .XXX0
#                 .ll.                                                                                                                               .ll:                                                                                                                               cdd,
#                 .ll.                                                                                                                               :kxd                                                                                                                               'll.
#                 .ll;..lxxx;...........'xxxd............dxxx;...........cxxxc...........,xxxd............dxxx,...........cxxxc...........;xxxo.....lWMMMk..lxxx:...........:xxxl...........,xxxd............oxxx;...........cxxxc...........,xxxd............dxxx,...........cxxx:.....;ll.
#                 .:::::OXXXd:::::::::::cXXXX::::::::::::KXXXo:::::::::::xXXXk:::::::::::lXXXK::::::::::::KXXXl:::::::::::kXXXx:::::::::::oXXX0:::::KMMMMX::OXXXd:::::::::::dXXXO:::::::::::cXXXX::::::::::::0XXXo:::::::::::xXXXk:::::::::::lXXXK::::::::::::KXXXl:::::::::::kXXXx:::::::;
#                       .'''.            ''''            ''''.           .'''.            ''''            ''''            .'''.           .'''.     .kXXK,  .'''.           .'''.            ''''            .'''.           .'''.            ''''            ''''            .'''.
#                                                                                                                                                    .ll:
#                                                                                                                                                    .ll:
#                                                                                                                                                    .ll:
#                                                                                                                                                    .ll:
#                                                                                                                                                    .ll:
#                                                                                                                                                    oOOk.
#                                                                                                                                                    OXXX.
#                                                                                                                                                    cxxx.
#                                                                                                                                                    .ll:
#                                                                                                                                                    .ll:
#                                                                                                                                                    .ll:
#                                                                                                                                                    .ll:
#                                                                                                                                                    .ll:
#                                                                                                                                           .........,llc.........
#                                                                                                                                          .cccccccccclllccccccccc.
#                                                                                                                                           ......................
#                                                                                                                                               ',,,,,,,,,,,,'
#                                                                                                                                              .;;;;;;;;;;;;;;
#                                                                                                                                                   ......
#                                                                                                                                                  .cllllc
#                                                                                                                                                   ......
#
#

R1 = R3 = 1000  # ohm
R2 = R4 = R5 = 2000  # ohm
V1 = 3  # v
# a)
A = np.array([[R1 + R2, -R2, -R1], [-R2, R3 + R2 + R4, -R4], [-R1, -R4, R4 + R1 + R5]])
b = np.array([V1, 0, 0])
X = np.linalg.solve(A, b)
print("8.\na)\ni1 = {}A\ni2 = {}A\ni3 = {}A".format(si(X[0]), si(X[1]), si(X[2])))
print("a potencia fornecida é de {}W".format(si(X[0]*V1)))

# b)

