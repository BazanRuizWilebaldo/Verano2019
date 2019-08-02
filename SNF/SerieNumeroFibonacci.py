
class SerieNumeroFibonacci(list):

    def append(self, elemento):
        if not esnumerofibonacci(elemento):
            raise TypeError("EL numero no es un numero de fibonacci %s" % elemento)
        super(SerieNumeroFibonacci, self).append(elemento)


def esnumerofibonacci(numero):
    primertermino = 0
    segundotermino = 1
    tercertermino = 0
    while tercertermino < numero:
        tercertermino = primertermino + segundotermino
        primertermino = segundotermino
        segundotermino = tercertermino

    if tercertermino == numero:
        return True

    return False
