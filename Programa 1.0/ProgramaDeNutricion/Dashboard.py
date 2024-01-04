import customtkinter as ctk 
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import platform
from tkinter import filedialog,messagebox, simpledialog
from datetime import datetime
from ProgramaDeNutricion.centerwin import center_window
from ProgramaDeNutricion.BaseDatos import BaseDeDatos
from ProgramaDeNutricion.VentanaUsuario import VentanaUsuario
from ProgramaDeNutricion.VentanaPaciente import VentanaPaciente
from ProgramaDeNutricion.VentanaRecetas import VentanaRecetas

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
        self.db_object = BaseDeDatos("Dashboard")
        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme("assets/SiluetaPalette.json")

        self.root = ctk.CTk()
        self.root.title("Nutrition Plan Assistant 1.0")


        self.title_logo = ctk.CTkImage(
            Image.open("assets/images/Silueta.png"), size=(250, 100)
        )

        # ------------------------ Fonts ------------------------#
        self.op_font = ctk.CTkFont(
            family="Rockwell", size=30, weight="bold", underline=True
        )
        self.title_font = ctk.CTkFont(
            family="Rockwell", size=35, weight="bold"
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
            family="Rockwell", size=15, weight="bold"
        )
        # ------------------------ Frames ------------------------#
        self.dashboard_frame = VentanaUsuario.Vista_Usuario(self,self.db_object)
        self.ventana_paciente=VentanaPaciente().Vista_Paciente(self,self.db_object)
        self.ventana_recetas=VentanaRecetas().mostrar_tabla_recetas(self,self.db_object)

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
        tagline_label.place(relx=0.45, rely=0.4, anchor=ctk.CENTER, y=20)
        title_logo_label.pack(side=ctk.RIGHT, padx=(0, 20))

        title_frame.pack(side=ctk.TOP, fill=ctk.X, padx=(0, 20), pady=20)

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

        pacientes_button = ctk.CTkButton(
            navigation_frame,
            text=" Crear paciente ",
            font=self.text_font_bold,
            command=lambda: self.reset_frame("Paciente"),
            corner_radius=10,
            height=40,
        )

        recetas_button = ctk.CTkButton(
            navigation_frame,
            text=" Planes diarios ",
            font=self.text_font_bold,
            command=lambda: self.reset_frame("Recetas"),
            corner_radius=10,
            height=40,
        )

        ##Dejo el espacio por si quieren poner otro botón
        # mhelp_button = ctk.CTkButton(
        #     navigation_frame,
        #     text=" Silueta ",
        #     font=self.text_font_bold,
        #     command=lambda: self.reset_frame("Información"),
        #     corner_radius=10,
        #     height=40,
        # )


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
        pacientes_button.pack(pady=15)
        recetas_button.pack(pady=15)

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

        if frame_name == "Paciente":
            
            self.ventana_paciente.pack(
                fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
            )
        else:
            self.ventana_paciente.pack_forget()

        # if frame_name == "mhelp":
        #     self.mhelp_frame.pack(
        #         fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
        #     )
        # else:
        #     self.mhelp_frame.pack_forget()

        if frame_name == "Recetas":
            self.ventana_recetas.pack(
                fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
            )
        else:
            self.ventana_recetas.pack_forget()

        print("Frame reset to", frame_name)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Change the appearance mode.

        Args:
            new_appearance_mode (str): The new appearance mode.
        """

        ctk.set_appearance_mode(new_appearance_mode)
        print("Appearance mode changed to", new_appearance_mode, "mode")

    def show_dashboard(self) -> None:
        """Show the dashboard."""

        self.navigation_frame()
        self.title_frame("Silueta")
        # self.show_dashboard_frame()

        center_window(self.root, self.width, self.height)
        self.root.mainloop()
 
