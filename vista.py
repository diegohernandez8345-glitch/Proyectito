class ArchivoG:
    def __init__(self, texto):
        self.texto = texto
        self.listaguardar = []

    def guardararchivo(self):
        self.listaguardar.append(self.texto)
        with open("agregar.txt", "a") as archivo:
            for linea in self.listaguardar:
                archivo.write(linea + "\n")


def main():
    s='s'
    while s!='n':
        prueba=ArchivoG(input('ingrese texto'))
        prueba.guardararchivo()
        s=input('desea agregar otro texto')
main()