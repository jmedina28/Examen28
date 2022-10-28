
class Nodo():

    info,sig = None,None

class datoPolinomio():

    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio():

    def __init__(self, termino_mayor,grado):

        self.termino_mayor = termino_mayor
        self.grado = grado
    
    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if(termino> polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while(actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux
