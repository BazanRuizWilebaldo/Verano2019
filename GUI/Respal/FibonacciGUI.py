import tkinter as tk
from numerofibonacci.NumeroFibonacci import NumeroFibonacci
from GUI.CampoDeTexto import CampoDeTexto

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
    __numero = NumeroFibonacci()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        letreroprincipal = tk.Label(self, text="  Numero Fibonacci", font=("Verdana", 12))
        letreroprincipal.grid(row=0, column=0)
        incrementar = tk.Button(self, text="incrementar")
        incrementar.grid(row=1, column=0)
        decrementar = tk.Button(self, text="decrementar")
        decrementar.grid(row=1, column=1)

        campotextobinario = CampoDeTexto("binario", 50)
        campotextobinario.pack()

        campotextohexadecimal = CampoDeTexto("hexadecimal", 50)
        campotextohexadecimal.pack()

        letrerobasesnumericas = tk.Label(self, text=" Numero en binario y hexadecimal")
        letrerobasesnumericas.grid(row=2, column=0)

        def eventosiguientenumero(event):
            try:
                self.__numero.siguiente()
                numerosiguiente = self.__numero.guardarEnlista().pop()
                campotextobinario.insertartexto(numerosiguiente)
                campotextohexadecimal.insertartexto(numerosiguiente)
            except ValueError:
                campotextohexadecimal.limpiar()
                campotextobinario.limpiar()

        def eventoanteriornumero(event):
            try:
                self.__numero.retroceder()
                numeroanterior = self.__numero.guardarEnlista().pop()
                campotextohexadecimal.insertartexto(numeroanterior)
                campotextobinario.insertartexto(numeroanterior)
            except ValueError:
                campotextohexadecimal.limpiar()
                campotextobinario.limpiar()

        decrementar.bind("<Button-1>", eventoanteriornumero)
        incrementar.bind("<Button-1>", eventosiguientenumero)


app = Appfibonacci()
app.mainloop()