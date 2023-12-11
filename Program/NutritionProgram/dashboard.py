import customtkinter as ctk
from PIL import Image

from NutritionProgram.centerwin import center_window
from NutritionProgram.database import Database


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
        theme_color: str = "green",
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

        self.dataset = self.db_object.get_patients()
        self.col_headers = self.db_object.get_col_headings("PatientTable")

        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(theme_color)

        self.root = ctk.CTk()
        self.root.title("#### nutricionista")
        # self.root.resizable(False, False)

        self.title_logo = ctk.CTkImage(
            Image.open("assets/images/turtle.jpeg"), size=(125, 100)
        )

        self.order_list = []
        self.column_widths = [200, 200, 200, 125, 200, 60, 90]
        self.column_widths_register = [200, 200, 200, 200, 200, 200, 200]

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

        self.dashboard_frame = ctk.CTkFrame(self.root)
        self.mrec_frame = ctk.CTkFrame(self.root)
        self.mhelp_frame = ctk.CTkFrame(self.root)
        # self.new_patient = ctk.CTkFrame(self.root)
        self.__name = ctk.StringVar()
        self.__apellido = ctk.StringVar()
        self.__email = ctk.StringVar()
        self.__edad = ctk.StringVar()
        self.__estatura = ctk.StringVar()
        self.__ID = ctk.StringVar()
        self.__Telefono=ctk.StringVar()
        self.__peso=ctk.StringVar()

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
            title_frame, text="- Nacho Turtle", font=self.tagline_font
        )

        title_logo_label = ctk.CTkLabel(
            title_frame, image=self.title_logo, text=""
        )

        title_label.pack(side=ctk.LEFT, padx=(20, 0))
        tagline_label.pack(side=ctk.LEFT, padx=(0, 20))
        title_logo_label.pack(side=ctk.RIGHT, padx=(0, 20), pady=5)

        title_frame.pack(side=ctk.TOP, fill=ctk.X, padx=(0, 20), pady=20)

    def navigation_frame(self) -> None:
        """Create the navigation frame."""

        navigation_frame = ctk.CTkFrame(
            self.root, width=250, height=self.height, corner_radius=15
        )

        navigation_title = ctk.CTkLabel(
            navigation_frame, text="Panel de navegación", font=self.op_font
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
            text=" Buscar paciente ",
            font=self.text_font_bold,
            command=lambda: self.reset_frame("mhelp"),
            corner_radius=10,
            height=40,
        )

        mrecord_button = ctk.CTkButton(
            navigation_frame,
            text=" Planes nutricionales ",
            font=self.text_font_bold,
            command=lambda: self.reset_frame("mrecord"),
            corner_radius=10,
            height=40,
        )

        light_mode = ctk.CTkButton(
            navigation_frame,
            text=" Light Mode ",
            font=self.text_font_bold,
            height=30,
            command=lambda: self.change_appearance_mode_event("Light"),
        )

        dark_mode = ctk.CTkButton(
            navigation_frame,
            text=" Dark Mode ",
            font=self.text_font_bold,
            height=30,
            command=lambda: self.change_appearance_mode_event("Dark"),
        )

        quit_button = ctk.CTkButton(
            navigation_frame,
            text=" Quit ",
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
            self.display_mrec()
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

        ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__name,
            font=self.small_text_font,
            width=300, height=30,
        ).place(relx=0.2, rely=0.10,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="Apellido",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.10, anchor=ctk.NW)

        ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__apellido,
            font=self.small_text_font,
            width=300, height=30,
        ).place(relx=0.6, rely=0.1,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="ID",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.2, anchor=ctk.NW)

        ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__ID,
            font=self.small_text_font,
            width=300, height=30,
        ).place(relx=0.2, rely=0.2,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="Teléfono",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.20, anchor=ctk.NW)

        ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__Telefono,
            font=self.small_text_font,
            width=300, height=30,
        ).place(relx=0.6, rely=0.20,  anchor=ctk.NW)


        ctk.CTkLabel(
            self.new_patient,
            text="Correo electrónico",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.3, anchor=ctk.NW)

        ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__email,
            font=self.small_text_font,
            width=300, height=30,
        ).place(relx=0.2, rely=0.3,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Estatura", font=self.small_text_font
        ).place(relx=0.5, rely=0.3, anchor=ctk.NW)

        ctk.CTkEntry(
            self.new_patient,
            textvariable=self.__estatura,
            font=self.small_text_font,
            width=300, height=30,
        ).place(relx=0.6, rely=0.3,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Edad", font=self.small_text_font
        ).place(relx=0.5, rely=0.4, anchor=ctk.NW)

        ctk.CTkEntry(
            self.new_patient,
            font=self.small_text_font,
            width=300, height=30,
            textvariable=self.__edad,
        ).place(relx=0.6, rely=0.4,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Peso", font=self.small_text_font
        ).place(relx=0.1, rely=0.40, anchor=ctk.NW)

        ctk.CTkEntry(
            self.new_patient,
            font=self.small_text_font,
            width=300, height=30,
            textvariable=self.__peso,
        ).place(relx=0.2, rely=0.40,  anchor=ctk.NW)

        # Create a button to add the patient
        ctk.CTkButton(
            self.new_patient,
            text="Añadir paciente",
            font=self.small_text_font,
            command=self.add_patient_button_click,
        ).place(relx=0.4, rely=0.9,  anchor=ctk.CENTER)
        self.new_patient.lift()
        self.new_patient.focus_force

         # Agrega un botón para cerrar la ventana emergente

        close_button = ctk.CTkButton(
            self.new_patient,
            text="Cerrar",
            font=self.small_text_font,
            command=self.new_patient.destroy,
        )
        close_button.place(relx=0.6, rely=0.9, anchor=ctk.CENTER)

    def add_patient_button_click(self):
        # Retrieve the data from the entry widgets
        nombre = self.__name.get()
        apellido = self.__apellido.get()
        id = self.__ID.get()
        email = self.__email.get()
        estatura = self.__estatura.get()
        edad = self.__edad.get()

        # Create an instance of the Database class
        database = Database()

        # Call the add_patient method with the retrieved data
        success = database.add_patient((nombre, apellido, id, email, estatura, edad))

        if success:
            print("Patient added successfully")
        else:
            print("Failed to add patient")

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
                row=1, column=(pos), pady=(10, 20), ipady=1, padx=6
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
                    entry.insert(ctk.END, i[j])

                entry.configure(state=ctk.DISABLED)

            row += 1

    def display_mrec(self) -> None:
        """Display the medicine records of the user."""

        mrec = self.db_object.get_medicine_record(self.user_id)

        if mrec == []:
            ctk.CTkLabel(
                self.mrec_frame,
                text="No records found",
                font=self.text_font,
            ).grid(row=1, column=0, padx=20, pady=20, sticky=ctk.NSEW)
        else:
            mrec_col_headers = [
                "Mid",
                "Name",
                "Treatment",
                "Price",
                "Time of Purchase",
            ]

            mrec_col_widths = [80, 150, 450, 80, 220]

            for i in range(0, len(mrec_col_headers)):
                col_cell = ctk.CTkEntry(
                    self.mrec_frame,
                    width=mrec_col_widths[i],
                    font=self.text_font,
                )
                col_cell.insert(ctk.END, mrec_col_headers[i].capitalize())
                col_cell.configure(state=ctk.DISABLED)
                col_cell.grid(row=1, column=i, pady=(10, 20), ipady=1, padx=5)

            for i in range(0, len(mrec)):
                m_row = self.db_object.get_medicine_details(mrec[i][1])
                for j in range(0, len(m_row) - 1):
                    entry = ctk.CTkEntry(
                        self.mrec_frame,
                        width=self.column_widths[j],
                        font=self.small_text_font,
                    )
                    try:
                        entry.insert(ctk.END, m_row[j].capitalize())
                    except AttributeError:
                        entry.insert(ctk.END, m_row[j])
                    entry.configure(state=ctk.DISABLED)
                    entry.grid(row=(i + 2), column=j, padx=5)

            for i in range(len(mrec)):
                e = ctk.CTkEntry(
                    self.mrec_frame,
                    width=mrec_col_widths[4],
                    font=self.small_text_font,
                )
                e.insert(ctk.END, mrec[i][2])
                e.configure(state=ctk.DISABLED)
                e.grid(row=(i + 2), column=4, padx=5)

        self.mrec_frame.pack(
            fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
        )

    def show_dashboard_frame(self) -> None:
        """Display the user dashboard."""

        # ------------------------ User Dashboard ------------------------#
        self.dashboard_frame = ctk.CTkFrame(self.root)

        ctk.CTkLabel(
            self.dashboard_frame,
            text="########: Centro nutricionista",
            font=self.op_font,
        ).pack(padx=20, pady=20)
        ctk.CTkLabel(
            self.dashboard_frame,
            text="""Hola!. Bienvenido a #####: Tu compañero nutricionista.""",
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
            text="About Asclepius",
            font=self.op_font,
            anchor=ctk.CENTER,
        ).pack(padx=(20, 20), pady=20)
        ctk.CTkLabel(
            self.mhelp_frame,
            text=wellness_description,
            font=self.small_text_font,
        ).pack(anchor=ctk.CENTER, padx=20)
        ctk.CTkLabel(
            self.mhelp_frame, text="Contact Us", font=self.op_font
        ).pack(anchor=ctk.W, padx=20, pady=20)
        ctk.CTkLabel(
            self.mhelp_frame,
            text="For general queries- 0120-7199300",
            font=self.small_text_font,
        ).pack(anchor=ctk.W, padx=20, pady=10)
        ctk.CTkLabel(
            self.mhelp_frame,
            text="WhatsApp- +91 8860309257",
            font=self.small_text_font,
        ).pack(anchor=ctk.W, padx=20, pady=10)
        # ----------------------- Med Help Dashboard -----------------------#

        # -------------------- Medical Records Dashboard --------------------#
        self.mrec_frame = ctk.CTkFrame(self.root)
        ctk.CTkLabel(
            self.mrec_frame, text="Medical Records", font=self.op_font
        ).grid(row=0, column=0, padx=20, pady=20, columnspan=7)
        # -------------------- Medical Records Dashboard --------------------#

        self.dashboard_frame.pack(
            fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
        )

    def show_dashboard(self) -> None:
        """Show the dashboard."""

        self.navigation_frame()
        self.title_frame("Lion")
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
        
        ctk.CTkLabel(
            self.new_patient,
            text=patient_info['Nombre'],
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.2, rely=0.10,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="Apellido",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.10, anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text=patient_info['Apellido'],
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.6, rely=0.1,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="ID",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.20, anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text=patient_info['ID'],
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.2, rely=0.2,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="Teléfono",
            font=self.small_text_font,
        ).place(relx=0.5, rely=0.20, anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text=patient_info['Telefono'],
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.6, rely=0.20,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text="Email",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.30, anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text=patient_info['email'],
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.2, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Estatura", font=self.small_text_font
        ).place(relx=0.5, rely=0.30, anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            text=patient_info['estatura'],
            font=self.small_text_font,
            width=300, height=30,
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.6, rely=0.30,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Edad", font=self.small_text_font
        ).place(relx=0.5, rely=0.40, anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            font=self.small_text_font,
            width=300, height=30,
            text=patient_info['edad'],
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.6, rely=0.40,  anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient, text="Peso", font=self.small_text_font
        ).place(relx=0.1, rely=0.40, anchor=ctk.NW)

        ctk.CTkLabel(
            self.new_patient,
            font=self.small_text_font,
            width=300, height=30,
            text=patient_info['Peso'],
            bg_color="gray",
            corner_radius=180,
        ).place(relx=0.2, rely=0.40,  anchor=ctk.NW)

        # Create a frame for the table
        table_frame = ctk.CTkFrame(self.new_patient)
        table_frame.place(relx=0.1, rely=0.5, anchor=ctk.NW)

        # Display the headers for the patient's register table
        headers = ["Fecha", "Peso", "PGC", "PA", "D"]
        for pos, text in enumerate(headers):
            col_cell = ctk.CTkLabel(
                table_frame,
                text=text.capitalize(),
                font=self.text_font,
                width=200,
                height=50,
            )
            col_cell.grid(row=1, column=pos, pady=(10, 20), ipady=1, padx=20)

        row = 2  # Start from row 2 to avoid overlapping with previous entries
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
        close_button.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

        # Set column weights for the table
        self.new_patient.grid_columnconfigure(0, weight=1)  # Make the first column take 100% width
        self.scrollable_frame.grid_columnconfigure(0, weight=1)  # Adjust the column weights for the table

        self.new_patient.lift()
        self.new_patient.focus_force()