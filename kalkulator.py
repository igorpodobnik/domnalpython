# -*- coding: utf-8 -*-
__author__ = 'Igor'
#spremenim v float,zaradi deljenja

pogoj = "d"
rezultat = 0
while pogoj == "d":
    x = input("Vnesi prvo stevilko: ")
    y = input("Vnesi drugo stevilko: ")

    print("Pritisni V za vsoto")
    print("Pritisni R za razliko")
    print("Pritisni P za produkt")
    print("Pritisni D za deljenje")
    operacija = raw_input("Vasa izbira je: ").lower()

    if operacija == "r":
        rezultat =  x - y
    if operacija == "v":
        rezultat = x + y
    if operacija == "p":
        rezultat = x * y
    if operacija == "d":
        x = x + 0.0
        y = y + 0.0
        rezultat = x/y

    print ("Vas rezultat je: %s" % rezultat)
    pogoj = raw_input("Ce zelite nadaljevati pritisnite D: ").lower()

