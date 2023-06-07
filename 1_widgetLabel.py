#pip install tk

import tkinter
#tkinter._test()

ventana = tkinter.Tk()
#ventana.config(bg="#00")
titulo=tkinter.Label(ventana,text="Hola mundo", font=("Arial",16,"bold"),padx=20,pady=40,bg="#000000",fg="#00ff00")
titulo.pack()
ventana.mainloop()
