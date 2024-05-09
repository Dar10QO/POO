import tkinter as tk
from tkinter import messagebox
from index import Index 
from functools import partial

root = tk.Tk()
root.title("Inicio de Sesión")


label_nombre = tk.Label(root, text="Nombre de usuario:")
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()


label_apellido = tk.Label(root, text="Apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(root)
entry_apellido.pack()
button_check = tk.Button(root, text="Comprobar", command=partial)
button_check.pack()


root.mainloop()
