__author__ = 'igorpodobnik'
import random


class avtomobili():
    znamka = "znamka"
    st_vrat = "stevilo vrat"
    model = "model"
    pogon = "spredaj/zadaj"
    tip_motorja = "diesel/bencin"

    def __init__(self,zn,st,mo,po,ti):
        self.znamka = zn
        self.st_vrat = st
        self.model = mo
        self.pogon=po
        self.tip_motorja=ti

    def __str__(self):
        return "STR %s %s %s %s %s " % (self.znamka,self.st_vrat,self.model,self.pogon,self.tip_motorja)
    def __repr__(self):
        return "STR %s %s %s %s %s " % (self.znamka,self.st_vrat,self.model,self.pogon,self.tip_motorja)


avti = []
avti.append(avtomobili("kia","5","Carens","Spredaj","Diesel"))
avti.append(avtomobili("renault","5","Clio","Spredaj","Bencin"))

cifra = random.randrange(len(avti))
print(cifra)

print avti
print avti[cifra]

