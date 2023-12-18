import customtkinter as ctk 
import tkinter as tk
from ProgramaDeNutricion.centerwin import center_window
from datetime import datetime

class VentanaPaciente():
    def __init__(
            self,
        ) -> None:

      
        self.column_widths= [200, 200, 200, 125, 200, 60, 90]
        self.text_font = ctk.CTkFont(
            family="Rockwell", size=20, weight="normal"
        )
        self.small_text_font = ctk.CTkFont(
            family="Rockwell", size=18, weight="normal"
        )
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

    def Vista_Paciente(self,dashboard,db_object):

        #Creamos los frames necesarios
        self.pacientes_frame = ctk.CTkFrame(dashboard.root)
        self.pacientes_canvas = ctk.CTkCanvas(self.pacientes_frame)
        self.scrollable_frame = ctk.CTkFrame(self.pacientes_canvas)

        self.scrollbarVertical = ctk.CTkScrollbar(
            self.pacientes_frame,
            orientation=ctk.VERTICAL,
            command=self.pacientes_canvas.yview,
            width=30,
        )
        self.scrollbarHorizontal = ctk.CTkScrollbar(
            self.pacientes_frame,
            orientation=ctk.HORIZONTAL,
            command=self.pacientes_canvas.xview,
            width=30,
        )


        # ----------------------- Tabla de pacientes -----------------------#
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.pacientes_canvas.configure(
                scrollregion=self.pacientes_canvas.bbox("all")
            ),
        )

        place_order_button = ctk.CTkButton(
            self.pacientes_frame, text="Añadir paciente nuevo", command= lambda: self.view_patient_info(dashboard, db_object,"Nuevo")
        )
        place_order_button.pack(padx=(0, 25), side="bottom", anchor=ctk.E)

        self.pacientes_canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor=ctk.N
        )
        self.pacientes_canvas.configure(yscrollcommand=self.scrollbarVertical.set)
        self.pacientes_canvas.configure(xscrollcommand=self.scrollbarHorizontal.set)

        self.scrollbarVertical.pack(side="right", fill="y")
        self.scrollbarHorizontal.pack(side="bottom", fill="x")
        self.pacientes_canvas.pack(side="left", fill="both", expand=True)

        self.display_table(dashboard,db_object)
        return self.pacientes_frame

        # ----------------------- Medicines Dashboard -----------------------#

    def display_table(self,dashboard,db_object) -> None:

        self.dataset=db_object.get_patients()
        self.col_headers= db_object.get_col_headings("PatientTable")
        self.col_headers= db_object.get_col_headings("PatientTable")
        
        """Muestra la tabla de pacientes"""
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
                command=lambda client_id=i[0]: self.view_patient_info(dashboard, db_object,"Vista",client_id),
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

    def view_patient_info(self,dashboard, db_object,mode,patient_id=None):
        
        self.new_patient = ctk.CTkToplevel(dashboard.root)
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

        self.entryName = ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__name,
            font=self.small_text_font,
            width=300, height=30,
        )
        self.entryName.place(relx=0.2, rely=0.10,  anchor=ctk.NW) 

        ctk.CTkLabel(
            self.new_patient,
            text="Apellido",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.10, anchor=ctk.NW)

        self.entryApellido=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__apellido,
            font=self.small_text_font,
            width=300, height=30,
        )
        self.entryApellido.place(relx=0.7, rely=0.1,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="ID",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.20, anchor=ctk.NW)

        self.entryID=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__ID,
            font=self.small_text_font,
            width=300, height=30,
        )
        self.entryID.place(relx=0.2, rely=0.2,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="Teléfono",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.20, anchor=ctk.NW)

        self.entrytelefono=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__telefono,
            font=self.small_text_font,
            width=300, height=30,
        )
        self.entrytelefono.place(relx=0.7, rely=0.20,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="Email",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.30, anchor=ctk.NW)

        self.entryemail=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__email,
            font=self.small_text_font,
            width=300, height=30,
        )
        self.entryemail.place(relx=0.2, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Estatura", font=self.small_text_font
        ).place(relx=0.5, rely=0.30, anchor=ctk.NW)

        self.entryestatura=ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__estatura,
            font=self.small_text_font,
            width=300, height=30,
        )
        self.entryestatura.place(relx=0.7, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Peso", font=self.small_text_font
        ).place(relx=0.1, rely=0.40, anchor=ctk.NW)

        self.entrypeso=ctk.CTkEntry(
            self.new_patient,
            font=self.small_text_font,
            width=300, height=30,
            textvariable=self.__peso,
        )
        self.entrypeso.place(relx=0.2, rely=0.40,  anchor=ctk.NW)
       
        ctk.CTkLabel(
            self.new_patient, text="Edad", font=self.small_text_font
        ).place(relx=0.5, rely=0.40, anchor=ctk.NW)

        self.entryedad=ctk.CTkEntry(
            self.new_patient,
            font=self.small_text_font,
            width=300, height=30,
            textvariable=self.__edad,
        )
        self.entryedad.place(relx=0.7, rely=0.40,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Género", font=self.small_text_font
        ).place(relx=0.1, rely=0.50, anchor=ctk.NW)
 
        self.entrygenero=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__genero,
            values=["Masculino","Femenino","Otro"],
        )
        self.entrygenero.place(relx=0.2,rely=0.50, anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Alergias", font=self.small_text_font
        ).place(relx=0.5, rely=0.50, anchor=ctk.NW)
 
        self.entryalergia=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__alergia,
            values=["Nueces", "Mariscos","Fresas","Gluten", "Lactosa", "Ninguna"],
        )
        self.entryalergia.place(relx=0.7,rely=0.50, anchor=ctk.NW)
        
        ctk.CTkLabel(
            self.new_patient, text="Actividad física", font=self.small_text_font
        ).place(relx=0.1, rely=0.60, anchor=ctk.NW)
 
        self.entryactividad=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__actividad,
            values=["1-3 veces por semana","4-5 veces por semana","6 o más veces por semana", "Nula"],
        )
        self.entryactividad.place(relx=0.2,rely=0.60, anchor=ctk.NW)
        
        ctk.CTkLabel(
            self.new_patient, text="¿Tiene exámenes recientes?", font=self.small_text_font
        ).place(relx=0.5, rely=0.60, anchor=ctk.NW)
 
        self.entryexamenes=ctk.CTkComboBox(
            self.new_patient,
            width=300,
            height=15,
            variable=self.__examenes,
            values=["Sí", "No"],
        )
        self.entryexamenes.place(relx=0.7,rely=0.60, anchor=ctk.NW)

        self.Borrar_info()

        if mode=="Vista":

            """Show information of a patient in a pop-up window."""
            # Create an instance of the Database class
            patient_info = db_object.view_client_info(patient_id)
            patient_register = db_object.view_client_register(patient_id)
            
            if not patient_info:
                print(f"No se encontró información del paciente con ID: {patient_id}")
                return

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

            self.entryName.insert(ctk.END, patient_info['Nombre'])
            self.entryApellido.insert(ctk.END, patient_info['Apellido'])
            self.entryID.insert(ctk.END, patient_info['ID'])
            self.entrytelefono.insert(ctk.END, patient_info['Telefono'])
            self.entryemail.insert(ctk.END, patient_info['email'])
            self.entryestatura.insert(ctk.END, patient_info['estatura'])
            self.entrypeso.insert(ctk.END, patient_info['Peso'])
            self.entryedad.insert(ctk.END, patient_info['edad'])
            self.entrygenero.set(patient_info['Genero'])
            self.entryalergia.set(patient_info['Alergias'])
            self.entryactividad.set(patient_info['Actividad'])
            self.entryexamenes.set(patient_info['Examenes'])

            # Agrega un botón para guardar datos
            close_button = ctk.CTkButton(
                self.new_patient,
                text="Guardar cambios",
                font=self.small_text_font,
                command=lambda: self.guardar_cambios_paciente(db_object,patient_id),
            )
            close_button.place(relx=0.45, rely=0.95, anchor=ctk.CENTER)

        if mode=="Nuevo":
            # Create a button to add the patient
            ctk.CTkButton(
                self.new_patient,
                text="Añadir paciente",
                font=self.small_text_font,
                command=self.anadir_paciente_boton,
            ).place(relx=0.45, rely=0.95,  anchor=ctk.CENTER)

        # Agrega un botón para cerrar la ventana emergente
        close_button = ctk.CTkButton(
            self.new_patient,
            text="Cerrar",
            font=self.small_text_font,
            command=self.new_patient.destroy,
        )
        close_button.place(relx=0.60, rely=0.95, anchor=ctk.CENTER)

        # Set column weights for the table
        self.new_patient.grid_columnconfigure(0, weight=1)  # Make the first column take 100% width
        self.scrollable_frame.grid_columnconfigure(0, weight=1)  # Adjust the column weights for the table

        self.new_patient.lift()
        self.new_patient.focus_force()
    
    def anadir_paciente_boton(self,db_object):
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

        # Call the add_patient method with the retrieved data
        success = db_object.add_patient((nombre, apellido,ID, telefono, email, estatura, peso, edad, genero, alergias, actividad, examenes))

        if success:
            print("Patient added successfully")
        else:
            print("Failed to add patient")

    def guardar_cambios_paciente(self, db_object ,SK):
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

        # Call the add_patient method with the retrieved data
        success = db_object.upload_patient((nombre, apellido,ID, telefono, email, estatura, peso, edad, genero, alergias, actividad, examenes),SK)

        if success:
            print("Patient uploaded successfully")
        else:
            print("Failed to upload patient")

    def Borrar_info(self):
        self.entryName.delete(0, ctk.END) 
        self.entryApellido.delete(0, ctk.END) 
        self.entryID.delete(0, ctk.END) 
        self.entrytelefono.delete(0, ctk.END) 
        self.entryemail.delete(0, ctk.END) 
        self.entryestatura.delete(0, ctk.END) 
        self.entrypeso.delete(0, ctk.END) 
        self.entryedad.delete(0, ctk.END) 
        self.entrygenero.set('')
        self.entryalergia.set('')
        self.entryactividad.set('')
        self.entryexamenes.set('')



        
