rodne_cislo = input('Zadej rodne cislo: ')


def format(rodne_cislo):
    if len(rodne_cislo)==11 and rodne_cislo[6] == '/':
        #chybi zjisteni, jestli jsou kolem lomitka cisla
        return('true')
    else:
        return('false')

def delitelnost(rodne_cislo):
    pomocny = rodne_cislo[:6] + rodne_cislo[7:]
    if int(pomocny) % 2 == 0:
        return('true')
    else:
        return('false')

def datum_naroz(rodne_cislo,pohlavivysledek):
    rok='19'+ rodne_cislo[:2]
    mesic=rodne_cislo[2:4]
    den=rodne_cislo[4:6]
    if pohlavi(rodne_cislo) == 'zena':
        mesic=int(mesic)
        mesic= mesic-50
        if mesic < 10:
            me=str(mesic)
            mesic='0'+me
        else:
            mesic=str(mesic)
        datum=[]
        datum=den+'.'+mesic+'.'+rok
        return(datum)
    else:
        datum=[]
        datum=den+'.'+mesic+'.'+rok
        return(datum)


def pohlavi(rodne_cislo):
    rok=int(rodne_cislo[2])
    if rok-5 < 0:
        return('Muz')
    else:
        return('Zena')


format_vysl=format(rodne_cislo)
delitelnost_vysl=delitelnost(rodne_cislo)
pohlavi_vysl=pohlavi(rodne_cislo)
datum_naroz_vysl=datum_naroz(rodne_cislo,pohlavi_vysl)

def testRC (rodne_cislo):
    if format_vysl == 'false' or delitelnost_vysl == 'false':
        return ('Chybne zadane rodne cislo!')
    else:
        datum=[]
        datum= pohlavi_vysl+', datum narozeni: '+datum_naroz_vysl
        return (datum)

print(testRC(rodne_cislo))
