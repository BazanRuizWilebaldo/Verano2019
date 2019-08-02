import tkinter as tk
from basesnumericas.ConversorDeBaseNumerica import ConversorBaseNumerica

class Subscriptor(tk.Entry):

    def __init__(self, nombredelabasenumerica, tamanio):
        tk.Entry.__init__(self)
        self.__baseNumerica = nombredelabasenumerica
        self.conversor = ConversorBaseNumerica()
        self.conversor.convertir(1, self.__baseNumerica)
        self.config(width=tamanio)

    def update2(self, numero):
        try:
            self.limpiar()
            texto = self.conversor.convertir(numero, self.__baseNumerica)
            self.insert(0, texto)
        except ValueError:
            self.limpiar()

    def limpiar(self):
        self.delete(0, 'end')



class PublicadorBoton:
    def __init__(self, events, numerofibonacci):
        self.__numeroFibonacci = numerofibonacci
        self.subscribers = {event: dict()
                            for event in events}

    def getsubscriptor(self, event):
        return self.subscribers[event]

    def registrar(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update2')
        self.getsubscriptor(event)[who] = callback

    def quitarderegistro(self, event, who):
        del self.getsubscriptor(event)[who]

    def enviar(self, event):
        if event.lower() == "incrementar":
            message = self.__numeroFibonacci.siguiente()
            for subscriber, callback in self.getsubscriptor(event).items():
                callback(message)
        elif event.lower() == "decrementar":
            message = self.__numeroFibonacci.retroceder()
            for subscriber, callback in self.getsubscriptor(event).items():
                callback(message)
        elif event.lower() == "limpiar":
            message = " "
            for subscriber, callback in self.getsubscriptor(event).items():
                callback(message)




