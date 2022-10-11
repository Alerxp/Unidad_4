class Nodo:
    def __init__(self, caracter, frecuencia):
        self.__caracter = caracter
        self.__frecuencia = int(frecuencia)
        self.__izquierdo = None
        self.__derecho = None

    def __str__(self):
        return f"{self.__caracter}: {self.__frecuencia}"

    def __eq__(self, other):
        return self.__caracter == other.__caracter

    def __lt__(self, other):
        return self.__frecuencia < other.__frecuencia

    def getCaracter(self):
        return self.__caracter

    def getFrecuencia(self):
        return self.__frecuencia

    def getIzquierdo(self):
        return self.__izquierdo

    def getDerecho(self):
        return self.__derecho

    def setCaracter(self, caracter):
        self.__caracter = caracter

    def setFrecuencia(self, frecuencia):
        self.__frecuencia = frecuencia

    def setIzquierdo(self, nodo):
        self.__izquierdo = nodo

    def setDerecho(self, nodo):
        self.__derecho = nodo
