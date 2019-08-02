
class SeriePadoVan:

    def __init__(self):
        self.__terminoActual = 0

    def siguiente(self):
        respaldo = self.__terminoActual
        self.__terminoActual +=1
        return self.numeroPadovan(respaldo)

    def retroceder(self):
        self.__terminoActual -= 1
        respaldo = self.__terminoActual
        if respaldo <= 0:
            self.__terminoActual =0
            raise ValueError('No existe un número de padovan después de uno')

        return self.numeroPadovan(respaldo)

    def numeroPadovan(self, numero):
        respaldoanterior = 1
        terminoanterior = 1
        terminoactual = 1
        terminosiguiente = 1
        for i in range(3, numero + 1):
            terminosiguiente = respaldoanterior + terminoanterior
            respaldoanterior = terminoanterior
            terminoanterior = terminoactual
            terminoactual = terminosiguiente
        return terminosiguiente



