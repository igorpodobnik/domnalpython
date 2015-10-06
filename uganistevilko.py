__author__ = 'igorpodobnik'
import random
global igralec
rezultat = 1
steviloposkusov = 1
ponovi = 1
steviloiger = 0
rekord = 100
stevilovsehposkusov = 0
"""enasteviloiger = 0
enastevilovseh = 0
enarekord = 11
dvasteviloiger = 0
dvastevilovseh = 0
dvarekord = 11"""
# DEFINICIJA LISTE
steviloigerodi = []
stevilovsehodi = []
rekordodvseh = []
k = raw_input("Koliko jih hoces?")
stigralc = int(k)
for i in range(0,stigralc):
    steviloigerodi.insert(i , 0)
    stevilovsehodi.insert(i , 0)
    rekordodvseh.insert(i, 11)
while ponovi == 1:
    i = raw_input("Izberite igralca z vnosom stevilke od 1 do %s: " % stigralc)
    igralec = int(i)
    igralec -= 1
    cifra = random.randrange(1000)
    #print(cifra)
    print("Ugani skrito stevilko!!!")
    vnos1 = raw_input("Zacni z vnosom prve stevilke med 0 in 1000: ")
    vnos = int(vnos1)
    while rezultat == 1:
        if vnos < cifra:
            print("Vecja je!!!")
            vnos1 = raw_input("Zacni z vnosom nove stevilke med 0 in 1000: ")
            vnos = int(vnos1)
            steviloposkusov += 1
            if vnos == cifra:
                rezultat = rezultat + 2
                print("---BRAVO--- Rabili ste %s poskusov" % steviloposkusov)
            elif steviloposkusov == 10:
                print("Zal, ni vec poskusov!")
                rezultat += 3
        elif vnos > cifra:
            print("Manjsa je!!!")
            vnos1 = raw_input("Zacni z vnosom nove stevilke med 0 in 1000: ")
            vnos = int(vnos1)
            steviloposkusov += 1
            if vnos == cifra:
                rezultat = rezultat + 2
                print("---BRAVO--- Rabili ste %s poskusov" % steviloposkusov)
            elif steviloposkusov == 10:
                print("Zal, ni vec poskusov!")
                rezultat += 3
        else:
            rezultat = rezultat + 2
            print("---BRAVO--- Rabili ste %s poskusov" % steviloposkusov)
            steviloiger = steviloiger + 1

    nadaljuj = raw_input("Bi rad nadaljeval z igro? Ce ne, potem vpisi Ne: ")
    """if igralec == "1":
        enasteviloiger = enasteviloiger + 1
        enastevilovseh = enastevilovseh + steviloposkusov
        if enarekord > steviloposkusov:
            enarekord = steviloposkusov
    else:
        dvasteviloiger = dvasteviloiger + 1
        dvastevilovseh = dvastevilovseh + steviloposkusov
        if dvarekord > steviloposkusov:
            dvarekord = steviloposkusov """
    # PROBLEM
    steviloigerodi[igralec] += 1
    stevilovsehodi[igralec] += steviloposkusov
    if rekordodvseh[igralec] >  steviloposkusov:
        rekordodvseh[igralec] = steviloposkusov
    if nadaljuj == "Ne":
        ponovi = 2

    else:
        ponovi = 1
        rezultat = 1
        steviloposkusov = 1

print(" ")
"""print("Stevilo iger ki ste jih odigrali Igralec 1 je %s" % enasteviloiger)
print("Stevilo iger ki ste jih odigrali Igralec 2 je %s" % dvasteviloiger)
print("Stevilo vseh poskusov Igralca 1 je %s" % enastevilovseh)
print("Stevilo vseh poskusov Igralca 2 je %s" % dvastevilovseh)
print("Rekord Igralca 1 je bil %s poskusov" % enarekord)
print("Rekord Igralca 2 je bil %s poskusov" % dvarekord)"""
#print teh rezultatov.
for i in range(0,stigralc):
    print(" Igralec %s : Stevilo iger je %s" % (i + 1, steviloigerodi[i]))
    print(" Igralec %s : Stevilo poskusov je %s" % (i + 1, stevilovsehodi[i]))
    print(" Igralec %s : Rekord je %s" % (i + 1, rekordodvseh[i]))
