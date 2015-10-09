__author__ = 'igorpodobnik'

def razmerje(stevilo,stevilovseh):
    rezultat = ((stevilo*100)/stevilovseh)
    return rezultat

def main():
    while 1==1:
        a = raw_input("Vnesi stevilo mladih ljudi: ")
        b = raw_input("Vnesi stevilo vseh ljudi: ")
        if a.isdigit() and b.isdigit():
            a =int(a)
            b =int(b)
            rezultat = razmerje(a,b)
        else:
            print("Se enkrat")
            main()

        print "Delez je: "+ str(rezultat) +"%"
        pogoj = raw_input("Vnesi N za prekinitev izracunavanja: ").lower()
        if pogoj == "n":
            break



if __name__ == "__main__":
    main()