import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()
main_window.title("Vista de árbol en Tkinter")
treeview = ttk.Treeview(columns=("size", "lastmod"))
treeview.heading("#0", text="Archivo")
treeview.heading("size", text="Tamaño")
treeview.heading("lastmod", text="Última modificación")
icon = tk.PhotoImage(file="archivo.png")
treeview.insert(
    "",
    tk.END,
    text="README.txt",
    values=("850 bytes", "18:30"),
    image=icon
)
treeview.pack()
main_window.mainloop()