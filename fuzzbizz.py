__author__ = 'Igor'
x = input("Vnesite tevilko od 1 do 100: ")
if x > 100:
    x = 100
    print("Stevilka prevelika, nastavljena na 100")
for i in range(1,x,1):
    #print i
    #print i % 3
    #print i % 5
    if ((i % 3) == 0) and ((i % 5) == 0) and i > 0 :
        print("fizzbuzz")
    elif ((i % 3) == 0) and i > 0:
        print("fizz")
    elif ((i % 5) == 0) and i > 0:
        print("buzz")
    else:
        print i
