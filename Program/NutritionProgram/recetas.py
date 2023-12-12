import customtkinter as ctk
from PIL import Image, ImageTk
import fitz  # PyMuPDF
import os
import shutil
import time
from NutritionProgram.centerwin import center_window
from NutritionProgram.database import Database

class receta:
    def __init__(self):
        self.db_object=Database("Recetas")

    def insertar_receta(self, nombre, descripcion,ruta_pdf):

        # Insertar la nueva receta en la base de datos y mueve el docuemnto de un lado a otro
        self.db_object.add_receta((nombre,descripcion,ruta_pdf))

    def visualizar_PDF(self,receta_sk):

        receta_info=self.db_object.get_receta(receta_sk)

        if not receta_info:
            print(f"No se encontró información de la receta con ID: {receta_sk}")
            return
        
        ruta_pdf = receta_info["ruta"]
        # Crear una nueva ventana para mostrar el PDF
        pdf_window = ctk.CTkToplevel()
        pdf_window.title(f"Visualizar PDF - {receta_info['Nombre']} - {receta_info['SK']}")  # Ajusta el índice según la estructura de tu respuesta de la base de datos
        # Cargar el documento PDF
        doc = fitz.open(ruta_pdf)
        # Crear un lienzo para mostrar las páginas del PDF
        pdf_canvas = ctk.CTkCanvas(pdf_window, bg="white")
        pdf_canvas.pack(fill="both", expand=True)
        
        # Recorrer las páginas y renderizarlas en el lienzo
        for num_pagina in range(len(doc)):
            pagina = doc.load_page(num_pagina)
            imagen = pagina.get_pixmap()
            imagen = Image.frombytes("RGB", [imagen.width, imagen.height], imagen.samples)
            imagen = ImageTk.PhotoImage(imagen)
            pdf_canvas.create_image(10, 10, anchor="nw", image=imagen)
        
        # Configurar el tamaño del lienzo
        pdf_canvas.config(scrollregion=pdf_canvas.bbox("all"))




        
        