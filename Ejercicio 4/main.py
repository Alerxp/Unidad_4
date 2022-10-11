from Codificador import Codificador

if __name__ == '__main__':
    codificador = Codificador()
    nombre = input("Nombre del archivo a comprimir: ")

    if codificador.leerArchivo(nombre):
        codificador.cargarLista()
        codificador.crearArbolHuffman()
        codificador.generarCodigos()
        codificador.comprimirArchivo()
