# -*- coding: utf-8 -*-
__author__ = 'Igor'
#spremenim v float,zaradi deljenja

pogoj = "d"
rezultat = 0
izbire = ["v","r","p","d"]
while pogoj == "d":
    x = raw_input("Vnesi prvo stevilko: ")
    while 1 == 1:
        if x.isdigit():
            x = int(x)
            break
        else:
            x = raw_input("Ni stevilka, probi se enkrat: ")
    y = raw_input("Vnesi drugo stevilko: ")
    while 1 == 1:
        if y.isdigit():
            y = int(y)
            break
        else:
            y = raw_input("Ni stevilka, probi se enkrat: ")


    print("Pritisni V za vsoto")
    print("Pritisni R za razliko")
    print("Pritisni P za produkt")
    print("Pritisni D za deljenje")
    operacija = raw_input("Vasa izbira je: ").lower()
    while 1==1:
        if operacija in izbire:
            break
        else:
            operacija = raw_input("Dej dej, se enkrat probaj, V, R, P ali D: ")



    if operacija == "r":
        rezultat =  x - y
    elif operacija == "v":
        rezultat = x + y
    elif operacija == "p":
        rezultat = x * y
    elif operacija == "d":
        # DODAJ CE JE NICLA
        x = x + 0.0
        y = y + 0.0
        rezultat = x/y

    print ("Vas rezultat je: %s" % rezultat)
    pogoj = raw_input("Ce zelite nadaljevati pritisnite D: ").lower()

