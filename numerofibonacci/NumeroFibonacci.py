from SNF.SerieNumeroFibonacci import SerieNumeroFibonacci

class NumeroFibonacci:

    def __init__(self):
        self.__lista = SerieNumeroFibonacci()
        self.__terminoActual = 0
        self.__terminoAnterior = 0
        self.__numeroVecesLlamado = 0

    def __reiniciar(self):
        self.__terminoActual = 0
        self.__terminoAnterior = 0
        self.__numeroVecesLlamado = 0

    def siguiente(self):
        if self.__terminoAnterior == 1 and self.__terminoActual == 0:
            self.__reiniciar()
        self.__actualizaTerminosAvanzar()
        self.__numeroVecesLlamado += 1
        self.__lista.append(self.__terminoActual)
        return self.__terminoActual

    def __actualizaTerminosAvanzar(self):
        if self.__numeroVecesLlamado == 0:
            self.__terminoActual = 0

        if self.__numeroVecesLlamado == 1:
            self.__terminoActual = 1

        if self.__numeroVecesLlamado >= 2:
            respaldoAnterior = self.__terminoAnterior
            self.__terminoAnterior = self.__terminoActual
            self.__terminoActual = self.__terminoAnterior \
                                   + respaldoAnterior

    def retroceder(self):
        self.__actualizaTerminosRetroceder()
        self.__numeroVecesLlamado -= 1
        self.__lista.append(self.__terminoActual)
        return self.__terminoActual



    def __actualizaTerminosRetroceder(self):
        respaldoTerminoActual = self.__terminoActual

        if respaldoTerminoActual == 0:
            raise ValueError('No existe un número de fibonacci después de cero')

        self.__terminoActual = self.__terminoAnterior
        self.__terminoAnterior = respaldoTerminoActual \
                                 - self.__terminoActual

    def __repr__(self):
        return "Numero Actual :%s Numero Anterior :%s Numero de veces llamado:%s" \
               % (self.__terminoActual, self.__terminoAnterior, self.__numeroVecesLlamado)

    def __str__(self):
        return "Numero Actual :%s Numero Anterior :%s Numero de veces llamado:%s" \
               % (self.__terminoActual, self.__terminoAnterior, self.__numeroVecesLlamado)

    def println(self):
        print(self)

    def guardarEnlista(self):
        return self.__lista



