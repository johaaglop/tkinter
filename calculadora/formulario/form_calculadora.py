import tkinter as tk
from tkinter import font
from config import constantes as cons
import util.util_ventana as util_ventana


class FormCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window() #invocar funcion config_window
        self.construir_widget()


#configuracion de la ventana, color, transparencia, centrar
    def config_window(self):
        #configuracion inicial de la ventana
        self.title("Super Calculadora")
        #configura el color de fondo y transparencia de ventana
        self.configure(bg=cons.COLOR_FONDO_DARK)
        self.attributes("-alpha", 0.96)
        w, h = 370, 470
        util_ventana.centrar_ventana(self, w, h)

#widgets en ventana
    def construir_widget(self):
        #etiqueta muestra operacion solicitada
        self.operation_label = tk.Label(self, text="", font=(
            "Arial", 16), fg=cons.COLOR_TEXTO_DARK, bg=cons.COLOR_FONDO_DARK, justify="right")
        self.operation_label.grid(
            row=0, column=3, padx=10, pady=10)
        #pantalla de operacion
        self.entry = tk.Entry(self, width=15, font=(
            "Arial", 40), bd=0, fg=cons.COLOR_TEXTO_DARK, bg=cons.COLOR_CAJA_TEXTO_DARK, justify="right")
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        #Lista de botones
        buttons = [
            'C', '%', '<', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=',
        ]
        #ajustato para dejar espacio para la etiqueta de operacion
        row_val = 2
        col_val = 0
        # configurar la tipografia para botones
        roboto_font = font.Font(family="Roboto", size=16)

        for button in buttons:
            #color de fondo de los botones especiales
            if button in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                color_fondo = cons.COLOR_BOTONES_DARKESPECIAL
            #ajustar tamaño fuente
                button_font = font.Font(size=16, weight='bold')
            else:
                color_fondo = cons.COLOR_BOTONES_DARK
                button_font = roboto_font
            #ajuste boton =
            if button == '=':
                tk.Button(self, text=button, width=11,height=2,command=lambda b=button: self.on_button_click(b),
                          bg=color_fondo, fg=cons.COLOR_TEXTO_DARK, relief=tk.FLAT, font=button_font, padx=5, pady=5,
                          bd=0, borderwidth=0, highlightthickness=0, overrelief='flat').grid(row=row_val, column=col_val,
                          columnspan=2, pady=5)
                col_val += 1

            else:
                tk.Button(self, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b),
                          bg=color_fondo, fg=cons.COLOR_TEXTO_DARK, relief=tk.FLAT, font=button_font, padx=5, pady=5,
                          bd=0, borderwidth=0, highlightthickness=0,
                          overrelief='flat').grid(row=row_val, column=col_val, pady=5)
                col_val += 1

            if col_val > 3:
                col_val = 0
                row_val +=1

#acciones del boton
    def on_button_click(self, value):
        if value == '=':
            try:
                expression = self.entry.get().replace('%', '/100')
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                operation = expression + " " + value
                self.operation_label.config(text=operation)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.operation_label.config(text="")
        elif value == 'C':
            self.entry.delete(0, tk.END)
            self.operation_label.config(text="")
        elif value == '<':
            current_text = self.entry.get()
            if current_text:
                new_text = current_text[:-1] #eliminar ultimo caracter
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, new_text)
                self.operation_label.config(text=new_text + " ")
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END) #limpiar pantalla
            self.entry.insert(tk.END, current_text + value) #inserta valor
            if value == '=':
                self.operation_label.config(text="")







