#funcion centrar ventana
def centrar_ventana(ventana,apli_ancho,apli_largo):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (apli_ancho/2))
    y = int((pantall_largo/2) - (apli_largo/2))
    return ventana.geometry(f"{apli_ancho}x{apli_largo}+{x}+{y}")
