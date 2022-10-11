from ABB import ABB
from ListaPorContenido import Lista

class Codificador:
    def __init__(self):
        self.__dicc = None
        self.__codigos = None
        self.__listaArboles = Lista()
        self.__arbolHuffman = None
        self.__archivo = ''

    def leerArchivo(self, nombre):
        flag = False
        try:
            with open(nombre + '.txt') as file:
                dicc = {}
                for char in file.read():  # obtenemos la frecuencia de cada caracter
                    if char != '\n':
                        if char in dicc:
                            dicc[char] += 1
                        else:
                            dicc[char] = 1
                    self.__archivo += char
            self.__dicc = dicc
            flag = True
        except:
            print("No existe un archivo con ese nombre")
        return flag

    def cargarLista(self):
        for c in self.__dicc.items():
            nuevoArbol = ABB(c)
            self.__listaArboles.insertar(nuevoArbol)

    def crearArbolHuffman(self):
        while len(self.__listaArboles) > 1:
            primero = self.__listaArboles.recuperar(1).getRaiz()  # nodo
            segundo = self.__listaArboles.recuperar(2).getRaiz()  # nodo

            caracter = primero.getCaracter() + segundo.getCaracter()
            frecuencia = primero.getFrecuencia() + segundo.getFrecuencia()
            dato = caracter, frecuencia

            nuevoArbol = ABB(dato)
            nuevoArbol.insertar(primero)
            nuevoArbol.insertar(segundo)

            self.__listaArboles.suprimir(1)
            self.__listaArboles.suprimir(1)
            self.__listaArboles.insertar(nuevoArbol)
        self.__arbolHuffman = self.__listaArboles.recuperar(1)

    def generarCodigos(self):
        dicc = {}
        for char in self.__dicc:
            dicc[char] = self.__arbolHuffman.generarCodigo(self.__arbolHuffman.getRaiz(), char)
        self.__codigos = dicc

    def comprimirArchivo(self):
        codigo = ''
        for char in self.__archivo:
            if char == '\n':
                codigo += char
            else:
                codigo += self.__codigos[char]

        with open('comprimido.txt', 'w') as nuevoArchivo:
            nuevoArchivo.write(codigo)

    def mostrarDicc(self):
        print(self.__dicc)

    def mostrarLista(self):
        self.__listaArboles.recorrer()

    def frontera(self):
        self.__arbolHuffman.frontera()
