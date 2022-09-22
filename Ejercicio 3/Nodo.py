class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__izquierdo = None
        self.__derecho = None

    def getDato(self):
        return self.__dato

    def getIzquierdo(self):
        return self.__izquierdo

    def getDerecho(self):
        return self.__derecho

    def setDato(self, dato):
        self.__dato = dato

    def setIzquierdo(self, nodo):
        self.__izquierdo = nodo

    def setDerecho(self, nodo):
        self.__derecho = nodo
