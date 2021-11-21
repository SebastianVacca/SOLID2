from abc import ABC, abstractmethod

class Coche(ABC):
    @abstractmethod
    def precioMedioCoche(self):
        pass
    def numAsientos(self):
        pass

class Renault (Coche):
    def precioMedioCoche(self):
        return "18000"
    def numAsientos(self):
        return "5"
class Auidi (Coche):
    def precioMedioCoche(self):
        return "25000"
    def numAsientos(self):
        return "2"

class Mercedes(Coche):
    def precioMedioCoche(self):
        return "27000"
    def numAsientos(self):
        return "2"


def imprimirPrecioMedioCoche(Coche):

    for i in Coche:
        print(i.precioMedioCoche())

def imprimirNumAsientos(Coche):

    for i in Coche:
        if Coche is Renault:
            print(numAsientos(Coche))
        if Coche is Audi:
            print(numAsientos(Coche))
        if Coche is Mercedes:
            print(numAsientos(Coche))

def imprimirNumAsientos(Coche):
    for i in Coche:
        print(i.numAsientos())

if __name__ == '__main__':

    coches = [Renault(), Auidi(), Mercedes()]
    imprimirPrecioMedioCoche(coches)
    imprimirNumAsientos(coches)
