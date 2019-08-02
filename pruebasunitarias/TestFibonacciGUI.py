import unittest
from GUI.CampoDeTexto import CampoDeTexto
from numerofibonacci.NumeroFibonacci import NumeroFibonacci
from basesnumericas.ConversorDeBaseNumerica import ConversorBaseNumerica


class TestfibonacciGUI(unittest.TestCase):

    def test_numero_siguiente_fibonacci(self):
        numero = NumeroFibonacci()
        numeroesperado = 0
        numero.siguiente()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_fibonacci_avanza2_regresa1(self):
        numero = NumeroFibonacci()
        numeroesperado = 0
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza4regresa3(self):
        numero = NumeroFibonacci()
        numeroesperado = 0
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza10regresa3(self):
        numero = NumeroFibonacci()
        numeroesperado = 8
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza10regresa4(self):
        numero = NumeroFibonacci()
        numeroesperado = 5
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza10regresa5(self):
        numero = NumeroFibonacci()
        numeroesperado = 3
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza10regresa6(self):
        numero = NumeroFibonacci()
        numeroesperado = 2
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza10regresa7(self):
        numero = NumeroFibonacci()
        numeroesperado = 1
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza10regresa8(self):
        numero = NumeroFibonacci()
        numeroesperado = 1
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza10regresa9(self):
        numero = NumeroFibonacci()
        numeroesperado = 0
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza10regresa10(self):
        with self.assertRaises(ValueError) as cero:
            numero = NumeroFibonacci()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
        self.assertEqual("No existe un número de fibonacci después de cero", str(cero.exception))
##----------
    def test_avanza11regresa3(self):
        numero = NumeroFibonacci()
        numeroesperado = 13
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza11regresa4(self):
        numero = NumeroFibonacci()
        numeroesperado = 8
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza11regresa5(self):
        numero = NumeroFibonacci()
        numeroesperado = 5
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza11regresa6(self):
        numero = NumeroFibonacci()
        numeroesperado = 3
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza11regresa7(self):
        numero = NumeroFibonacci()
        numeroesperado = 2
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza11regresa8(self):
        numero = NumeroFibonacci()
        numeroesperado = 1
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza11regresa9(self):
        numero = NumeroFibonacci()
        numeroesperado = 1
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza11regresa10(self):
        numero = NumeroFibonacci()
        numeroesperado = 0
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.siguiente()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numero.retroceder()
        numeroObtenido = numero.guardarEnlista().pop()
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_avanza11regresa11(self):
        with self.assertRaises(ValueError) as cero:
            numero = NumeroFibonacci()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.siguiente()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
            numero.retroceder()
        self.assertEqual("No existe un número de fibonacci después de cero", str(cero.exception))


 #---

    def test_avanza2regresa2(self):
        with self.assertRaises(ValueError) as cero:
            numero = NumeroFibonacci()
            numero.siguiente()
            numero.siguiente()
            numero.retroceder()
            numero.retroceder()
        self.assertEqual("No existe un número de fibonacci después de cero", str(cero.exception))

    def test_basenumericanosoportada(self):
        with self.assertRaises(ValueError) as incorrecto:
            campotextobinario = CampoDeTexto("binar", 30)
            campotextobinario.insertartexto("2345")
        self.assertEqual("Base numerica aun no implementada", str(incorrecto.exception))

    def test_decimal_12_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido =str(conversor.convertir(12, "hexadecimal"))
        numeroesperado = "c"

        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_1_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(1, "hexadecimal"))
        numeroesperado = "1"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_2_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(2, "hexadecimal"))
        numeroesperado = "2"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_3_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(3, "hexadecimal"))
        numeroesperado = "3"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_4_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(4, "hexadecimal"))
        numeroesperado = "4"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_5_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(5, "hexadecimal"))
        numeroesperado = "5"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_6_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(6, "hexadecimal"))
        numeroesperado = "6"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_7_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(7, "hexadecimal"))
        numeroesperado = "7"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_8_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(8, "hexadecimal"))
        numeroesperado = "8"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_9_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(9, "hexadecimal"))
        numeroesperado = "9"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_10_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(10, "hexadecimal"))
        numeroesperado = "a"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_11_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(11, "hexadecimal"))
        numeroesperado = "b"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_12_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(12, "hexadecimal"))
        numeroesperado = "c"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_13_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(13, "hexadecimal"))
        numeroesperado = "d"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_14_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(14, "hexadecimal"))
        numeroesperado = "e"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_15_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(15, "hexadecimal"))
        numeroesperado = "f"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_16_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(16, "hexadecimal"))
        numeroesperado = "10"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_17_a_hexacimal(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(17, "hexadecimal"))
        numeroesperado = "11"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_0_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(0, "binario"))
        numeroesperado = "00000000"

        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_1_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(1, "binario"))
        numeroesperado = "00000001"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_2_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(2, "binario"))
        numeroesperado = "00000010"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_3_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(3, "binario"))
        numeroesperado = "00000011"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_4_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(4, "binario"))
        numeroesperado = "00000100"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_5_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(5, "binario"))
        numeroesperado = "00000101"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_6_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(6, "binario"))
        numeroesperado = "00000110"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_7_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(7, "binario"))
        numeroesperado = "00000111"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_8_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(8, "binario"))
        numeroesperado = "00001000"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_9_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(9, "binario"))
        numeroesperado = "00001001"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_10_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(10, "binario"))
        numeroesperado = "00001010"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_11_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(11, "binario"))
        numeroesperado = "00001011"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_12_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(12, "binario"))
        numeroesperado = "00001100"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_13_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(13, "binario"))
        numeroesperado = "00001101"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_14_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(14, "binario"))
        numeroesperado = "00001110"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_15_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(15, "binario"))
        numeroesperado = "00001111"
        self.assertEqual(numeroesperado, numeroObtenido)

    def test_decimal_16_a_binario(self):
        conversor = ConversorBaseNumerica()
        numeroObtenido = str(conversor.convertir(16, "binario"))
        numeroesperado = "00010000"
        self.assertEqual(numeroesperado, numeroObtenido)


if __name__ == '__main__':
   unittest.main()
