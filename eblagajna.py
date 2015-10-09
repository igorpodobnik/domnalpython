__author__ = 'igorpodobnik'

def izpis(artikel):
    a = artikli[artikel]
    return a

artikli ={
"mleko" : 1,
"jajca" : 1.2,
"kruh" : 2,
"pivo" : 1.1
}

def main():
    while 1==1:
        vnos = raw_input("Vnesi artikel (H za seznam): ").lower()
        if vnos == "h":
            for i in artikli:
                print i
        else:
            print izpis(vnos)



if __name__ == "__main__":
    main()