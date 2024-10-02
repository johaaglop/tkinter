import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
from formulario.form_maestra_desingn import FormMaestroDesing

class FormMaestro(FormMaestroDesing):
    def __init__(self) -> None: #constrctor
        super().__init__()      #constructor padre