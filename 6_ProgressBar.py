import tkinter as tk
from tkinter import ttk

ventana=tk.Tk()
ventana.title("Barra de Progreso en TK")
ventana.iconbitmap('c:/python/gui.ico')
progressBar= ttk.Progressbar(maximum=200)
#progressBar= ttk.Progressbar(orient=tk.VERTICAL)
progressBar.place(x=30, y=60, width=200)
#progressBar.place(x=30, y=30, height=160)
progressBar.step(50)

#ProgressBar Indeterminado
#progressBar= ttk.Progressbar(mode="indeterminate")
#progressBar.place(x=30, y=60, width=200)
#progressBar.start()

ventana.geometry("300x200")
ventana.mainloop()