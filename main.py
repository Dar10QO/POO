import tkinter as tk
from tkinter import messagebox
from index import Index
from functools import partial

def comprobar(index, nombre_entry, apellido_entry, output_text, error_label):
    try:
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        index.guardarDatos(nombre, apellido)
        print("Nombre:", nombre) 
    except NameError as e:
        print("Se ha producido un NameError:", e)
        error_label.config(text="Se ha producido un error al procesar los datos.")

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

output_text = tk.Text(root, height=5, width=30)
output_text.pack()

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

index = Index(root) 

button_check = tk.Button(root, text="Comprobar", command=partial(comprobar, index, entry_nombre, entry_apellido, output_text, error_label))
button_check.pack()

root.mainloop()
