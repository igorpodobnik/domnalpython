__author__ = 'igorpodobnik'
from delez import razmerje
from eblagajna import izpis


def procent():
    assert razmerje(20,50) == 40
    return "Razmerje OK"

def prikaz():
    assert izpis("mleko")== 1
    return "Prikaz OK"
print procent()
print prikaz()