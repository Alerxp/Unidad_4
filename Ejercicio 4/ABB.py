from NodoABB import Nodo

class ABB:
    def __init__(self, dato):
        self.__raiz = Nodo(dato[0], dato[1])

    def __lt__(self, other):
        return self.__raiz.getFrecuencia() < other.__raiz.getFrecuencia()

    def __ge__(self, other):
        return self.__raiz.getFrecuencia() >= other.__raiz.getFrecuencia()

    def __insertarNodo(self, nodo, nuevoNodo):
        if nodo.getIzquierdo() is None:
            nodo.setIzquierdo(nuevoNodo)
        else:
            nodo.setDerecho(nuevoNodo)

    def __preOrdenRecursivo(self, nodo):
        if nodo is not None:
            print(nodo, end=" ")
            self.__preOrdenRecursivo(nodo.getIzquierdo())
            self.__preOrdenRecursivo(nodo.getDerecho())

    def __inOrdenRecursivo(self, nodo):
        if nodo is not None:
            self.__inOrdenRecursivo(nodo.getIzquierdo())
            print(nodo, end=" ")
            self.__inOrdenRecursivo(nodo.getDerecho())

    def __postOrdenRecursivo(self, nodo):
        if nodo is not None:
            self.__postOrdenRecursivo(nodo.getIzquierdo())
            self.__postOrdenRecursivo(nodo.getDerecho())
            print(nodo, end=" ")

    def __fronteraRecursivo(self, nodo):
        if nodo is not None:
            if nodo.getIzquierdo() is None and nodo.getDerecho() is None:
                print(nodo, end=" ")
            self.__fronteraRecursivo(nodo.getIzquierdo())
            self.__fronteraRecursivo(nodo.getDerecho())

# Métodos públicos

    def insertar(self, nuevoNodo):
        self.__insertarNodo(self.__raiz, nuevoNodo)

    def getRaiz(self):
        return self.__raiz

    def preOrden(self):
        if self.__raiz is not None:
            print("PreOrden")
            self.__preOrdenRecursivo(self.__raiz)
            print("")
        else:
            print("Árbol vacío")

    def inOrden(self):
        if self.__raiz is not None:
            print("InOrden")
            self.__inOrdenRecursivo(self.__raiz)
            print("")
        else:
            print("Árbol vacío")

    def postOrden(self):
        if self.__raiz is not None:
            print("PostOrden")
            self.__postOrdenRecursivo(self.__raiz)
            print("")
        else:
            print("Árbol vacío")

    def frontera(self):
        if self.__raiz is not None:
            self.__fronteraRecursivo(self.__raiz)
            print("")
        else:
            print("Ábol vacío")

    def generarCodigo(self, nodo, caracter):
        if caracter == nodo.getCaracter():
            return ''
        else:
            if caracter in nodo.getIzquierdo().getCaracter():
                return '0' + self.generarCodigo(nodo.getIzquierdo(), caracter)
            elif caracter in nodo.getDerecho().getCaracter():
                return '1' + self.generarCodigo(nodo.getDerecho(), caracter)
