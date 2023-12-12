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

        # Insertar la nueva receta en la base de datos y mueve el docuemnto de un lado a otro
        self.db_object.add_receta((nombre,descripcion,ruta_pdf))


        
        