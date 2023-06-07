import tkinter as tk
ventana=tk.Tk()

nombre_var = tk.StringVar()

def cambio_nombre():
    titulo_nombre.configure(text="Hola " + nombre_var.get())

titulo_nombre= tk.Label(ventana, text="Saludo", font=("Arial",18),padx=20, pady=10)
titulo_nombre.pack()

nombre=tk.Entry(ventana, font=("Arial", 18),textvariable=nombre_var)
nombre.pack(padx=20, pady=10)

boton_cambio=tk.Button(ventana, text="Cambio",font=("Arial", 18), command=cambio_nombre)
boton_cambio.pack(padx=20, pady=10)


ventana.mainloop()
