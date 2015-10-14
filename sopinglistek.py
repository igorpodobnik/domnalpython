__author__ = 'Igor'
# -*- coding: utf-8 -*-
import os

soping_list = []
i=0
hoces = raw_input("Zelite kaj vnesti? D za Da: ").lower()
if hoces != "d":
    print("Pa nic...")
while hoces == "d":
    vnos = raw_input("Vnesi novo stvar za nakupovalni seznam (oz. stop za prekinitev): ")

    #pogoj = raw_input("Ce zelite nadaljevati pritisnite D: ").lower()
    if vnos == "stop":
        break
    soping_list.append(vnos)
if hoces == "d":
    print "\n" * 20
    print("Vas seznam vsebuje:")
    for i in soping_list:
        print i
    print("--- Konec seznama ---")

