import customtkinter as ctk

class PatientViewInfo(ctk.CTkFrame):
    def __init__(self, parent):
        self.parent = parent
        self.frame=ctk.CTkFrame(self.parent)
        # ------------------------ Fonts ------------------------#
        self.op_font = ctk.CTkFont(
            family="Franklin Gothic", size=30, weight="bold", underline=True
        )
        self.title_font = ctk.CTkFont(
            family="Rockwell", size=60, weight="bold"
        )
        self.text_font = ctk.CTkFont(
            family="Rockwell", size=20, weight="normal"
        )
        self.text_font_bold = ctk.CTkFont(
            family="Rockwell", size=20, weight="bold"
        )
        self.small_text_font = ctk.CTkFont(
            family="Arial", size=18, weight="normal"
        )
        self.tagline_font = ctk.CTkFont(
            family="Rockwell", size=30, weight="normal"
        )
        # ------------------------ Frames ------------------------#

        self.labels = [
            ("Nombre", "name"),
            ("Apellido", "apellido"),
            ("ID", "ID"),
            ("Teléfono", "telefono"),
            ("Email", "email"),
            ("Estatura", "estatura"),
            ("Peso", "peso"),
            ("Edad", "edad"),
            ("Género", "genero"),
            ("Alergias", "alergia"),
            ("Actividad física", "actividad"),
            ("¿Tiene exámenes recientes?", "examenes"),
        ]

        # self.create_widgets(patient_info)

    def create_widgets(self,patient_info={}):

        # Mostrar la información del paciente utilizando CTkLabel
        ctk.CTkLabel(
            self.parent,
            text="Nombre",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.10, anchor=ctk.NW)
        
        ctk.CTkLabel(
            self.parent,
            text=patient_info.get('Nombre', ''),
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.2, rely=0.10,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            text="Apellido",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.10, anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            text=patient_info.get('Apellido', ''),
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.6, rely=0.1,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            text="ID",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.20, anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            text=patient_info.get('ID', ''),
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.2, rely=0.2,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            text="Teléfono",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.20, anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            text=patient_info.get('Telefono', ''),
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.6, rely=0.20,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            text="Email",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.30, anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            text=patient_info.get('email', ''),
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.2, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent, text="Estatura", font=self.small_text_font
        ).place(relx=0.5, rely=0.30, anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            text=patient_info.get('estatura', ''),
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.6, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent, text="Edad", font=self.small_text_font
        ).place(relx=0.5, rely=0.40, anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            font=self.small_text_font,
            width=300, height=30,
            text=patient_info.get('edad', ''),
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.6, rely=0.40,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent, text="Peso", font=self.small_text_font
        ).place(relx=0.1, rely=0.40, anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            font=self.small_text_font,
            width=300, height=30,
            text=patient_info.get('Peso', ''),
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.2, rely=0.40,  anchor=ctk.NW)


        ctk.CTkLabel(
            self.parent, text="Género", font=self.small_text_font
        ).place(relx=0.1, rely=0.50, anchor=ctk.NW)
 
        ctk.CTkLabel(
            self.parent,
            font=self.small_text_font,
            width=300, height=30,
            text=patient_info.get('Genero', ''),
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.2,rely=0.50, anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent, text="Alergias", font=self.small_text_font
        ).place(relx=0.5, rely=0.50, anchor=ctk.NW)
 
        ctk.CTkLabel(
            self.parent,
            font=self.small_text_font,
            width=300, height=30,
            text=patient_info.get('Alergias', ''),
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.6,rely=0.50, anchor=ctk.NW)
        
        ctk.CTkLabel(
            self.parent, text="Actividad física", font=self.small_text_font
        ).place(relx=0.1, rely=0.60, anchor=ctk.NW)
 
        ctk.CTkLabel(
            self.parent,
            font=self.small_text_font,
            width=300, height=30,
            text=patient_info.get('Actividad', ''),
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.2,rely=0.60, anchor=ctk.NW)
        
        ctk.CTkLabel(
            self.parent, text="¿Tiene exámenes recientes?", font=self.small_text_font
        ).place(relx=0.5, rely=0.60, anchor=ctk.NW)
 
        ctk.CTkLabel(
            self.parent,
            font=self.small_text_font,
            width=300, height=30,
            text=patient_info.get('Examenes', ''),
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.6,rely=0.60, anchor=ctk.NW)

        self.frame = ctk.CTkFrame(self.parent)
