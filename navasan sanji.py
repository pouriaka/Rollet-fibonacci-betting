import random




def shartbandi(max_win , charak):

    tedad_dast_shart_bastan = 0
    maxwin_list = []

    # fibo value
    za_1 = 1
    za_2 = 1
    a = [1 , 4 , 7]

    zc_1 = 1
    zc_2 = 1
    c = [2 , 5 , 8]

    zd_1 = 1
    zd_2 = 1
    d = [1 , 2 , 3]

    ze_1 = 1
    ze_2 = 1
    e = [4 , 5 , 6]



    while max_win > 0 :
        if max_win <= charak :
            # chance value
            b = random.randint(1,9)
            maxwin_list.append(max_win)
            #print('maxwin:',max_win)
            #print('a:',a,'c:',c,'b:',b)
            #print('za_1 =', za_1 , 'za_2 =', za_2)
            #print('zc_1 =', zc_1, 'zc_2 =', zc_2)
            tedad_dast_shart_bastan += 1


            #halat bord va jam kardane pool az a
            if a[0] == b or a[1] == b or a[2] == b:
                max_win = max_win  +  za_1 * 3
                za_1 = 1
                za_2 = 1

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


            # halat bord va jam kardane pool az c
            if c[0] == b or c[1] == b or c[2] == b:
                max_win = max_win + zc_1 * 3

                zc_1 = 1
                zc_2 = 1



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

            if d[0] == b or d[1] == b or d[2] == b:
                max_win = max_win + zd_1 * 3

                zd_1 = 1
                zd_2 = 1



            # halate bakht va edame shart bandi az a
            else:
                if zd_2 <= 5:
                    max_win = max_win - zd_1
                    zd_3 = zd_1 + zd_2
                    zd_1 = zd_2
                    zd_2 = zd_3


                else:
                    max_win = max_win - zd_1
                    zd_1 = 1
                    zd_2 = 1

            if e[0] == b or e[1] == b or e[2] == b:
                max_win = max_win + ze_1 * 3

                ze_1 = 1
                ze_2 = 1



            # halate bakht va edame shart bandi az a
            else:
                if ze_2 <= 5:
                    max_win = max_win - ze_1
                    ze_3 = ze_1 + ze_2
                    ze_1 = ze_2
                    ze_2 = ze_3


                else:
                    max_win = max_win - ze_1
                    ze_1 = 1
                    ze_2 = 1




        else:

            return maxwin_list
            break

    return maxwin_list
a = []
for i in range (1,10000):
    a.append(min(shartbandi(200,500)))


a.sort()
print(a)
Miane = len(a) // 2
charake_aval = len(a) // 4
charake_sevom = (len(a) // 2) + (len(a) // 4)
bishtar_az_90darsad = (len(a) // 2) + (len(a) // 4) + (len(a) // 7)
print('charake aval barabar ast ba :' + str(a[charake_aval]))
print('miane barabar ast ba :' + str(a[Miane]))
print('charake sevom barabar ast ba :' + str(a[charake_sevom]))
print('bishtar az 90 darsade afrad :', str(a[bishtar_az_90darsad]))


print('avrage min:',sum(a)/len(a))
print('min min :',min(a))




