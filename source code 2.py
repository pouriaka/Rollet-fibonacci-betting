import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from random import randint
from time import  sleep



def shartbandi(max_win):
    ending_win = 0
    shomarandeie_mahdodiat_miz = 0
    # fibo value
    z_1 = 1
    z_2 = 1
    tedad_dast = 0
    a = randint(1, 3)

    while tedad_dast <= 10000:
        if max_win > 0:
            tedad_dast += 1
            # chance value
            b = randint(1, 3)
            if a == b:
                max_win = max_win  +  z_2 * 3
                ending_win = max_win
                shomarandeie_mahdodiat_miz = 0
                a = randint(1, 3)

            else:
                if shomarandeie_mahdodiat_miz <= 20 :
                    max_win = max_win - z_2
                    z_3 = z_1 + z_2
                    z_1 = z_2
                    z_2 = z_3
                    shomarandeie_mahdodiat_miz += 1
                    #print('adad bara bar ast ba' + str(z_2))
                    #sleep(5)
                else:
                    z_1 = 1
                    z_2 = 1
                    a = randint(1, 3)
        else:
            break

    return ending_win


#sakhtan jameae amari
borde_ghomarbazan = []
for i in range(0,10000):
    borde_ghomarbazan.append(shartbandi(1000))

borde_ghomarbazan.sort()

min_bord = min(borde_ghomarbazan)
max_bord = max(borde_ghomarbazan)

Miane = len(borde_ghomarbazan) // 2
charake_aval = len(borde_ghomarbazan) // 4
charake_sevom = (len(borde_ghomarbazan) // 2) + (len(borde_ghomarbazan) // 4)
print('charake aval barabar ast ba :' + str(borde_ghomarbazan[charake_aval]))
print('miane barabar ast ba :' + str(borde_ghomarbazan[Miane]))
print('charake sevom barabar ast ba :' + str(borde_ghomarbazan[charake_sevom]))
print(borde_ghomarbazan)
print(min_bord,max_bord)




