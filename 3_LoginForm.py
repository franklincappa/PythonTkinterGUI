import tkinter as tk
ventana=tk.Tk()

usuario= tk.StringVar()
password=tk.StringVar()


def login():
    nombre=usuario.get()
    clave=password.get()

    if nombre=="admin" and clave=="admin":
        label_login.configure(text="Datos Validos")
    else:
        label_login.configure(text="Datos Invalidos")


label_usuario=tk.Label(ventana, text="Nombre Usario", font=("Arial", 16)).pack(padx=20,pady=10)
entry_usuario= tk.Entry(ventana,font=("Arial", 16), textvariable=usuario).pack(padx=20,pady=10)
label_password=tk.Label(ventana, text="Contraseña", font=("Arial", 16)).pack(padx=20,pady=10)
entry_password= tk.Entry(ventana,font=("Arial", 16), textvariable=password).pack(padx=20,pady=10)
button_ingresar= tk.Button(ventana, text="Ingresar", font=("Arial", 18), command=login).pack(padx=20,pady=10)

label_login=tk.Label(ventana, text="", font=("Arial", 16), fg="#00ff00")
label_login.pack(padx=20,pady=10)


ventana.mainloop()
