__author__ = 'igorpodobnik'
import random


class avtomobili():
    zap_st = 0
    znamka = "znamka"
    st_vrat = "stevilo vrat"
    model = "model"
    pogon = "spredaj/zadaj"
    tip_motorja = "diesel/bencin"

    def __init__(self,zn,zap,st,mo,po,ti):
        self.znamka = zn
        self.zap_st = zap
        self.st_vrat = st
        self.model = mo
        self.pogon=po
        self.tip_motorja=ti

    def __str__(self):
        return "STR %d %s %s %s %s %s " % (self.zap_st,self.znamka,self.st_vrat,self.model,self.pogon,self.tip_motorja)
    def __repr__(self):
        return "STR %d %s %s %s %s %s " % (self.zap_st,self.znamka,self.st_vrat,self.model,self.pogon,self.tip_motorja)

def koncaj(pogoj,kontr):
    if pogoj == kontr:
        print "Yeeeey"
        return False
    else:
        return True



avti = []
avti.append(avtomobili("kia",0,"5","Carens","Spredaj","Diesel"))
avti.append(avtomobili("renault",1,"5","Clio","Spredaj","Bencin"))
avti.append(avtomobili("porshe",2,"2","911","Zadaj","Bencin"))
avti.append(avtomobili("bmw",3,"4","3 Series","Zadaj","Diesel"))




loop = True
#print(cifra)

#print avti
#print avti[cifra]
while True:
    se = raw_input("Vnesi D za nadaljevanje: ").lower()
    if se != "d":
        break
    cifra = random.randrange(len(avti))
    #print str(cifra)+"cifra"
    loop = True
    for i in avti:
        #print str(i.zap_st) + "zap"
        if cifra == i.zap_st:
            while loop == True:
                #print "hello " + str(i.model)
                kater_podatek = random.randrange(3)
                #print str(kater_podatek) + "kater_podatek"
                if kater_podatek==0:
                    #print i.st_vrat
                    print ("Stevilo vrat je %s: " % i.st_vrat)
                    uganka = raw_input("Vnesi znamko: ").lower()
                    loop = koncaj(uganka,i.znamka)
                    #print str(loop) + "loop"
                    #if uganka == i.znamka:
                        #print "YEY"
                        #break

                elif kater_podatek == 1:
                    #print i.model
                    print ("Model je %s: " % i.model)
                    uganka = raw_input("Vnesi znamko: ").lower()
                    loop = koncaj(uganka,i.znamka)

                elif kater_podatek == 2:
                    #print i.model
                    print ("Pogon ima %s: " % i.pogon)
                    uganka = raw_input("Vnesi znamko: ").lower()
                    loop = koncaj(uganka,i.znamka)


