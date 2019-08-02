from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry, Button
from observerpattern.PatronGUI import Subscriptor, PublicadorBoton
from numerofibonacci.NumeroFibonacci import NumeroFibonacci
from sucesiones.NumeroDeLaSuerte import NumeroDeLaSuerte
from sucesiones.Padovan import SeriePadoVan
class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Review")
        self.pack(fill=BOTH, expand=True)


        frameNumeroFibonacci = Frame(self)
        frameNumeroFibonacci.pack(fill=X)

        letreroFibonacci = Label(frameNumeroFibonacci, text="Número de Fibonacci", width=30)
        letreroFibonacci.pack(side=LEFT, padx=5, pady=5)
        botonFibonacciAvanzar = Button(frameNumeroFibonacci, text="Avanzar")
        botonFibonacciAvanzar.pack(side=LEFT, padx=5, pady=5)
        botonFibonacciRetroceder = Button(frameNumeroFibonacci, text="Retroceder")
        botonFibonacciRetroceder.pack(side=LEFT,padx=5, pady=5)

        frameNumerodelaSuerte = Frame(self)
        frameNumerodelaSuerte.pack(fill=X)

        letreroSuerte = Label(frameNumerodelaSuerte, text="Número De la Suerte", width=30)
        letreroSuerte.pack(side=LEFT, padx=5, pady=5)
        botonSuerteAvanzar = Button(frameNumerodelaSuerte, text="Avanzar")
        botonSuerteAvanzar.pack(side=LEFT, padx=5, pady=5)
        botonSuerteRetroceder = Button(frameNumerodelaSuerte, text="Retroceder")
        botonSuerteRetroceder.pack(side=LEFT,padx=5, pady=5)

        frameNumerodePadovan = Frame(self)
        frameNumerodePadovan.pack(fill=X)
        letreroPadovan = Label(frameNumerodePadovan, text="Número De Pavodan", width=30)
        letreroPadovan.pack(side=LEFT, padx=5, pady=5)
        botonPadovanAvanzar = Button(frameNumerodePadovan, text="Avanzar")
        botonPadovanAvanzar.pack(side=LEFT, padx=5, pady=5)
        botonPadovanRetroceder = Button(frameNumerodePadovan, text="Retroceder")
        botonPadovanRetroceder.pack(side=LEFT, padx=5, pady=5)

        #---------------------------------------

        frameNumeroFeliz = Frame(self)
        frameNumeroFeliz.pack(fill=X)
        letreroNumeroFeliz = Label(frameNumeroFeliz, text="¿Es Un Número Feliz?", width=30)
        letreroNumeroFeliz.pack(side=LEFT, padx=5, pady=5)
        campoEsNumeroFeliz = Subscriptor("numero feliz", 50)
        campoEsNumeroFeliz.place(x=150, y=110)


        frameNumerocapicua = Frame(self)
        frameNumerocapicua.pack(fill=X)
        letreroNumerocapicua = Label(frameNumerocapicua, text="¿Es Un Número Capicúa?", width=30)
        letreroNumerocapicua.pack(side=LEFT, padx=5, pady=5)
        campoEsNumerocapicua = Subscriptor("numero capicua", 50)
        campoEsNumerocapicua.place(x=150, y=140)


        frameNumeroDecimal = Frame(self)
        frameNumeroDecimal.pack(fill=X)
        letreroNumeroDecimal = Label(frameNumeroDecimal, text="El numero en decimal", width=30)
        letreroNumeroDecimal.pack(side=LEFT, padx=5, pady=5)
        campoEsNumeroDecimal = Subscriptor("decimal", 50)
        campoEsNumeroDecimal.place(x=150, y=170)



        frameNumeroBinario = Frame(self)
        frameNumeroBinario.pack(fill=X)
        letreroNumeroBinario = Label(frameNumeroBinario, text="El numero en Binario", width=30)
        letreroNumeroBinario.pack(side=LEFT, padx=5, pady=5)
        campoNumeroBinario = Subscriptor("binario", 50)
        campoNumeroBinario.place(x=150, y=200)

        frameNumeroHexadecimal = Frame(self)
        frameNumeroHexadecimal.pack(fill=X)
        letreroNumeroHexadecimal = Label(frameNumeroHexadecimal, text="El numero en hexadecimal", width=30)
        letreroNumeroHexadecimal.pack(side=LEFT, padx=5, pady=5)
        campoNumeroHexadecimal= Subscriptor("hexadecimal", 50)
        campoNumeroHexadecimal.place(x=150, y=226)

        frameNumeroaNombre = Frame(self)
        frameNumeroaNombre.pack(fill=X)
        letreroNumeroaNombre = Label(frameNumeroaNombre, text="El numero en Español", width=30)
        letreroNumeroaNombre.pack(side=LEFT, padx=5, pady=5)
        campoNumeroaNombre= Subscriptor("numero en espaniol", 50)
        campoNumeroaNombre.place(x=150, y=250)

        __numeroFibonacci = NumeroFibonacci()
        __numeroSuerte = NumeroDeLaSuerte()
        __numeroPadovan = SeriePadoVan()

        publicadorFibonacci = PublicadorBoton(['incrementar', 'decrementar', 'limpiar'], __numeroFibonacci)
        publicadorFibonacci.registrar('incrementar', campoEsNumeroFeliz)
        publicadorFibonacci.registrar('decrementar', campoEsNumeroFeliz)

        publicadorFibonacci.registrar('incrementar', campoEsNumerocapicua)
        publicadorFibonacci.registrar('decrementar', campoEsNumerocapicua)

        publicadorFibonacci.registrar('incrementar', campoEsNumeroDecimal)
        publicadorFibonacci.registrar('decrementar', campoEsNumeroDecimal)

        publicadorFibonacci.registrar('incrementar', campoNumeroBinario)
        publicadorFibonacci.registrar('decrementar', campoNumeroBinario)

        publicadorFibonacci.registrar('incrementar', campoNumeroHexadecimal)
        publicadorFibonacci.registrar('decrementar', campoNumeroHexadecimal)

        publicadorFibonacci.registrar('incrementar', campoNumeroaNombre)
        publicadorFibonacci.registrar('decrementar', campoNumeroaNombre)

        publicadorNumeroDeLaSuerte = PublicadorBoton(['incrementar', 'decrementar', 'limpiar'], __numeroSuerte)
        publicadorNumeroDeLaSuerte.registrar('incrementar', campoEsNumeroFeliz)
        publicadorNumeroDeLaSuerte.registrar('decrementar', campoEsNumeroFeliz)

        publicadorNumeroDeLaSuerte.registrar('incrementar', campoEsNumerocapicua)
        publicadorNumeroDeLaSuerte.registrar('decrementar', campoEsNumerocapicua)

        publicadorNumeroDeLaSuerte.registrar('incrementar', campoEsNumeroDecimal)
        publicadorNumeroDeLaSuerte.registrar('decrementar', campoEsNumeroDecimal)

        publicadorNumeroDeLaSuerte.registrar('incrementar', campoNumeroBinario)
        publicadorNumeroDeLaSuerte.registrar('decrementar', campoNumeroBinario)

        publicadorNumeroDeLaSuerte.registrar('incrementar', campoNumeroHexadecimal)
        publicadorNumeroDeLaSuerte.registrar('decrementar', campoNumeroHexadecimal)

        publicadorNumeroDeLaSuerte.registrar('incrementar', campoNumeroaNombre)
        publicadorNumeroDeLaSuerte.registrar('decrementar', campoNumeroaNombre)

        publicadorNumeroDePadovan= PublicadorBoton(['incrementar', 'decrementar', 'limpiar'], __numeroPadovan)
        publicadorNumeroDePadovan.registrar('incrementar', campoEsNumeroFeliz)
        publicadorNumeroDePadovan.registrar('decrementar', campoEsNumeroFeliz)

        publicadorNumeroDePadovan.registrar('incrementar', campoEsNumerocapicua)
        publicadorNumeroDePadovan.registrar('decrementar', campoEsNumerocapicua)

        publicadorNumeroDePadovan.registrar('incrementar', campoEsNumeroDecimal)
        publicadorNumeroDePadovan.registrar('decrementar', campoEsNumeroDecimal)

        publicadorNumeroDePadovan.registrar('incrementar', campoNumeroBinario)
        publicadorNumeroDePadovan.registrar('decrementar', campoNumeroBinario)

        publicadorNumeroDePadovan.registrar('incrementar', campoNumeroHexadecimal)
        publicadorNumeroDePadovan.registrar('decrementar', campoNumeroHexadecimal)

        publicadorNumeroDePadovan.registrar('incrementar', campoNumeroaNombre)
        publicadorNumeroDePadovan.registrar('decrementar', campoNumeroaNombre)


        def eventoSiguienteNumeroDePadovan(event):
             publicadorNumeroDePadovan.enviar("incrementar")

        def eventoAnteriorNumeroDePadovan(event):
            try:
                publicadorNumeroDePadovan.enviar("decrementar")
            except ValueError:
                pass

        def eventoSiguienteNumeroDeLaSuerte(event):
             publicadorNumeroDeLaSuerte.enviar("incrementar")

        def eventoAnteriorNumeroDeLaSuerte(event):
            try:
                publicadorNumeroDeLaSuerte.enviar("decrementar")
            except ValueError:
                pass

        def eventoSiguienteNumeroFibonacci(event):
             publicadorFibonacci.enviar("incrementar")

        def eventoanteriornumeroFibonacci(event):
            try:
                publicadorFibonacci.enviar("decrementar")
            except ValueError:
                pass



        botonFibonacciAvanzar.bind("<Button-1>", eventoSiguienteNumeroFibonacci)
        botonFibonacciRetroceder.bind("<Button-1>", eventoanteriornumeroFibonacci)
        botonSuerteAvanzar.bind("<Button-1>", eventoSiguienteNumeroDeLaSuerte)
        botonSuerteRetroceder.bind("<Button-1>", eventoAnteriorNumeroDeLaSuerte)
        botonPadovanAvanzar.bind("<Button-1>", eventoSiguienteNumeroDePadovan)
        botonPadovanRetroceder.bind("<Button-1>", eventoAnteriorNumeroDePadovan)


def main():

    root = Tk()
    root.geometry("600x400+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()