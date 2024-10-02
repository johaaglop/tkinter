import tkinter

#crear ventana
ventana = tkinter.Tk()
#funcion
def a_binario():
    text = texto.get("1.0", tkinter.END) #"1,0" recupera el tex de linea 1, 1er caracter, END =hasta el final
    texto_bin = ""
    for letra in text:
        texto_bin += bin(ord(letra))[2:]
    texto.delete("1.0",tkinter.END) #borra texto
    texto.insert("1.0", texto_bin) #introduce respuesta
#aparece en ventana
label_texto = tkinter.Label(ventana,text="Conversor de texto a binario", font=("Arial", 18)).pack(padx=20,pady=10)
label_texto = tkinter.Label(ventana,text="Ingresa el texto a convertir:", font=("Arial", 12)).pack(padx=10,pady=0)
texto = tkinter.Text(ventana, width=40,height=5)
texto.pack(padx=20,pady=10)
boton = tkinter.Button(ventana, text="A binario",font=("Arial", 18), command=a_binario).pack(padx=20,pady=10)

#mostar ventana
ventana.mainloop()