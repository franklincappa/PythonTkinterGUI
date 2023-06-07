import tkinter as tk
ventana = tk.Tk()

def nuevo_archivo():
    print("Has presionado el menú")

def menu_iniciar_con_sistema_presionado():
    if iniciar_con_sistema.get():
        print("Opción establecida (iniciar con el sistema).")
    else:
        print("Opción deshabilitada (no iniciar con el sistema).")

def menu_tema_presionado():
    valor_tema = tema_elegido.get()
    if valor_tema == 1:
        print("Tema claro establecido.")
    elif valor_tema == 2:
        print("Tema oscuro establecido.")


ventana.title("Barra de menús en Tk")
ventana.config(width=400, height=300)
# Crear una barra de menús.
barra_menus = tk.Menu()
# Crear el primer menú.
menu_archivo = tk.Menu(barra_menus, tearoff=False)
img_menu_nuevo = tk.PhotoImage(file="archivo.png")

menu_archivo.add_command(
    label="Nuevo",
    accelerator="Ctrl+N",
    command=nuevo_archivo,
    image=img_menu_nuevo, #Opcional
    compound=tk.LEFT, #opcional
    state=tk.DISABLED #Opcional
)

ventana.bind_all("<Control-n>", nuevo_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.destroy)

#Menú Opciones
menu_opciones = tk.Menu(barra_menus, tearoff=False)
iniciar_con_sistema = tk.BooleanVar()
menu_opciones.add_checkbutton(
    label="Iniciar con sistema",
    command=menu_iniciar_con_sistema_presionado,
    variable=iniciar_con_sistema
)

#Submenu Tema
menu_tema = tk.Menu(barra_menus, tearoff=False)
tema_elegido = tk.IntVar()
tema_elegido.set(1)  # Opción seleccionada por defecto ("Claro").
menu_tema.add_radiobutton(
    label="Claro",
    variable=tema_elegido,
    value=1,
    command=menu_tema_presionado
)
menu_tema.add_radiobutton(
    label="Oscuro",
    value=2,
    variable=tema_elegido,
    command=menu_tema_presionado
)


# Agregarlo a la barra.
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
barra_menus.add_cascade(menu=menu_opciones, label="Opciones")
menu_opciones.add_cascade(menu=menu_tema, label="Tema")

# Insertarla en la ventana principal.
ventana.config(menu=barra_menus)
ventana.mainloop()