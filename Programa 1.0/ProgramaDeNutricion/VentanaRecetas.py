import customtkinter as ctk 
import tkinter as tk
import subprocess
import platform
from tkinter import filedialog,messagebox, simpledialog
from ProgramaDeNutricion.centerwin import center_window

class VentanaRecetas():
    def __init__(
            self,
        ) -> None:
        self.text_font = ctk.CTkFont(
            family="Rockwell", size=20, weight="normal"
        )
        self.small_text_font = ctk.CTkFont(
            family="Rockwell", size=18, weight="normal"
        )   

    def mostrar_tabla_recetas(self,dashboard,db_object):
            """Muestra la lista de recetas que se tengan"""

            #Creamos los frames necesarios
            recetas_frame = ctk.CTkFrame(dashboard.root)
            recetas_canvas = ctk.CTkCanvas(recetas_frame)
            scrollable_frame = ctk.CTkFrame(recetas_canvas)
            nueva_receta_btn = ctk.CTkButton(
                recetas_frame, text="Añadir nueva receta", command= lambda: self.nueva_receta(dashboard,db_object)
            )
            nueva_receta_btn.pack(padx=(0, 25), side="bottom", anchor=ctk.E)

            scrollable_frame.bind(
            "<Configure>",
            lambda e: recetas_canvas.configure(
                scrollregion=recetas_canvas.bbox("all")
            ),
            )
        
            scrollbarVertical = ctk.CTkScrollbar(
                recetas_frame,
                orientation=ctk.VERTICAL,
                command=recetas_canvas.yview,
                width=30,
            )
            scrollbarHorizontal = ctk.CTkScrollbar(
                recetas_frame,
                orientation=ctk.HORIZONTAL,
                command=recetas_canvas.xview,
                width=30,
            )
            recetas_canvas.create_window(
                (0, 0), window=scrollable_frame, anchor=ctk.N
            )
            recetas_canvas.configure(
                yscrollcommand=scrollbarVertical.set,
                xscrollcommand=scrollbarHorizontal.set,
            )
            scrollbarVertical.pack(side="right", fill="y")
            scrollbarHorizontal.pack(side="bottom", fill="x")
            recetas_canvas.pack(fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20))

            recetas = db_object.get_recetas()
            rec_col_headers = [
                "Nombre",
                "Descipción",
            ]

            mrec_col_widths = [450, 450]

            """Lista de recetas"""
            for pos, text in enumerate(rec_col_headers):

                col_cell = ctk.CTkLabel(
                    scrollable_frame,
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
                    scrollable_frame,
                    text="Ver receta",
                    font=self.small_text_font,
                    command=lambda receta_sk=i[0]: self.imprimir_pdf(receta_sk,db_object),
                )
                view_button.grid(row=row, column=len(rec_col_headers), padx=5)

                for j in range(1, 3):
                    entry = ctk.CTkEntry(
                        scrollable_frame,
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

            return recetas_frame

    def imprimir_pdf(self, receta_sk,db_object):

        receta_info=db_object.get_receta(receta_sk)
        pdf_file_path = receta_info["ruta"]
        try:
            if platform.system() == "Darwin":
                # macOS: Usa 'open' para abrir el visor de PDF predeterminado
                subprocess.run(["open", "-a", "Preview", pdf_file_path], check=True)
            elif platform.system() == "Windows":
                # Windows: Usa 'start' para abrir el visor de PDF predeterminado
                subprocess.run(["start", "", pdf_file_path], shell=True, check=True)
            else:
                # Otros sistemas: Ajusta según sea necesario
                messagebox.showerror("Plataforma no compatible", "Esta plataforma no está soportada.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error de impresión", "Error al intentar imprimir el PDF")

    def nueva_receta(self,dashboard,db_object):

        # Abre el cuadro de diálogo para seleccionar un archivo PDF
        ruta_pdf = filedialog.askopenfilename(
            title='Seleccionar archivo PDF',
            filetypes=[('PDF files', '*.pdf')]
        )

        if not ruta_pdf:
            # El usuario canceló la selección del archivo
            return

        nombre=ctk.StringVar()
        descripcion=ctk.StringVar()
        # Crear una nueva ventana de diálogo para ingresar el nombre y la descripción de la receta
        receta_info = ctk.CTkToplevel(dashboard.root)
        receta_info.title('Nueva Receta')
        center_window(receta_info, 400, 200)
        receta_info.resizable(False, False)
        receta_info.grab_set()

        nombre_label = ctk.CTkLabel(receta_info, text='Nombre:')
        nombre_label.place(relx=0.2,rely=0.2, anchor=ctk.NW)

        nombre_entry = ctk.CTkEntry(receta_info,textvariable=nombre)
        nombre_entry.place(relx=0.5,rely=0.2, anchor=ctk.NW)

        descripcion_label = ctk.CTkLabel(receta_info, text='Descripción:')
        descripcion_label.place(relx=0.2,rely=0.5, anchor=ctk.NW)

        descripcion_entry = ctk.CTkEntry(receta_info,textvariable=descripcion)
        descripcion_entry.place(relx=0.5,rely=0.5, anchor=ctk.NW)

        # Función para cerrar y aceptar la ventana de diálogo
        def cerrar_ventana():
            receta_info.destroy()

        boton_aceptar = ctk.CTkButton(
            receta_info,
            text='Aceptar',
            command=lambda: [cerrar_ventana(), db_object.add_receta((nombre.get(), descripcion.get(),ruta_pdf)),self.actualizar_tabla_recetas(dashboard,db_object)],
        )
        boton_aceptar.place(relx=0.6,rely=0.8, anchor=ctk.NW)

        boton_cancelar = ctk.CTkButton(receta_info, text='Cancelar', command=cerrar_ventana)
        boton_cancelar.place(relx=0.1,rely=0.8, anchor=ctk.NW)
        
    def actualizar_tabla_recetas(self, dashboard, db_object):

        dashboard.ventana_recetas.pack_forget()

        # Assuming this method returns the new frame
        recetas_frame = self.mostrar_tabla_recetas(dashboard, db_object)

        # Pack the new frame into the existing widget
        recetas_frame.pack(fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20))
