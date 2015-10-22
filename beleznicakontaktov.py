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
    while pogoj == "da":
        pogoj=raw_input("Vpisite Da za vnos v koledar: ").lower()
        print pogoj
        if pogoj != "da":
            break
        else:
            print "dal si DA"

    prvi = kontakt("Igor","Podobnik","igor@igor.si","0044","Chengdujska")
    print "haha"
    print prvi
    print prvi.first_name
    print prvi.last_name
    print ("%s in %s" % (prvi.first_name,prvi.last_name))
    print "end"



if __name__ == "__main__":
    main()