__author__ = 'igorpodobnik'


class kontakt():
    pozicija = "0"
    first_name = "name"
    last_name = "surname"
    email = "email"
    phone = "0"
    adress = "adress"

    def __init__(self,pozic, ime, priimek, e_mail, stevilka, naslov):
        self.pozicija = pozic
        self.first_name = ime
        self.last_name = priimek
        self.email = e_mail
        self.phone = stevilka
        self.adress = naslov

    def __str__(self):
        return "HM %s %s %s %s %s %s %s" % (self.pozicija,self.first_name, self.last_name, self.email, self.phone, self.adress, self.fullname())

    def __repr__(self):
        return "Ha %s %s %s %s %s %s %s" % (self.pozicija,self.first_name, self.last_name, self.email, self.phone, self.adress, self.fullname())
        # http://www.bogotobogo.com/python/python_classes_instances.php d
    def fullname(self):
        name = self.first_name + " " + self.last_name
        return name



Imenik = []
for i in range(1, 256):
    pogoj = raw_input("Vpisite Da za vnos v koledar: ").lower()
    # print pogoj
    # print i
    if pogoj != "da":
        break
        # else:
        # print "dal si DA"
    ime = raw_input("Vpisi ime: ")
    priimek = raw_input("Vpisi priimek: ")
    mejl = raw_input("Vpisi email: ")
    tel = raw_input("Vpisi telefonsko: ")
    nasl = raw_input("Vpisi naslov:")
    # print ime
    prviime = kontakt(i,ime, priimek, mejl, tel, nasl)
    #print prviime.fullname()
    # print (prviime.first_name)
    Imenik.append(prviime)

print Imenik
for i in Imenik:
    #print "Ime: " + str(i.first_name) + " " + str(i.last_name) + " == " + str(i.fullname())
    print "\n"
    print "Pozicija v imeniku:  " + str(i.pozicija)
    print "Polno ime:           " + str(i.fullname())
    print "Email naslov:        " + str(i.email)
    print "Telefonska stevilka: " + str(i.phone)
    print "Naslov je:           " + str(i.adress)
    print "---------------------"
