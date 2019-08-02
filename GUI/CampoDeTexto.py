import tkinter as tk
from basesnumericas.ConversorDeBaseNumerica import ConversorBaseNumerica

class CampoDeTexto(tk.Entry):

    def __init__(self,nombredelabasenumerica,tamanio):
        tk.Entry.__init__(self)
        self.__baseNumerica = nombredelabasenumerica
        self.conversor = ConversorBaseNumerica()
        self.conversor.convertir(1, self.__baseNumerica)
        self.config(width=tamanio)

    def insertartexto(self, numero):
        self.limpiar()
        texto = self.conversor.convertir(numero, self.__baseNumerica)
        self.insert(0, texto)

    def limpiar(self):
        self.delete(0, 'end')