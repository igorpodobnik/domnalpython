__author__ = 'igorpodobnik'

class kontakt():
    first_name = "name"
    last_name = "surname"
    email = "email"
    phone = "0"
    adress = "adress"

    def __init__(self, ime, priimek, e_mail, stevilka, naslov):
        self.first_name = ime
        self.last_name = priimek
        self.email = e_mail
        self.phone = stevilka
        self.adress = naslov
    def __str__(self):
		return "Ha %s %s %s %s %s" % (self.first_name,self.last_name,self.email,self.phone,self.adress)
    def __repr__(self):
        return "Ha %s %s %s %s %s" % (self.first_name,self.last_name,self.email,self.phone,self.adress)
    #http://www.bogotobogo.com/python/python_classes_instances.php

pogoj = "da"
Imenik = []
for i in range(0,255):
    pogoj=raw_input("Vpisite Da za vnos v koledar: ").lower()
    print pogoj
    print i
    if pogoj != "da":
        break
    #else:
        #print "dal si DA"
    ime=raw_input("Vpisi ime: ")
    priimek=raw_input("Vpisi priimek: ")
    mejl=raw_input("Vpisi email: ")
    tel=raw_input("Vpisi telefonsko: ")
    nasl=raw_input("Vpisi naslov:")
    #print ime
    prviime = kontakt(ime,priimek,mejl,tel,nasl)
    #print prviime
    #print (prviime.first_name)
    Imenik.append(prviime)

print Imenik
for i in Imenik:
    print i





""" prvi = kontakt("Igor","Podobnik","igor@igor.si","0044","Chengdujska")
    print "haha"
    print prvi
    print prvi.first_name
    print prvi.last_name
    print ("%s in %s" % (prvi.first_name,prvi.last_name))
    print "end"  """