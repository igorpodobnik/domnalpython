# -*- coding: utf-8 -*-
__author__ = 'Igor'
#spremenim v float,zaradi deljenja

hoces = True
rezultat = 0
while hoces == True:
    x = input("Vnesi prvo stevilko: ")
    y = input("Vnesi drugo stevilko: ")
    x = x + 0.0
    y = y + 0.0
    print("Pritisni V za vsoto")
    print("Pritisni R za razliko")
    print("Pritisni P za produkt")
    print("Pritisni D za deljenje")
    operacija = raw_input("Vasa izbira je: ")

    if operacija == "R" or operacija == "r":
        rezultat =  x - y
    if operacija == "v" or operacija == "V":
        rezultat = x + y
    if operacija == "p" or operacija == "P":
        rezultat = x * y
    if operacija == "d" or operacija == "D":
        rezultat = x/y
    print ("Vas rezultat je: %s" % rezultat)
    pogoj =  raw_input("Ce zelite koncati pritisnite N: ")
    if pogoj == "n" or pogoj == "N":
        break
