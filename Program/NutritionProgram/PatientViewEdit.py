import customtkinter as ctk

class PatientViewEdit(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.entry_widgets = {}
        self.frame=ctk.CTkFrame(self.parent)
        self.parent.__name = ctk.StringVar()
        self.parent.__apellido = ctk.StringVar()
        self.parent.__email = ctk.StringVar()
        self.parent.__edad = ctk.IntVar()
        self.parent.__estatura = ctk.IntVar()
        self.parent.__ID = ctk.StringVar()
        self.parent.__telefono=ctk.StringVar()
        self.parent.__peso=ctk.IntVar()
        self.parent.__genero=ctk.StringVar()
        self.parent.__alergia=ctk.StringVar()
        self.parent.__examenes=ctk.StringVar()
        self.parent.__actividad=ctk.StringVar()
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
        
        # self.create_widgets(values)


    def create_widgets(self,values={}):

        ctk.CTkLabel(
            self.parent,
            text="Nombre",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.10, anchor=ctk.NW)

        entryName = ctk.CTkEntry(
            self.parent,
            textvariable=self.parent.__name,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryName.place(relx=0.2, rely=0.10,  anchor=ctk.NW) 
        self.entry_widgets['Nombre'] = entryName

        ctk.CTkLabel(
            self.parent,
            text="Apellido",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.10, anchor=ctk.NW)

        entryApellido=ctk.CTkEntry(
            self.parent,
            textvariable=self.parent.__apellido,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryApellido.place(relx=0.7, rely=0.1,  anchor=ctk.NW)
        self.entry_widgets['Apellido'] = entryApellido

        ctk.CTkLabel(
            self.parent,
            text="ID",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.20, anchor=ctk.NW)

        entryID=ctk.CTkEntry(
            self.parent,
            textvariable=self.parent.__ID,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryID.place(relx=0.2, rely=0.2,  anchor=ctk.NW)
        self.entry_widgets['ID'] = entryID

        ctk.CTkLabel(
            self.parent,
            text="Teléfono",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.20, anchor=ctk.NW)

        entrytelefono=ctk.CTkEntry(
            self.parent,
            textvariable=self.parent.__telefono,
            font=self.small_text_font,
            width=300, height=30,
        )
        entrytelefono.place(relx=0.7, rely=0.20,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent,
            text="Email",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.30, anchor=ctk.NW)

        entryemail=ctk.CTkEntry(
            self.parent,
            textvariable=self.parent.__email,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryemail.place(relx=0.2, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent, text="Estatura", font=self.small_text_font
        ).place(relx=0.5, rely=0.30, anchor=ctk.NW)

        entryestatura=ctk.CTkEntry(
            self.parent,
            textvariable=self.parent.__estatura,
            font=self.small_text_font,
            width=300, height=30,
        )
        entryestatura.place(relx=0.7, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent, text="Peso", font=self.small_text_font
        ).place(relx=0.1, rely=0.40, anchor=ctk.NW)

        entrypeso=ctk.CTkEntry(
            self.parent,
            font=self.small_text_font,
            width=300, height=30,
            textvariable=self.parent.__peso,
        )
        entrypeso.place(relx=0.2, rely=0.40,  anchor=ctk.NW)
       
        ctk.CTkLabel(
            self.parent, text="Edad", font=self.small_text_font
        ).place(relx=0.5, rely=0.40, anchor=ctk.NW)

        entryedad=ctk.CTkEntry(
            self.parent,
            font=self.small_text_font,
            width=300, height=30,
            textvariable=self.parent.__edad,
        )
        entryedad.place(relx=0.7, rely=0.40,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent, text="Género", font=self.small_text_font
        ).place(relx=0.1, rely=0.50, anchor=ctk.NW)
 
        entrygenero=ctk.CTkComboBox(
        self.parent,
        width=300,
        height=15,
        variable=self.parent.__genero,
        values=["Masculino","Femenino","Otro"],
        )
        entrygenero.place(relx=0.2,rely=0.50, anchor=ctk.NW)

        ctk.CTkLabel(
            self.parent, text="Alergias", font=self.small_text_font
        ).place(relx=0.5, rely=0.50, anchor=ctk.NW)
 
        entryalergia=ctk.CTkComboBox(
        self.parent,
        width=300,
        height=15,
        variable=self.parent.__alergia,
        values=["Nueces", "Mariscos","Fresas","Gluten", "Lactosa", "Ninguna"],
        )
        entryalergia.place(relx=0.7,rely=0.50, anchor=ctk.NW)
        
        ctk.CTkLabel(
            self.parent, text="Actividad física", font=self.small_text_font
        ).place(relx=0.1, rely=0.60, anchor=ctk.NW)
 
        entryactividad=ctk.CTkComboBox(
        self.parent,
        width=300,
        height=15,
        variable=self.parent.__actividad,
        values=["1-3 veces por semana","4-5 veces por semana","6 o más veces por semana", "Nula"],
        )
        entryactividad.place(relx=0.2,rely=0.60, anchor=ctk.NW)
        
        ctk.CTkLabel(
            self.parent, text="¿Tiene exámenes recientes?", font=self.small_text_font
        ).place(relx=0.5, rely=0.60, anchor=ctk.NW)
 
        entryexamenes=ctk.CTkComboBox(
        self.parent,
        width=300,
        height=15,
        variable=self.parent.__examenes,
        values=["Sí", "No"],
        )
        entryexamenes.place(relx=0.7,rely=0.60, anchor=ctk.NW)

        if not values:
            return
        else:
        entryName.insert(ctk.END, values.get('Nombre', ''))
        entryApellido.insert(ctk.END, values['Apellido'])
        entryID.insert(ctk.END, values['ID'])
        entrytelefono.insert(ctk.END, values['Telefono'])
        entryemail.insert(ctk.END, values['email'])
        entryestatura.insert(ctk.END, values['estatura'])
        entrypeso.insert(ctk.END, values['Peso'])
        entryedad.insert(ctk.END, values['edad'])
        entrygenero.set(values['Genero'])
        entryalergia.set(values['Alergias'])
        entryactividad.set(values['Actividad'])
        entryexamenes.set(values['Examenes'])

        self.frame = ctk.CTkFrame(self.parent)
