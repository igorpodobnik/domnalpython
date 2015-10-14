__author__ = 'igorpodobnik'
from uganiprestolnico import par


def main():

    while 1==1:
        #kontrolo za šumnike oz kontrolo za neprimerne vnose dej notri
        vnos_drzave = raw_input("Vnesi drzavo (oz. stop):")
        if vnos_drzave == "stop":
            break
        else:
            print "Prestolnica je: " + par(vnos_drzave)

if __name__ == "__main__":
    main()