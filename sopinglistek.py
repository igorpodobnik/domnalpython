__author__ = 'Igor'
# -*- coding: utf-8 -*-
import os

list = []
i=0
hoces = raw_input("Zelite kaj vnesti? D za Da: ").lower()
if hoces == "d":
    i = 1
else:
    print("Pa nic...")
while i == 1:
    vnos = raw_input("Vnesi prvo stvar za nakupovalni seznam: ")
    list.append(vnos)
    pogoj = raw_input("Ce zelite nadaljevati pritisnite D: ").lower()
    if pogoj != "d":

        break
if hoces == "d":
    print "\n" * 20
    print("Vas seznam vsebuje:")
    for i in list:
        print i
    print("--- Konec seznama ---")

