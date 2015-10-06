# -*- coding: utf-8 -*-
import urllib2
#https://dl.dropboxusercontent.com/u/29645703/SmartNinja/DNK/dna.txt

DNA = urllib2.urlopen("https://dl.dropboxusercontent.com/u/29645703/SmartNinja/DNK/dna.txt")
#DNA = open("testni.txt", "r").read()
print DNA
lasje = {"Crna" : "CCAGCAATCGC", "Rjava": "GCCAGTGCCG", "Oranzna": "TTAGCTATCGC"}
oblika_obraza = {"Kvadraten": "GCCACG", "Okrogel": "ACCACAA", "Ovalen": "AGGCCTCA"}
barva_oci = {"Modra": "TTGTGGTGGC","Zelena": "GGGAGGTGGC" , "Rjava": "AAGTAGTGAC"}
spol = {"Moski": "TGCAGGAACTTC" ,"Zenska": "TGAAGGACCTTC"}
rasa = { "Belec" : "AAAACCTCA" , "Crnec" : "CGACTACAG" , "Azijec": "CGCGGGCCG"}

Ziga = {"Spol" : spol["Moski"], "Rasa": rasa["Belec"], "Barva las": lasje["Oranzna"], "Barva oci": barva_oci["Rjava"], "Oblika obraza": oblika_obraza["Okrogel"]}
Matej = {"Spol" : spol["Moski"], "Rasa": rasa["Belec"], "Barva las": lasje["Crna"], "Barva oci": barva_oci["Modra"], "Oblika obraza": oblika_obraza["Ovalen"]}
Miha = {"Spol" : spol["Moski"], "Rasa": rasa["Belec"], "Barva las": lasje["Rjava"], "Barva oci": barva_oci["Zelena"], "Oblika obraza": oblika_obraza["Kvadraten"]}

#print spol["Moski"]
#print Ziga["Spol"]
zigavred = 0
for vzorec1 in Ziga:
    #print vzorec1
    #print Ziga[vzorec1]
    if Ziga[vzorec1] in DNA:
        zigavred += 1

print zigavred

mihavred = 0
for vzorec2 in Miha:
    #print Miha[vzorec2]
    if Miha[vzorec2] in DNA:
        mihavred += 1

print mihavred

matejvred = 0
for vzorec3 in Matej:
    #print Matej[vzorec3]
    if Matej[vzorec3] in DNA:
        matejvred += 1
    #print matejvred

print matejvred

if zigavred == 5:
    print("Ziga je KRIV!")
if mihavred == 5:
    print("Miha je KRIV!")
if matejvred == 5:
    print("Matej je KRIV!")
