from random import randint




def shartbandi(max_win):
    ending_win = 0
    shomarandeie_mahdodiat_miz = 0
    # fibo value
    z_1 = 1
    z_2 = 1

    a = randint(1, 3)

    while max_win > 0 and max_win < 1000000:

            # chance value
            b = randint(1, 3)
            #print('a:',a,'b:',b)
            #print('maxwin:',max_win)
            #halat bord va jam kardane pool
            if a == b:
                max_win = max_win  +  z_1 * 3
                ending_win = max_win
                shomarandeie_mahdodiat_miz = 0
                z_1 = 1
                z_2 = 1
                a = randint(1, 3)
            #halate bakht va edame shart bandi
            else:
                if shomarandeie_mahdodiat_miz <= 20 :
                    max_win = max_win - z_1
                    z_3 = z_1 + z_2
                    z_1 = z_2
                    z_2 = z_3
                    shomarandeie_mahdodiat_miz += 1

                else:
                    z_1 = 1
                    z_2 = 1
                    a = randint(1, 3)


    return ending_win


#sakhtan jameae amari
borde_ghomarbazan = []
for i in range(0,100):
    borde_ghomarbazan.append(shartbandi(1000))

borde_ghomarbazan.sort()
print(borde_ghomarbazan)

min_bord = min(borde_ghomarbazan)
max_bord = max(borde_ghomarbazan)

Miane = len(borde_ghomarbazan) // 2
charake_aval = len(borde_ghomarbazan) // 4
charake_sevom = (len(borde_ghomarbazan) // 2) + (len(borde_ghomarbazan) // 4)
print('charake aval barabar ast ba :' + str(borde_ghomarbazan[charake_aval]))
print('miane barabar ast ba :' + str(borde_ghomarbazan[Miane]))
print('charake sevom barabar ast ba :' + str(borde_ghomarbazan[charake_sevom]))

print('minimom bord barabar ast ba:',min_bord,'maximom bord barabar ast ba:',max_bord)




