from Nodo import Nodo

class ABB:
    def __init__(self):
        self.__raiz = None

    def __insertarRecursivo(self, nodo, dato):
        if dato == nodo.getDato():
            print("El elemento ya se encuentra en el árbol")
        elif dato < nodo.getDato():
            if nodo.getIzquierdo() is None:
                nodo.setIzquierdo(Nodo(dato))
            else:
                self.__insertarRecursivo(nodo.getIzquierdo(), dato)
        else:
            if nodo.getDerecho() is None:
                nodo.setDerecho(Nodo(dato))
            else:
                self.__insertarRecursivo(nodo.getDerecho(), dato)

    def __preOrdenRecursivo(self, nodo):
        if nodo is not None:
            print(nodo.getDato(), end=" ")
            self.__preOrdenRecursivo(nodo.getIzquierdo())
            self.__preOrdenRecursivo(nodo.getDerecho())

    def __inOrdenRecursivo(self, nodo):
        if nodo is not None:
            self.__inOrdenRecursivo(nodo.getIzquierdo())
            print(nodo.getDato(), end=" ")
            self.__inOrdenRecursivo(nodo.getDerecho())

    def __postOrdenRecursivo(self, nodo):
        if nodo is not None:
            self.__postOrdenRecursivo(nodo.getIzquierdo())
            self.__postOrdenRecursivo(nodo.getDerecho())
            print(nodo.getDato(), end=" ")

    def __buscaRecursivo(self, nodo, padre, dato):
        if nodo is None:
            return None, None
        if dato == nodo.getDato():
            return nodo, padre
        elif dato < nodo.getDato():
            padre = nodo
            return self.__buscaRecursivo(nodo.getIzquierdo(), padre, dato)
        else:
            padre = nodo
            return self.__buscaRecursivo(nodo.getDerecho(), padre, dato)

    def __hoja(self, unNodo, dato):
        nodo = self.__buscaRecursivo(unNodo, None, dato)
        if nodo:
            if not nodo[0].getIzquierdo() and not nodo[0].getDerecho():
                return True
            else:
                return False

    def __hijo(self, nodo, hijo, padre):
        hijoIzquierdo, hijoDerecho = False, False
        nodoPadre = self.__buscaRecursivo(nodo, None, padre)[0]
        nodoHijo = self.__buscaRecursivo(nodo, None, hijo)[0]
        if nodoPadre and nodoHijo:
            if nodoPadre.getIzquierdo() is not None:
               hijoIzquierdo = nodoPadre.getIzquierdo().getDato() == nodoHijo.getDato()
            if nodoPadre.getDerecho() is not None:
               hijoDerecho = nodoPadre.getDerecho().getDato() == nodoHijo.getDato()
        return hijoIzquierdo or hijoDerecho

    def __nivelRecursivo(self, nodo, nivel, dato):
        if nodo is None:
            return None
        if dato == nodo.getDato():
            return nivel
        elif dato < nodo.getDato():
            nivel += 1
            return self.__nivelRecursivo(nodo.getIzquierdo(), nivel, dato)
        else:
            nivel += 1
            return self.__nivelRecursivo(nodo.getDerecho(), nivel, dato)

    def __alturaRecursivo(self, nodo):
        if nodo is None:
            return -1
        else:
            return 1 + max(self.__alturaRecursivo(nodo.getIzquierdo()), self.__alturaRecursivo(nodo.getDerecho()))

    def __maxIzquierdo(self, nodo, padre):  # mayor del subárbol izquierdo
        if nodo.getDerecho() is None:
            return nodo, padre
        else:
            padre = nodo
            return self.__maxIzquierdo(nodo.getDerecho(), padre)

    def __suprimir(self, nodo, padre):
        if self.__hoja(nodo, nodo.getDato()):  # el nodo a eliminar es hoja
            if padre.getIzquierdo() == nodo:
                padre.setIzquierdo(None)
            if padre.getDerecho() == nodo:
                padre.setDerecho(None)
        else:
            if (nodo.getIzquierdo() and nodo.getDerecho() is None) or (nodo.getIzquierdo() is None and nodo.getDerecho()):  # el nodo a eliminar tiene un hijo
                if padre.getIzquierdo() == nodo:
                    if nodo.getIzquierdo():
                        padre.setIzquierdo(nodo.getIzquierdo())
                    else:
                        padre.setIzquierdo(nodo.getDerecho())
                if padre.getDerecho() == nodo:
                    if nodo.getDerecho():
                        padre.setDerecho(nodo.getDerecho())
                    else:
                        padre.setDerecho(nodo.getIzquierdo())
            else:  # el nodo a eliminar tiene dos hijos
                nodoReemplazo, nodoPadre = self.__maxIzquierdo(nodo.getIzquierdo(), nodo)
                nodo.setDato(nodoReemplazo.getDato())
                self.__suprimir(nodoReemplazo, nodoPadre)

    def __caminoRecursivo(self, x, z, camino):
        if x is None:
            return None
        else:
            camino.append(x.getDato())
            if z == x.getDato():
                return camino
            elif z < x.getDato():
                return self.__caminoRecursivo(x.getIzquierdo(), z, camino)
            else:
                return self.__caminoRecursivo(x.getDerecho(), z, camino)

# Métodos públicos

    def insertar(self, dato):
        if self.__raiz is None:
            self.__raiz = Nodo(dato)
        else:
            self.__insertarRecursivo(self.__raiz, dato)

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

    def busca(self, dato):
        if self.__raiz is not None:
            padre = None
            return self.__buscaRecursivo(self.__raiz, padre, dato)[0]
        else:
            print("Árbol vacío")

    def hoja(self, dato):
        if self.__raiz is not None:
            return self.__hoja(self.__raiz, dato)
        else:
            print("Árbol vacío")

    def hijo(self, hijo, padre):
        if self.__raiz is not None:
            return self.__hijo(self.__raiz, hijo, padre)
        else:
            print("Árbol vacío")

    def padre(self, padre, hijo):
        if self.__raiz is not None:
            return self.__hijo(self.__raiz, hijo, padre)
        else:
            print("Árbol vacío")

    def nivel(self, dato):
        if self.__raiz is not None:
            nivelRaiz = 0
            return self.__nivelRecursivo(self.__raiz, nivelRaiz, dato)
        else:
            print("Árbol vacío")

    def altura(self):
        if self.__raiz is not None:
            return self.__alturaRecursivo(self.__raiz)
        else:
            print("Árbol vacío")

    def suprimir(self, dato):
        if self.__raiz is not None:
            nodo, padre = self.__buscaRecursivo(self.__raiz, None, dato)
            if nodo:
                self.__suprimir(nodo, padre)
        else:
            print("Árbol vacío")

    def camino(self, x, z):
        if self.__raiz is not None:
            ancestro = self.__buscaRecursivo(self.__raiz, None, x)[0]
            descendiente = self.__buscaRecursivo(self.__raiz, None, z)[0].getDato()
            if ancestro and descendiente:
                camino = []
                return self.__caminoRecursivo(ancestro, descendiente, camino)
        else:
            print("Árbol vacío")
