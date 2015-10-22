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
        self.full_name = ime + " " + priimek
    #PREVERI ker ne dela ok.
    def fulln(self):
        full_name = self.first_name + " " + self.last_name
        print full_name
        return full_name
    def __str__(self):
        return "HM %s %s %s %s %s " % (self.first_name, self.last_name, self.email, self.phone, self.adress)

    def __repr__(self):
        return "Ha %s %s %s %s %s " % (self.first_name, self.last_name, self.email, self.phone, self.adress)
        # http://www.bogotobogo.com/python/python_classes_instances.php d


pogoj = "da"
Imenik = []
for i in range(0, 255):
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
    prviime = kontakt(ime, priimek, mejl, tel, nasl)
    # print prviime
    # print (prviime.first_name)
    Imenik.append(prviime)

print Imenik
for i in Imenik:
    print "Ime: " + i.first_name + " " + i.last_name
    print i.fulln
