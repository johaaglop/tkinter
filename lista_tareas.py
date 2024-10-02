import tkinter
ventana = tkinter.Tk()

saludo_label = tkinter.Label(ventana, text="Tareas de Tomazo", font=("Arial, 22")).pack(padx=20, pady=10)

tupla_tareas = ["Comer sus croquetas","Morder a sus mamis","Tomar agua","Hacer caca","Salir a pasear","Dar amor"]

for tarea in tupla_tareas:
    tkinter.Checkbutton(ventana, text=tarea, font=("Arial", 18)).pack(pady=20,padx=10)

ventana.mainloop()