class NumeroDeLaSuerte:
    def __init__(self):
        self.__terminoActual = 0
        self.__listaNumerosSuerte = self.generadorNumeroSuerte(1000)

    def siguiente(self):
        respaldo = self.__terminoActual
        self.__terminoActual += 1
        return self.__listaNumerosSuerte[respaldo]

    def retroceder(self):
        respaldo = self.__terminoActual-1
        if self.__terminoActual == 0:
            raise ValueError('No existe un número de de la suerte después de uno')
        if self.__terminoActual <=2:
            self.__terminoActual -=1
            return self.__listaNumerosSuerte[self.__terminoActual]

        self.__terminoActual =self.__terminoActual-1

        return self.__listaNumerosSuerte[self.__terminoActual]

    def guardarenlista(self):
        return self.__lista

    def __str__(self):
        return "Numero Actual :%s" % self.__terminoActual

    def println(self):
        print(self.__str__())



    def generadorNumeroSuerte(self, n):
        if n < 3:
            return [1]
        listaaretornar = list(range(1, n + 1, 2))
        listaaretornar_index = 1
        while True:
            listaaretornar_len = len(listaaretornar)
            if (listaaretornar_index + 1)>listaaretornar_len:
                break
            indice = listaaretornar[listaaretornar_index]
            if listaaretornar_len < indice:
                break
            del listaaretornar[indice - 1:: indice]
            listaaretornar_index += 1
        return listaaretornar

