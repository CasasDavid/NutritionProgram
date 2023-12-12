import customtkinter as ctk
from PIL import Image
import fitz  # PyMuPDF
import os
import shutil
from NutritionProgram.centerwin import center_window
from NutritionProgram.database import Database

class receta:
    def __init__(self):
        self.db_object=Database("Recetas")



    def insertar_receta(self, nombre, descripcion,ruta_pdf):

        # Insertar la nueva receta en la base de datos
        receta=self.db_object.add_receta((nombre,descripcion))

        if receta:

            # Directorio de destino para copiar el PDF
            directorio_destino = 'assets/recetas/'

            # Nombre del archivo en el directorio de destino
            nombre_archivo_destino = f"{nombre}.pdf"

            # Ruta completa del archivo en el directorio de destino
            ruta_destino = os.path.join(directorio_destino, nombre_archivo_destino)

            # Copiar el archivo PDF al directorio de destino
            shutil.copy(ruta_pdf, ruta_destino)

        
        