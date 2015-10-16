__author__ = 'igorpodobnik'
from delez import razmerje
from eblagajna import izpis


def razmerjemladihinvseh():
    assert razmerje(30,120) == 25
    return "Razmerje OK"

def cenaartiklamoraobstajati():
    assert izpis("mleko")== 1
    return "Prikaz OK"
print razmerjemladihinvseh()
print cenaartiklamoraobstajati()