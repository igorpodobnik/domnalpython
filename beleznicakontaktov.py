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


def main():
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
        print ime
        Imenik.append(kontakt(ime,"0","0","0","0"))

"""    prvi = kontakt("Igor","Podobnik","igor@igor.si","0044","Chengdujska")
    print "haha"
    print prvi
    print prvi.first_name
    print prvi.last_name
    print ("%s in %s" % (prvi.first_name,prvi.last_name))
    print "end"     """
    #print Imenik
    for i in Imenik:
        print i.first_name


if __name__ == "__main__":
    main()