import tkinter as tk
from tkinter import *
import sys 




class Index: 
    def guardar():
        def __init__(self):
            self.datosUsuario = []
            self.app = Tk()
        
        def entrada(self):
            self.int = Entry (self.app)
    

        def guardarDatos(self, nombre, apellido):
            self.datosUsuario.append({'nombr':nombr, 'apellido':apellido})
            
        def datosImprimir(self):
            return self.datosContacto
        
        def imprimirError(self):
            try:
                print(datosUsuario)
            except:
                print("Error inesperado", sys.exc_info()[0]) 
                raise