import tkinter as tk

ventana=tk.Tk()

lista_task= ["Introducción a Python", "Manejo de Variables", "Condionales", "Bucles en python", "Listas, Arrays, Tuplas"]

for tarea in lista_task:
    tk.Checkbutton(ventana, text=tarea, font=("Arial", 13)).pack(padx=20, pady=10)

ventana.mainloop()