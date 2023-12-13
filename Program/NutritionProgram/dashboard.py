import customtkinter as ctk 
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import platform
from tkinter import filedialog,messagebox, simpledialog
from datetime import datetime
from NutritionProgram.centerwin import center_window
from NutritionProgram.database import Database
from NutritionProgram.recetas import receta


class Dashboard:
    """
    This class is used to create the dashboard for the user.
    This is where most of the program will be run from.
    """

    def __init__(
        self,
        width: int = 2100,
        height: int = 720,
        appearance: str = "dark",
        theme_color: str = "blue",
        userName: str = "",
    ) -> None:
        """Constructor for Dashboard class for Asclepius.

        Args:
            width (int): width of the window
            height (int): height of the window
            appearance (str): ['light', 'Dark']
            theme_color (str): ['blue','green','dark-blue']
            dataset (list): list of lists containing the data
            col_headers (list): list of strings containing the column headers
        """

        self.width = width
        self.height = height
        self.user_id = userName

        self.db_object = Database("Dashboard")
        self.receta_manager=receta()

        self.dataset = self.db_object.get_patients()
        self.col_headers = self.db_object.get_col_headings("PatientTable")

        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(theme_color)

        self.root = ctk.CTk()
        self.root.title("Nutrition Plan Assistant 1.0")
        # self.root.resizable(False, False)

        self.title_logo = ctk.CTkImage(
            Image.open("assets/images/logo.jpg"), size=(125, 100)
        )

        self.order_list = []
        self.column_widths = [200, 200, 200, 125, 200, 60, 90]
        self.column_widths_register = [200, 200, 200, 200, 200, 200, 200]

        # ------------------------ Fonts ------------------------#
        self.op_font = ctk.CTkFont(
            family="Rockwell", size=30, weight="bold", underline=True
        )
        self.title_font = ctk.CTkFont(
            family="Rockwell", size=40, weight="bold"
        )
        self.text_font = ctk.CTkFont(
            family="Rockwell", size=20, weight="normal"
        )
        self.text_font_bold = ctk.CTkFont(
            family="Rockwell", size=20, weight="bold"
        )
        self.small_text_font = ctk.CTkFont(
            family="Rockwell", size=18, weight="normal"
        )
        self.tagline_font = ctk.CTkFont(
            family="Rockwell", size=15, weight="normal"
        )
        # ------------------------ Frames ------------------------#
        self.dashboard_frame = ctk.CTkFrame(self.root)
        self.mhelp_frame = ctk.CTkFrame(self.root)
        # self.new_patient = ctk.CTkFrame(self.root)
        self.__name = ctk.StringVar()
        self.__apellido = ctk.StringVar()
        self.__email = ctk.StringVar()
        self.__edad = ctk.IntVar()
        self.__estatura = ctk.IntVar()
        self.__ID = ctk.StringVar()
        self.__telefono=ctk.StringVar()
        self.__peso=ctk.IntVar()
        self.__genero=ctk.StringVar()
        self.__alergia=ctk.StringVar()
        self.__examenes=ctk.StringVar()
        self.__actividad=ctk.StringVar()

        self.meds_frame = ctk.CTkFrame(self.root)
        self.meds_canvas = ctk.CTkCanvas(self.meds_frame)
        self.scrollable_frame = ctk.CTkFrame(self.meds_canvas)
        self.scrollbarVertical = ctk.CTkScrollbar(
            self.meds_frame,
            orientation=ctk.VERTICAL,
            command=self.meds_canvas.yview,
            width=30,
        )
        self.scrollbarHorizontal = ctk.CTkScrollbar(
            self.meds_frame,
            orientation=ctk.HORIZONTAL,
            command=self.meds_canvas.xview,
            width=30,
        )

        self.mrec_frame = ctk.CTkFrame(self.root)
        self.mrec_canvas = ctk.CTkCanvas(self.mrec_frame)
        self.scrollable_frame_mrec = ctk.CTkFrame(self.mrec_canvas )
        self.scrollbarVertical_mrec = ctk.CTkScrollbar(
            self.mrec_frame,
            orientation=ctk.VERTICAL,
            command=self.meds_canvas.yview,
            width=30,
        )
        self.scrollbarHorizontal_mrec = ctk.CTkScrollbar(
            self.mrec_frame,
            orientation=ctk.HORIZONTAL,
            command=self.meds_canvas.xview,
            width=30,
        )

    def title_frame(self, title: str) -> None:
        """Create the title frame.

        Args:
            title (str): title of the frame
        """

        title_frame = ctk.CTkFrame(
            self.root, width=self.width - 200, height=50, corner_radius=10
        )

        title_label = ctk.CTkLabel(
            title_frame, text=title, font=self.title_font
        )

        tagline_label = ctk.CTkLabel(
            title_frame, text=" Auriculoterapia para bajar de peso, saludablemente, sin rebote... y sin dejar de comer.", font=self.tagline_font
        )

        title_logo_label = ctk.CTkLabel(
            title_frame, image=self.title_logo, text=""
        )

        title_label.pack(side=ctk.LEFT, padx=(20, 0))
        tagline_label.place(relx=0.5, rely=0.4, anchor=ctk.CENTER, y=20)
        title_logo_label.pack(side=ctk.RIGHT, padx=(0, 20))

        title_frame.pack(side=ctk.TOP, fill=ctk.X, padx=(0, 20), pady=20)

    def update_table(self):
        # Actualiza el conjunto de datos y los encabezados de columna
        self.dataset = self.db_object.get_patients()
        self.col_headers = self.db_object.get_col_headings("PatientTable")
        self.display_table()

    def update_table(self):
        # Actualiza el conjunto de datos y los encabezados de columna
        self.dataset = self.db_object.get_patients()
        self.col_headers = self.db_object.get_col_headings("PatientTable")
        self.display_mrec()
    
    def navigation_frame(self) -> None:
        """Create the navigation frame."""

        navigation_frame = ctk.CTkFrame(
            self.root, width=250, height=self.height, corner_radius=15
        )

        navigation_title = ctk.CTkLabel(
            navigation_frame, text="Menú", font=self.op_font
        )

        dashboard_button = ctk.CTkButton(
            navigation_frame,
            text=" Usuario Actual ",
            font=self.text_font_bold,
            command=lambda: self.reset_frame("home"),
            corner_radius=10,
            height=40,
        )

        meds_button = ctk.CTkButton(
            navigation_frame,
            text=" Crear paciente ",
            font=self.text_font_bold,
            command=lambda: self.reset_frame("meds"),
            corner_radius=10,
            height=40,
        )

        mhelp_button = ctk.CTkButton(
            navigation_frame,
            text=" Silueta ",
            font=self.text_font_bold,
            command=lambda: self.reset_frame("mhelp"),
            corner_radius=10,
            height=40,
        )

        mrecord_button = ctk.CTkButton(
            navigation_frame,
            text=" Planes diarios ",
            font=self.text_font_bold,
            command=lambda: self.reset_frame("mrecord"),
            corner_radius=10,
            height=40,
        )

        light_mode = ctk.CTkButton(
            navigation_frame,
            text=" Modo claro ",
            font=self.text_font_bold,
            height=30,
            command=lambda: self.change_appearance_mode_event("Light"),
        )

        dark_mode = ctk.CTkButton(
            navigation_frame,
            text=" Modo oscuro ",
            font=self.text_font_bold,
            height=30,
            command=lambda: self.change_appearance_mode_event("Dark"),
        )

        quit_button = ctk.CTkButton(
            navigation_frame,
            text=" Salir ",
            font=self.text_font_bold,
            command=self.root.destroy,
            corner_radius=10,
            height=40,
        )

        navigation_frame.pack(side=ctk.LEFT, fill=ctk.Y, padx=20, pady=20)

        navigation_title.pack(pady=20)

        dashboard_button.pack(pady=15)
        meds_button.pack(pady=15)
        mrecord_button.pack(pady=15)
        mhelp_button.pack(pady=15)

        quit_button.pack(pady=15, side=ctk.BOTTOM)
        light_mode.pack(pady=15, side=ctk.BOTTOM)
        dark_mode.pack(pady=15, side=ctk.BOTTOM)

    def reset_frame(self, frame_name) -> None:
        """Changes the frame to the given frame. Forgets the other frames.

        Args:
            frame_name (str): name of the frame to be displayed
        """

        if frame_name == "home":
            self.dashboard_frame.pack(
                fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
            )
        else:
            self.dashboard_frame.pack_forget()

        if frame_name == "meds":
            self.meds_frame.pack(
                fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
            )
        else:
            self.meds_frame.pack_forget()

        if frame_name == "mhelp":
            self.mhelp_frame.pack(
                fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
            )
        else:
            self.mhelp_frame.pack_forget()

        if frame_name == "mrecord":
            self.mrec_frame.pack(
                fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
            )
        else:
            self.mrec_frame.pack_forget()

        print("Frame reset to", frame_name)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Change the appearance mode.

        Args:
            new_appearance_mode (str): The new appearance mode.
        """

        ctk.set_appearance_mode(new_appearance_mode)
        print("Appearance mode changed to", new_appearance_mode, "mode")

    def order_check_button(self, mid: str) -> None:
        """Check button pressed. Add or remove the medicine from the order list.

        Args:
            mid (str): Medicine ID
        """
        try:
            self.order_list.remove(mid)
            print("Removed", mid)
        except ValueError:
            self.order_list.append(mid)
            print("Added", mid)

    def final_confirm_button_pressed(self) -> None:
        """Final confirm button pressed. Place the order."""

        self.db_object.add_orders(self.order_list, self.user_id)

        self.order_list = []
        self.order_confirmation.destroy()
        print("Order placed.")

    def new_patient(self) -> None:
        """Pop up a window to add new patient. """

        self.new_patient = ctk.CTkToplevel(self.root)
        self.new_patient.title("Información del nuevo paciente")
        self.new_patient.resizable(False, False)
        self.new_patient.grab_set()


        center_window(self.new_patient, 1500, 800)

        ctk.CTkLabel(
            self.new_patient,
            text="Nombre",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.10, anchor=ctk.NW)

        entryName = ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__name,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryName.place(relx=0.2, rely=0.10,  anchor=ctk.NW) 

        ctk.CTkLabel(
            self.new_patient,
            text="Apellido",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.10, anchor=ctk.NW)

        entryApellido=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__apellido,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryApellido.place(relx=0.7, rely=0.1,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="ID",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.20, anchor=ctk.NW)

        entryID=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__ID,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryID.place(relx=0.2, rely=0.2,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="Teléfono",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.20, anchor=ctk.NW)

        entrytelefono=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__telefono,
            font=self.small_text_font,
            width=300, height=30,
        )
        entrytelefono.place(relx=0.7, rely=0.20,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="Email",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.30, anchor=ctk.NW)

        entryemail=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__email,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryemail.place(relx=0.2, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Estatura", font=self.small_text_font
        ).place(relx=0.5, rely=0.30, anchor=ctk.NW)

        entryestatura=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__estatura,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryestatura.place(relx=0.7, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Peso", font=self.small_text_font
        ).place(relx=0.1, rely=0.40, anchor=ctk.NW)

        entrypeso=ctk.CTkEntry(
            self.new_patient,
            font=self.small_text_font,
            width=300, height=30,
            textvariable=self.__peso,
        )
        entrypeso.place(relx=0.2, rely=0.40,  anchor=ctk.NW)
       
        ctk.CTkLabel(
            self.new_patient, text="Edad", font=self.small_text_font
        ).place(relx=0.5, rely=0.40, anchor=ctk.NW)

        entryedad=ctk.CTkEntry(
            self.new_patient,
            font=self.small_text_font,
            width=300, height=30,
            textvariable=self.__edad,
        )
        entryedad.place(relx=0.7, rely=0.40,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Género", font=self.small_text_font
        ).place(relx=0.1, rely=0.50, anchor=ctk.NW)
 
        entrygenero=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__genero,
            values=["Masculino","Femenino","Otro"],
        )
        entrygenero.place(relx=0.2,rely=0.50, anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Alergias", font=self.small_text_font
        ).place(relx=0.5, rely=0.50, anchor=ctk.NW)
 
        entryalergia=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__alergia,
            values=["Nueces", "Mariscos","Fresas","Gluten", "Lactosa", "Ninguna"],
        )
        entryalergia.place(relx=0.7,rely=0.50, anchor=ctk.NW)
        
        ctk.CTkLabel(
            self.new_patient, text="Actividad física", font=self.small_text_font
        ).place(relx=0.1, rely=0.60, anchor=ctk.NW)
 
        entryactividad=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__actividad,
            values=["1-3 veces por semana","4-5 veces por semana","6 o más veces por semana", "Nula"],
        )
        entryactividad.place(relx=0.2,rely=0.60, anchor=ctk.NW)
        
        ctk.CTkLabel(
            self.new_patient, text="¿Tiene exámenes recientes?", font=self.small_text_font
        ).place(relx=0.5, rely=0.60, anchor=ctk.NW)
 
        entryexamenes=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__examenes,
            values=["Sí", "No"],
        )
        entryexamenes.place(relx=0.7,rely=0.60, anchor=ctk.NW)

        entryName.delete(0, ctk.END) 
        entryApellido.delete(0, ctk.END) 
        entryID.delete(0, ctk.END) 
        entrytelefono.delete(0, ctk.END) 
        entryemail.delete(0, ctk.END) 
        entryestatura.delete(0, ctk.END) 
        entrypeso.delete(0, ctk.END) 
        entryedad.delete(0, ctk.END) 


        # Create a button to add the patient
        ctk.CTkButton(
            self.new_patient,
            text="Añadir paciente",
            font=self.small_text_font,
            command=self.add_patient_button_click,
        ).place(relx=0.45, rely=0.95,  anchor=ctk.CENTER)
        
        self.new_patient.lift()
        self.new_patient.focus_force

        # Agrega un botón para cerrar la ventana emergente

        close_button = ctk.CTkButton(
            self.new_patient,
            text="Cerrar",
            font=self.small_text_font,
            command=lambda:[self.new_patient.destroy(), self.update_table()],
        )
        close_button.place(relx=0.55, rely=0.95, anchor=ctk.CENTER)

    def add_patient_button_click(self):
        # Retrieve the data from the entry widgets
        nombre = self.__name.get()
        apellido = self.__apellido.get()
        ID = self.__ID.get()
        telefono=self.__telefono.get()
        email = self.__email.get()
        estatura = self.__estatura.get()
        peso=self.__peso.get()
        edad = self.__edad.get()
        genero=self.__genero.get()
        alergias=self.__alergia.get()
        actividad=self.__actividad.get()
        examenes=self.__examenes.get()

        # Create an instance of the Database class
        database = Database()

        # Call the add_patient method with the retrieved data
        success = database.add_patient((nombre, apellido,ID, telefono, email, estatura, peso, edad, genero, alergias, actividad, examenes))

        if success:
            print("Patient added successfully")
        else:
            print("Failed to add patient")

    def upload_patient_button_click(self,SK):
        # Retrieve the data from the entry widgets
        nombre = self.__name.get()
        apellido = self.__apellido.get()
        ID = self.__ID.get()
        telefono=self.__telefono.get()
        email = self.__email.get()
        estatura = self.__estatura.get()
        peso=self.__peso.get()
        edad = self.__edad.get()
        genero=self.__genero.get()
        alergias=self.__alergia.get()
        actividad=self.__actividad.get()
        examenes=self.__examenes.get()

        # Create an instance of the Database class
        database = Database()

        # Call the add_patient method with the retrieved data
        success = database.upload_patient((nombre, apellido,ID, telefono, email, estatura, peso, edad, genero, alergias, actividad, examenes),SK)

        if success:
            print("Patient uploaded successfully")
        else:
            print("Failed to upload patient")

    def display_table(self) -> None:

        """Display the table of medicines."""
        for pos, text in enumerate(self.col_headers[0:5]):

            col_cell = ctk.CTkLabel(
                self.scrollable_frame,
                text=text.capitalize(),
                font=self.text_font,
                width=self.column_widths[pos],
                height=50,
            )
            col_cell.grid(
                row=1, column=(pos), pady=(10, 20), ipady=1, padx=5
            )

        row = 2
        for i in self.dataset:

            # Create a button to view client information
            view_button = ctk.CTkButton(
                self.scrollable_frame,
                text="View",
                font=self.small_text_font,
                command=lambda client_id=i[0]: self.view_patient_info(client_id),
            )
            view_button.grid(row=row, column=len(self.col_headers), padx=5)


            for j in range(0, 5):
                entry = ctk.CTkEntry(
                    self.scrollable_frame,
                    width=self.column_widths[j],
                    font=self.small_text_font,
                )
                entry.grid(row=row, column=(j), padx=5)

                try:
                    entry.insert(ctk.END, i[j].capitalize())
                except AttributeError:
                    try:
                        entry.insert(ctk.END, i[j])
                    except:
                        entry.insert(ctk.END,"")

                entry.configure(state=ctk.DISABLED)

            row += 1

    def display_mrec(self) -> None:
        """Muestra la lista de recetas que se tengan"""

        mrec = self.db_object.get_recetas()
        mrec_col_headers = [
            "Nombre",
            "Descipción",
        ]

        mrec_col_widths = [400, 400]

        """Lista de recetas"""
        for pos, text in enumerate(mrec_col_headers):

            col_cell = ctk.CTkLabel(
                self.scrollable_frame_mrec,
                text=text.capitalize(),
                font=self.text_font,
                width=mrec_col_widths[pos],
                height=50,
            )
            col_cell.grid(
                row=1, column=(pos), pady=(10, 20), ipady=1, padx=5
            )

        row = 2
        for i in mrec:

            # Create a button to view client information
            view_button = ctk.CTkButton(
                self.scrollable_frame_mrec,
                text="Ver receta",
                font=self.small_text_font,
                command=lambda receta_sk=i[0]: self.imprimir_pdf(receta_sk),
            )
            # Asignar la función al botón
            view_button.grid(row=row, column=len(mrec_col_headers), padx=5)

            for j in range(1, 3):
                entry = ctk.CTkEntry(
                    self.scrollable_frame_mrec,
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

    def new_receta(self):

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
        receta_info = ctk.CTkToplevel(self.root)
        receta_info.title('Nueva Receta')
        center_window(receta_info, 400, 200)
        receta_info.resizable(False, False)
        receta_info.grab_set()

        nombre_label = ctk.CTkLabel(receta_info, text='Nombre:')
        # nombre_label.grid(row=0, column=0, sticky='e', padx=5, pady=5)
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
            command=lambda: [cerrar_ventana(), self.receta_manager.insertar_receta(nombre.get(), descripcion.get(),ruta_pdf),self.display_mrec()]
        )
        boton_aceptar.place(relx=0.6,rely=0.8, anchor=ctk.NW)

        boton_cancelar = ctk.CTkButton(receta_info, text='Cancelar', command=cerrar_ventana)
        boton_cancelar.place(relx=0.1,rely=0.8, anchor=ctk.NW)

        # Actualiza la visualización de las recetas
        self.display_mrec()
        
    def show_dashboard_frame(self) -> None:
        """Display the user dashboard."""

        # ------------------------ User Dashboard ------------------------#
        self.dashboard_frame = ctk.CTkFrame(self.root)

        ctk.CTkLabel(
            self.dashboard_frame,
            text="Nutrition Plan Assistant",
            font=self.op_font,
        ).pack(padx=20, pady=20) 
        ctk.CTkLabel(
            self.dashboard_frame,
            text="""¡Tu aliado #1 en planificación y control nutricional!""",
            font=self.text_font,
            anchor=ctk.CENTER,
        ).pack(anchor=ctk.CENTER, padx=20, pady=(20, 40))

        user_detail_labels = [
            "SK DE USUARIO: ",
            "USERNAME: ",
            "NOMBRE: ",
            "APELLIDO: ",
            "EMAIL: ",
        ]
        user_details = self.db_object.get_signupdetails(self.user_id)

        for i in range(len(user_details) - 1):

            if user_details[i] == "":
                text_label = "Not Provided"
            else:
                try:
                    text_label = user_details[i].capitalize()
                except AttributeError:
                    text_label = user_details[i]

            ctk.CTkLabel(
                self.dashboard_frame,
                text=f"{user_detail_labels[i]} : {text_label}",
                font=self.text_font,
                anchor=ctk.W,
            ).pack(anchor=ctk.W, padx=40, pady=20)

        # ------------------------ User Dashboard ------------------------#

        # ----------------------- Medicines Dashboard -----------------------#

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.meds_canvas.configure(
                scrollregion=self.meds_canvas.bbox("all")
            ),
        )

        place_order_button = ctk.CTkButton(
            self.meds_frame, text="Añadir paciente nuevo", command=self.new_patient
        )
        place_order_button.pack(padx=(0, 25), side="bottom", anchor=ctk.E)

        self.meds_canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor=ctk.N
        )
        self.meds_canvas.configure(yscrollcommand=self.scrollbarVertical.set)
        self.meds_canvas.configure(xscrollcommand=self.scrollbarHorizontal.set)

        self.scrollbarVertical.pack(side="right", fill="y")
        self.scrollbarHorizontal.pack(side="bottom", fill="x")
        self.meds_canvas.pack(side="left", fill="both", expand=True)

        self.display_table()

        # ----------------------- Medicines Dashboard -----------------------#

        # ----------------------- Med Help Dashboard -----------------------#

        wellness_description = """
To ensure students’s well-being, Bennett provides a well-equipped wellness centre with four beds and round-the-clock,
with a small nursing staff on standby. A well-qualified general physician is available on campus 24*7.For prolonged 
medical illness, or for case of infection, recovery rooms are available. The centre organizes health check-up camps, 
blood donation drives, and physiotherapy sessions for students and staff.

Asclepius is a platform for students to access the wellness centre from anywhere. It provides all the necessary 
services and information about the wellness centre.
"""

        ctk.CTkLabel(
            self.mhelp_frame,
            text="Acerca de Silueta",
            font=self.op_font,
            anchor=ctk.CENTER,
        ).pack(padx=(20, 20), pady=20)
        ctk.CTkLabel(
            self.mhelp_frame,
            text=wellness_description,
            font=self.small_text_font,
        ).pack(anchor=ctk.CENTER, padx=20)
        ctk.CTkLabel(
            self.mhelp_frame, text="Contáctanos", font=self.op_font
        ).pack(anchor=ctk.W, padx=20, pady=20)
        ctk.CTkLabel(
            self.mhelp_frame,
            text="----------------",
            font=self.small_text_font,
        ).pack(anchor=ctk.W, padx=20, pady=10)
        ctk.CTkLabel(
            self.mhelp_frame,
            text="WhatsApp- 0999926455",
            font=self.small_text_font,
        ).pack(anchor=ctk.W, padx=20, pady=10)
        # ----------------------- Med Help Dashboard -----------------------#

        # -------------------- Recetas Dashboard --------------------#
        self.scrollable_frame_mrec.bind(
            "<Configure>",
            lambda e: self.mrec_canvas.configure(
                scrollregion=self.mrec_canvas.bbox("all")
            ),
        )

        place_order_button = ctk.CTkButton(
            self.mrec_frame, text="Añadir receta nueva", command=self.new_receta
        )
        place_order_button.pack(padx=(0, 25), side="bottom", anchor=ctk.E)

        self.mrec_canvas.create_window(
            (0, 0), window=self.scrollable_frame_mrec, anchor=ctk.N
        )
        self.mrec_canvas.configure(yscrollcommand=self.scrollbarVertical_mrec.set)
        self.mrec_canvas.configure(xscrollcommand=self.scrollbarHorizontal_mrec.set)

        self.scrollbarVertical_mrec.pack(side="right", fill="y")
        self.scrollbarHorizontal_mrec.pack(side="bottom", fill="x")
        self.mrec_canvas.pack(side="left", fill="both", expand=True)

        self.display_mrec()
        # -------------------- Medical Records Dashboard --------------------#

        self.dashboard_frame.pack(
            fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
        )

    def show_dashboard(self) -> None:
        """Show the dashboard."""

        self.navigation_frame()
        self.title_frame("Silueta...")
        self.show_dashboard_frame()

        center_window(self.root, self.width, self.height)
        self.root.mainloop()

    def view_patient_info(self, patient_id: str) -> None:
        """Show information of a patient in a pop-up window."""
        # Create an instance of the Database class
        database = Database()
        patient_info = database.view_client_info(patient_id)
        patient_register = database.view_client_register(patient_id)

        if not patient_info:
            print(f"No se encontró información del paciente con ID: {patient_id}")
            return

        self.new_patient = ctk.CTkToplevel(self.root)
        self.new_patient.title("Información del Paciente")
        self.new_patient.resizable(False, False)
        self.new_patient.grab_set()

        center_window(self.new_patient, 1500, 800)

        # Mostrar la información del paciente utilizando CTkLabel
        ctk.CTkLabel(
            self.new_patient,
            text="Nombre",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.10, anchor=ctk.NW)

        entryName = ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__name,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryName.place(relx=0.2, rely=0.10,  anchor=ctk.NW) 

        ctk.CTkLabel(
            self.new_patient,
            text="Apellido",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.10, anchor=ctk.NW)

        entryApellido=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__apellido,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryApellido.place(relx=0.7, rely=0.1,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="ID",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.20, anchor=ctk.NW)

        entryID=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__ID,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryID.place(relx=0.2, rely=0.2,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="Teléfono",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.20, anchor=ctk.NW)

        entrytelefono=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__telefono,
            font=self.small_text_font,
            width=300, height=30,
        )
        entrytelefono.place(relx=0.7, rely=0.20,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="Email",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.30, anchor=ctk.NW)

        entryemail=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__email,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryemail.place(relx=0.2, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Estatura", font=self.small_text_font
        ).place(relx=0.5, rely=0.30, anchor=ctk.NW)

        entryestatura=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__estatura,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryestatura.place(relx=0.7, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Peso", font=self.small_text_font
        ).place(relx=0.1, rely=0.40, anchor=ctk.NW)

        entrypeso=ctk.CTkEntry(
            self.new_patient,
            font=self.small_text_font,
            width=300, height=30,
            textvariable=self.__peso,
        )
        entrypeso.place(relx=0.2, rely=0.40,  anchor=ctk.NW)
       
        ctk.CTkLabel(
            self.new_patient, text="Edad", font=self.small_text_font
        ).place(relx=0.5, rely=0.40, anchor=ctk.NW)

        entryedad=ctk.CTkEntry(
            self.new_patient,
            font=self.small_text_font,
            width=300, height=30,
            textvariable=self.__edad,
        )
        entryedad.place(relx=0.7, rely=0.40,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Género", font=self.small_text_font
        ).place(relx=0.1, rely=0.50, anchor=ctk.NW)
 
        entrygenero=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__genero,
            values=["Masculino","Femenino","Otro"],
        )
        entrygenero.place(relx=0.2,rely=0.50, anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Alergias", font=self.small_text_font
        ).place(relx=0.5, rely=0.50, anchor=ctk.NW)
 
        entryalergia=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__alergia,
            values=["Nueces", "Mariscos","Fresas","Gluten", "Lactosa", "Ninguna"],
        )
        entryalergia.place(relx=0.7,rely=0.50, anchor=ctk.NW)
        
        ctk.CTkLabel(
            self.new_patient, text="Actividad física", font=self.small_text_font
        ).place(relx=0.1, rely=0.60, anchor=ctk.NW)
 
        entryactividad=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__actividad,
            values=["1-3 veces por semana","4-5 veces por semana","6 o más veces por semana", "Nula"],
        )
        entryactividad.place(relx=0.2,rely=0.60, anchor=ctk.NW)
        
        ctk.CTkLabel(
            self.new_patient, text="¿Tiene exámenes recientes?", font=self.small_text_font
        ).place(relx=0.5, rely=0.60, anchor=ctk.NW)
 
        entryexamenes=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__examenes,
            values=["Sí", "No"],
        )
        entryexamenes.place(relx=0.7,rely=0.60, anchor=ctk.NW)

        entryName.delete(0, ctk.END) 
        entryName.insert(ctk.END, patient_info['Nombre'])
        entryApellido.delete(0, ctk.END) 
        entryApellido.insert(ctk.END, patient_info['Apellido'])
        entryID.delete(0, ctk.END) 
        entryID.insert(ctk.END, patient_info['ID'])
        entrytelefono.delete(0, ctk.END) 
        entrytelefono.insert(ctk.END, patient_info['Telefono'])
        entryemail.delete(0, ctk.END) 
        entryemail.insert(ctk.END, patient_info['email'])
        entryestatura.delete(0, ctk.END) 
        entryestatura.insert(ctk.END, patient_info['estatura'])
        entrypeso.delete(0, ctk.END) 
        entrypeso.insert(ctk.END, patient_info['Peso'])
        entryedad.delete(0, ctk.END) 
        entryedad.insert(ctk.END, patient_info['edad'])
        entrygenero.set(patient_info['Genero'])
        entryalergia.set(patient_info['Alergias'])
        entryactividad.set(patient_info['Actividad'])
        entryexamenes.set(patient_info['Examenes'])


        # Create a frame for the table
        table_frame = ctk.CTkFrame(self.new_patient)
        table_frame.place(relx=0.1, rely=0.7, anchor=ctk.NW)

        # Display the headers for the patient's register table
        headers = ["Fecha", "Peso", """%GC""", "%A", "Receta"]
        for pos, text in enumerate(headers):
            col_cell = ctk.CTkLabel(
                table_frame,
                text=text,
                font=self.text_font,
                width=200,
                height=50,
            )
            col_cell.grid(row=1, column=pos, pady=(10, 20), ipady=1, padx=20)

            #Imprime la fecha en que se ingresan los valores del paciente
            self.__fecharegistro=ctk.StringVar()
            fechaactual=datetime.now().date()
            entryfecharegistro=ctk.CTkEntry(
                self.new_patient,
                font=self.small_text_font,
                width=200, height=30,
                textvariable=self.__fecharegistro,
          )
            entryfecharegistro.place(relx=0.1, rely=0.765, anchor=ctk.NW)
            entryfecharegistro.delete(0, ctk.END) 
            entryfecharegistro.insert(ctk.END, fechaactual)
            #entryfecharegistro.grid(row=2, column=1, ipady=5, sticky=ctk.NW)

            #Ingresa el peso tomado en el control con el paciente
            self.__pesocontrol=ctk.IntVar()
            entrypesocontrol=ctk.CTkEntry(
            self.new_patient,
            font=self.small_text_font,
            width=200, height=30,
            textvariable=self.__pesocontrol,
        ).place(relx=0.26, rely=0.765,  anchor=ctk.NW)
            
            #Ingresa el porcentaje de grasa tomado en el control con el paciente
            self.__porcentajegrasacontrol=ctk.IntVar()
            entryporcentajegrasacontrol=ctk.CTkEntry(
            self.new_patient,
            font=self.small_text_font,
            width=200, height=30,
            textvariable=self.__porcentajegrasacontrol,
        ).place(relx=0.42, rely=0.765,  anchor=ctk.NW)
            
            #Ingresa el porcentaje de agua tomado en el control con el paciente
            self.__porcentajeaguacontrol=ctk.IntVar()
            entryporcentajeaguacontrol=ctk.CTkEntry(
            self.new_patient,
            font=self.small_text_font,
            width=200, height=30,
            textvariable=self.__porcentajeaguacontrol,
        ).place(relx=0.58, rely=0.765,  anchor=ctk.NW)
    
            #Agrega un botón para buscar la receta apropiada para el paciente
        Recipe_lookup_button = ctk.CTkButton(
            self.new_patient,
            text="Buscar receta",
            font=self.small_text_font,
            command="",
        ).place(relx=0.805, rely=0.783, anchor=ctk.CENTER)
    


            
        
        row = 3  # Start from row 3 to avoid overlapping with previous entries
        for i in patient_register:
            for j in range(1, 6):  # Assuming the data starts from index 1 in each entry
                entry = ctk.CTkEntry(
                    table_frame,
                    width=200,
                    font=self.small_text_font,
                )
                entry.grid(row=row, column=j-1, ipady=5, sticky=ctk.NW)

                try:
                    entry.insert(ctk.END, i[j].capitalize())
                except AttributeError:
                    entry.insert(ctk.END, i[j])

                entry.configure(state=ctk.DISABLED)

            row += 1

        
        # Agrega un botón para cerrar la ventana emergente
        close_button = ctk.CTkButton(
            self.new_patient,
            text="Cerrar",
            font=self.small_text_font,
            command=self.new_patient.destroy,
        )
        close_button.place(relx=0.55, rely=0.95, anchor=ctk.CENTER)

        # Agrega un botón para guardar datos
        close_button = ctk.CTkButton(
            self.new_patient,
            text="Guardar cambios",
            font=self.small_text_font,
            command=lambda: self.upload_patient_button_click(patient_id),
        )
        close_button.place(relx=0.45, rely=0.95, anchor=ctk.CENTER)

        # Set column weights for the table
        self.new_patient.grid_columnconfigure(0, weight=1)  # Make the first column take 100% width
        self.scrollable_frame.grid_columnconfigure(0, weight=1)  # Adjust the column weights for the table

        self.new_patient.lift()
        self.new_patient.focus_force()

    def imprimir_pdf(self, receta_sk):

        receta_info=self.db_object.get_receta(receta_sk)
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

        


    




    