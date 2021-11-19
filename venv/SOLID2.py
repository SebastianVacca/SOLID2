from abc import ABC, abstractmethod

class Coche(ABC):
    @abstractmethod
    def precioMedioCoche(self):
        pass

class Renault (Coche):
    def precioMedioCoche(self):
        return "18000"
    def numAsientos(self):
        return "5"
class Auidi (Coche):
    def precioMedioCoche(self):
        return "25000"

class Mercedes(Coche):
    def precioMedioCoche(self):
        return "27000"


def imprimirPrecioMedioCoche(Coche):

    for i in Coche:
        print(i.precioMedioCoche())

if __name__ == '__main__':

    coches = [Renault(), Auidi(), Mercedes()]
    imprimirPrecioMedioCoche(coches)
