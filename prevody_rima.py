# slovnik
prevod={1:'I',
        2:'II',
        3:'III',
        4:'IV',
        5:'V',
        6:'IV',
        7:'VII',
        8:'VIII',
        9:'IX',
}

cislo=input('Zadej: ')
cislo=int(cislo)

def overeni_zaporu(cislo):
    '''Podiva se, jestli je cislo mensi nez nula, pokud ano, vrati chybu. Chyba je pozdeji odchytavana'''

    if cislo <0:
        return False

def prevadeni(cislo):
    prevedene=[]

    while cislo >= 1000:
        cislo=cislo-1000
        prevedene.append('M')

    if cislo >= 900:
        cislo=cislo-900
        prevedene.append('CM')
    elif cislo >= 500:
        cislo=cislo-500
        prevedene.append('D')
    elif cislo >= 400:
        cislo=cislo-400
        prevedene.append('CD')

    while cislo >= 100:
        cislo=cislo-100
        prevedene.append('C')

    if cislo >= 90:
        cislo=cislo-90
        prevedene.append('XC')
    elif cislo >= 50:
        cislo=cislo-50
        prevedene.append('L')
    elif cislo >= 40:
        cislo=cislo-40
        prevedene.append('XL')

    while cislo >= 10:
        cislo=cislo-10
        prevedene.append('X')

    if cislo > 0:
        prevedene.append(prevod[cislo])

    prevedene = ''.join(str(znak) for znak in prevedene)
    return prevedene


if overeni_zaporu(cislo) == False:
    print('Zaporne nelze prevadet')
else:
    print(prevadeni(cislo))
