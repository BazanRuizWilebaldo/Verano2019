
def sumadecuadrados(numero):
    resultado = 0
    suma = 0
    if numero>0:
        while(numero >0):
            resultado = numero % 10
            suma = suma + (resultado * resultado)
            numero = numero // 10
    return suma


def esUnNumeroFeliz(numero):
    resultado = numero
    if (resultado>0):
        while (resultado != 1 and  resultado != 4):
            resultado = sumadecuadrados(resultado)

    if resultado == 1:
        return "Verdadero"
    if resultado == 4 or resultado == 0:
        return "Falso"


def esNumercapicua(numero):
    cadenaAlrevez = str(numero)[::-1]
    if str(numero) == cadenaAlrevez:
        return "Verdadero"
    return "Falso"





