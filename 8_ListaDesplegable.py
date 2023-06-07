import tkinter as tk
from tkinter import messagebox,ttk

def mostrar_seleccion():
    selection = combo.get()
    index= combo.current() #obtiene el indice
    messagebox.showinfo(
        message="La opción seleccionada es: " + selection + ", indice: "+ str(index),
        title="Selección"
    )

def selection_changed(event):
    selection=combo.get()
    messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=selection
    )

root = tk.Tk()
root.config(width=300, height=200)
root.title("ComboBox")
combo=ttk.Combobox(
    state="readonly",
    values=["Python","Csharp","Typescript","PHP", "Transact SQL"]
)
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=50, y=50)

mostrar_button = ttk.Button(text="Mostrar Selección", command=mostrar_seleccion)
mostrar_button.place(x=50, y=100)

root.mainloop()