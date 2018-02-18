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

#definice vyjimek psanych odcitanim
#if cislo is in vyjimky: #tech je tuna, nebo to nechapu..

    while cislo >= 1000:
        cislo=cislo-1000
        prevedene.append('M')

    while cislo >= 500:
        cislo=cislo-500
        prevedene.append('D')

    while cislo >= 100:
        cislo=cislo-100
        prevedene.append('C')

    while cislo >= 50:
        cislo=cislo-50
        prevedene.append('L')

    while cislo >= 10:
        cislo=cislo-10
        prevedene.append('X')

    prevedene.append(prevod[cislo])
    prevedene = ''.join(str(znak) for znak in prevedene)
    return prevedene


if overeni_zaporu(cislo) == False:
    print('Zaporne nelze prevadet')
else:
    prevedene_cislo=(prevadeni(cislo))
    print(prevedene_cislo)
