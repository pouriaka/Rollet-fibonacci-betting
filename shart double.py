import random

"""
dar tabe shartbandi  pool shoro shart vared va charak mi shavad
ke charak meghdar hadaf ast va vaghti ghomar baz be in meghdar az 
bord beresad motevaghef mi shavad

dar thabe shart bandi chand dafeii tedad dafati ke ghomar baz 
mitavanad hesabash ra az sefr sharj konad vared mi shavad

"""



def shartbandi(max_win , charak):

    tedad_dast_shart_bastan = 0

    # fibo value
    za_1 = 1
    za_2 = 1
    a = random.sample(range(1,6), 2)
    #a = [1 , 2]
    zc_1 = 1
    zc_2 = 1
    c = random.sample(range(1,6), 2)
    #c = [3 , 4]

    if ( a[0] == c[0] or a[0] == c[1] ) and (a[1] == c[0] or a[1] == c[1]):
        while ( a[0] == c[0] or a[0] == c[1] ) and (a[1] == c[0] or a[1] == c[1]) :
            c = random.sample(range(1,6),2)


    else:
        pass


    while max_win > 0 :
        if max_win <= charak :
            # chance value
            b = random.randint(1,6)
            #print('maxwin:',max_win)
            #print('a:',a,'c:',c,'b:',b)
            #print('za_1 =', za_1 , 'za_2 =', za_2)
            #print('zc_1 =', zc_1, 'zc_2 =', zc_2)
            tedad_dast_shart_bastan += 1


            #halat bord va jam kardane pool az a
            if a[0] == b or a[1] == b:
                max_win = max_win  +  za_1 * 3
                za_1 = 1
                za_2 = 1
                a = random.sample(range(1, 6), 2)

                if (a[0] == c[0] or a[0] == c[1]) and (a[1] == c[0] or a[1] == c[1]):
                    while (a[0] == c[0] or a[0] == c[1]) and (a[1] == c[0] or a[1] == c[1]):
                        a = random.sample(range(1, 6), 2)
                else:
                    pass

            #halate bakht va edame shart bandi az a
            else:
                if  za_2 <= 5 :
                    max_win = max_win - za_1
                    za_3 = za_1 + za_2
                    za_1 = za_2
                    za_2 = za_3


                else:
                    max_win = max_win - za_1
                    za_1 = 1
                    za_2 = 1

                    a = random.sample(range(1, 6), 2)

                    if (a[0] == c[0] or a[0] == c[1]) and (a[1] == c[0] or a[1] == c[1]):
                        while (a[0] == c[0] or a[0] == c[1]) and (a[1] == c[0] or a[1] == c[1]):
                            c = random.sample(range(1, 6), 2)
                    else:
                        pass

            # halat bord va jam kardane pool az c
            if c[0] == b or c[1] == b:
                max_win = max_win + zc_1 * 3

                zc_1 = 1
                zc_2 = 1

                c = random.sample(range(1, 6), 2)

                if (a[0] == c[0] or a[0] == c[1]) and (a[1] == c[0] or a[1] == c[1]):
                    while (a[0] == c[0] or a[0] == c[1]) and (a[1] == c[0] or a[1] == c[1]):
                        c = random.sample(range(1, 6), 2)
                else:
                    pass


            # halate bakht va edame shart bandi az a
            else:
                if zc_2 <= 5:
                    max_win = max_win - zc_1
                    zc_3 = zc_1 + zc_2
                    zc_1 = zc_2
                    zc_2 = zc_3


                else:
                    max_win = max_win - zc_1
                    zc_1 = 1
                    zc_2 = 1

                    c = random.sample(range(1, 6), 2)

                    if (a[0] == c[0] or a[0] == c[1]) and (a[1] == c[0] or a[1] == c[1]):
                        while (a[0] == c[0] or a[0] == c[1]) and (a[1] == c[0] or a[1] == c[1]):
                            c = random.sample(range(1, 6), 2)
                    else:
                        pass

        else:

            return True , tedad_dast_shart_bastan
            break

    return False , tedad_dast_shart_bastan




def shartbandi_chand_dafeii():
    tedad_dafe_varedkardan_1000dolar = 0
    majmo_dast_har_fard = 0


    while True:
        a = shartbandi(200 , 500)
        majmo_dast_har_fard += a[1]



        if a[0] == False:
            tedad_dafe_varedkardan_1000dolar += 1

        else:
            return tedad_dafe_varedkardan_1000dolar , majmo_dast_har_fard
            break



#sakhtan jameae amari
borde_ghomarbazan = []
sum_dast = 0
tedad_jame_amari_ghomar_bazan = 1000

for i in range(0,tedad_jame_amari_ghomar_bazan):

    borde_ghomarbazan.append(shartbandi_chand_dafeii())

borde_ghomarbazan.sort()
for i in range(0,tedad_jame_amari_ghomar_bazan):

    sum_dast += borde_ghomarbazan[i][1]
miangin_dast = sum_dast / tedad_jame_amari_ghomar_bazan
print(borde_ghomarbazan)
print('miangin dast:',miangin_dast)




#peida kardane tedad afradi ke az in algoritm tamam pool khod ra az dast dadan
afrad_mal_bakhte = 0
max_mojaz_besarfe = 1
for j in range(0 , len(borde_ghomarbazan)):
    if borde_ghomarbazan[j][0] < max_mojaz_besarfe :
        pass
    else:
        afrad_mal_bakhte += 1

print('tedad afrade mal bakhte =',afrad_mal_bakhte)




min_bord = min(borde_ghomarbazan)
max_bord = max(borde_ghomarbazan)

Miane = len(borde_ghomarbazan) // 2
charake_aval = len(borde_ghomarbazan) // 4
charake_sevom = (len(borde_ghomarbazan) // 2) + (len(borde_ghomarbazan) // 4)
bishtar_az_90darsad = (len(borde_ghomarbazan) // 2) + (len(borde_ghomarbazan) // 4) + (len(borde_ghomarbazan) // 7)
print('charake aval barabar ast ba :' + str(borde_ghomarbazan[charake_aval]))
print('miane barabar ast ba :' + str(borde_ghomarbazan[Miane]))
print('charake sevom barabar ast ba :' + str(borde_ghomarbazan[charake_sevom]))
print('bishtar az 90 darsade afrad :', str(borde_ghomarbazan[bishtar_az_90darsad]))
print('minimom dafe sherkat barabar ast ba:',min_bord,'maximom dafe sherkat barabar ast ba:',max_bord)






