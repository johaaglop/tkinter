import tkinter

ventana = tkinter.Tk()
#funcion login
def login():
    nombre = nombre_var.get()
    password = password_var.get()
    if nombre == "admin" and password == "12345":
        mensaje_label.configure(text="Acceso autorizado")
    else:
        mensaje_label.configure(text="Acceso Denegado!!")

#variables
nombre_var = tkinter.StringVar()
password_var = tkinter.StringVar()

#informacion en ventana
nombre_label = tkinter.Label(ventana, text="Nombre de usuario", font=("Arial, 18")).pack(padx=20, pady=10)
nombre_entry = tkinter.Entry(ventana, font=("Arial, 16"), textvariable=nombre_var).pack(padx=20, pady=10)
password_label = tkinter.Label(ventana, text="Password", font=("Arial, 18")).pack(padx=20, pady=10)
password_entry = tkinter.Entry(ventana, font=("Arial, 16"), textvariable=password_var).pack(padx=20, pady=10)

#mensaje de acceso
mensaje_label = tkinter.Label(ventana, text="", font=("Arial, 20"))
mensaje_label.pack(padx=20, pady=10)
#boton
boton_ingresar = tkinter.Button(ventana,text="Ingresar", font=("Arial", 18), command=login).pack(padx=20, pady=10)

#muestra la ventana
ventana.mainloop()