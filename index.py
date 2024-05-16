import tkinter as tk

class Index:
    def __init__(self, root):
        self.datosUsuario = []
        self.app = root

    def guardarDatos(self, nombre, apellido):
        self.datosUsuario.append({'nombre': nombre, 'apellido': apellido})
