import customtkinter as ctk 
import tkinter as tk
from ProgramaDeNutricion.centerwin import center_window
from datetime import datetime

class VentanaPaciente():
    def __init__(
            self,
        ) -> None:
        self.text_font = ctk.CTkFont(
            family="Rockwell", size=20, weight="normal"
        )
        self.small_text_font = ctk.CTkFont(
            family="Rockwell", size=18, weight="normal"
        )   

    def mostrar_tabla_recetas(self,db_object,dashboard) -> None:
            """Muestra la lista de recetas que se tengan"""

            #Creamos los frames necesarios
            self.recetas_frame = ctk.CTkFrame(dashboard.root)
            self.recetas_canvas = ctk.CTkCanvas(self.recetas_frame)
            self.scrollable_frame = ctk.CTkFrame(self.recetas_canvas)

            self.scrollbarVertical = ctk.CTkScrollbar(
                self.recetas_frame,
                orientation=ctk.VERTICAL,
                command=self.recetas_canvas.yview,
                width=30,
            )
            self.scrollbarHorizontal = ctk.CTkScrollbar(
                self.recetas_frame,
                orientation=ctk.HORIZONTAL,
                command=self.recetas_canvas.xview,
                width=30,
            )

            recetas = db_object.get_recetas()
            rec_col_headers = [
                "Nombre",
                "Descipción",
            ]

            mrec_col_widths = [400, 400]

            """Lista de recetas"""
            for pos, text in enumerate(rec_col_headers):

                col_cell = ctk.CTkLabel(
                    self.recetas_frame,
                    text=text.capitalize(),
                    font=self.text_font,
                    width=mrec_col_widths[pos],
                    height=50,
                )
                col_cell.grid(
                    row=1, column=(pos), pady=(10, 20), ipady=1, padx=5
                )

            row = 2
            for i in recetas:

                # Create a button to view client information
                view_button = ctk.CTkButton(
                    self.recetas_frame,
                    text="Ver receta",
                    font=self.small_text_font,
                    # command=lambda receta_sk=i[0]: self.imprimir_pdf(receta_sk),
                )
                # Asignar la función al botón
                view_button.grid(row=row, column=len(rec_col_headers), padx=5)

                for j in range(1, 3):
                    entry = ctk.CTkEntry(
                        self.recetas_frame,
                        width=mrec_col_widths[j-1],
                        font=self.small_text_font,
                    )
                    entry.grid(row=row, column=(j-1), padx=5)

                    try:
                        entry.insert(ctk.END, i[j].capitalize())
                    except AttributeError:
                        try:
                            entry.insert(ctk.END, i[j])
                        except:
                            entry.insert(ctk.END,"")

                    entry.configure(state=ctk.DISABLED)

                row += 1



        
