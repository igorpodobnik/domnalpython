__author__ = 'Igor'
import random



def izracunajstevilke(maxstevilo,kolikokroglic):
    rezultati = []
    izrebanih = 0
    while izrebanih < kolikokroglic:
        #print i
        #print kolikokroglic
        #print maxstevilo
        cifra = random.randrange(1,maxstevilo)
        #print cifra
        if cifra not in rezultati:
            rezultati.append(cifra)
            izrebanih +=1
    rezultati.sort()
    return rezultati


def main():
    skupnostevilo = input("Vnesi maksimalno stevilo: ")
    steviloizzrebanih = input("Vnesi stevilo izrebanih stevilk: ")


    print izracunajstevilke(skupnostevilo,steviloizzrebanih)
    Sloloto = izracunajstevilke (39,7)
    EUROJACKPOT1 = izracunajstevilke(50,5)
    EUROJACKPOT2 = izracunajstevilke(10,2)

    print "Eurojackpot stevilke so: "+ str(EUROJACKPOT1) + "in dodatne " + str(EUROJACKPOT2)
    print "Slovenske loto stevilke so: "+ str(Sloloto)



if __name__ == "__main__":
    main()