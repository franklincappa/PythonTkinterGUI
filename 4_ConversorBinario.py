import tkinter as tk
ventana=tk.Tk()

def binario():
    texto_binario=""
    texto=texto_entry.get("1.0", tk.END)
    for letra in texto:
        texto_binario+=bin(ord(letra))[2:]
    
    texto_entry.delete=("1.0", tk.END)
    texto_entry.insert("1.0", texto_binario)



titulo_label=tk.Label(ventana,text="Ingrese un texto", font=("Arial", 16)).pack(padx=20, pady=10)
texto_entry= tk.Text(ventana, width=40, height=15)
texto_entry.pack(padx=20, pady=10)
convertir_button=tk.Button(ventana,text="Convertir",command=binario, font=("Arial", 16)).pack(padx=20, pady=10)
ventana.mainloop()