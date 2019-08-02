import tkinter as tk
from observerpattern.PatronGUI import  Subscriptor, PublicadorBoton
from sucesiones.Padovan import SeriePadoVan
class Appfibonacci(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack()
        self.frames = {}
        frame = PanelPrincipal(container, self)
        self.frames[PanelPrincipal] = frame
        frame.grid(row=5, column=2)
        self.show_frame(PanelPrincipal)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class PanelPrincipal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        letreroprincipal = tk.Label(self, text="  Numero Fibonacci", font=("Verdana", 12))
        letreroprincipal.grid(row=0, column=0)
        incrementar = tk.Button(self, text="incrementar")
        incrementar.grid(row=1, column=0)
        decrementar = tk.Button(self, text="decrementar")
        decrementar.grid(row=1, column=1)
        #__numero = NumeroFibonacci()
        #__numero = NumeroDeLaSuerte()
        __numero = SeriePadoVan()



        campotextobinario = Subscriptor("decimal", 50)
        campotextobinario.pack()

        campotextohexadecimal = Subscriptor("hexadecimal", 50)
        campotextohexadecimal.pack()

        letrerobasesnumericas = tk.Label(self, text=" Numero en binario y hexadecimal")
        letrerobasesnumericas.grid(row=2, column=0)

        publicadorFibonacci = PublicadorBoton(['incrementar', 'decrementar','limpiar'], __numero)
        publicadorFibonacci.registrar('incrementar', campotextohexadecimal)
        publicadorFibonacci.registrar('decrementar', campotextohexadecimal)
        publicadorFibonacci.registrar('incrementar', campotextobinario)
        publicadorFibonacci.registrar('decrementar', campotextobinario)
        publicadorFibonacci.registrar('limpiar', campotextohexadecimal)
        publicadorFibonacci.registrar('limpiar', campotextobinario)
        # publicadorFibonacci.pack()

        def eventosiguientenumero(event):
             publicadorFibonacci.enviar("incrementar")

        def eventoanteriornumero(event):
            try:
                publicadorFibonacci.enviar("decrementar")
            except ValueError:
                publicadorFibonacci.enviar("limpiar")

        decrementar.bind("<Button-1>", eventoanteriornumero)
        incrementar.bind("<Button-1>", eventosiguientenumero)


app = Appfibonacci()
app.mainloop()