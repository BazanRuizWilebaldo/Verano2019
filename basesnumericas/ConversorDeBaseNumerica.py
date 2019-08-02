from sucesiones.VerificadorNumero import esNumercapicua, esUnNumeroFeliz
from num2words import num2words

class ConversorBaseNumerica:

    def convertir(self, numero, baseaconvertir):
        conversor = get_conversor(baseaconvertir)
        return conversor(numero)


def get_conversor(baseaconvertir):
    if baseaconvertir.lower() == 'binario':
        return _convertir_a_binario
    if baseaconvertir.lower() == 'hexadecimal':
        return _convertir_a_hexadecimal
    if baseaconvertir.lower() == 'decimal':
        return _convertir_a_decimal
    if baseaconvertir.lower() == 'numero feliz':
        return _valida_numero_feliz
    if baseaconvertir.lower() == 'numero capicua':
        return _valida_numero_capicua
    if baseaconvertir.lower() == 'numero en espaniol':
        return _nombre_del_numero_en_espaniol
    raise ValueError("Base numerica aun no implementada")


def _convertir_a_binario(numero):
    retornar = str(f'{numero:08b}')
    return retornar


def _convertir_a_decimal(numero):
    retornar = str(numero)
    return retornar


def _valida_numero_feliz(numero):
    if int(numero)>0:
        retornar = str(esUnNumeroFeliz(numero))
        return retornar
    else:
        return "Falso"


def _valida_numero_capicua(numero):
    retornar = esNumercapicua(numero)
    return retornar


def _nombre_del_numero_en_espaniol(numero):
    retornar = str(num2words(numero, lang='es'))
    return retornar


def _convertir_a_hexadecimal(numero):
    retornar = str(format(numero, 'x'))
    return retornar

