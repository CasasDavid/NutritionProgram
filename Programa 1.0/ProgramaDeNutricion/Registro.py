import re

import customtkinter as ctk
from PIL import Image

from ProgramaDeNutricion.BaseDatos import BaseDeDatos


class Signup:
    """Class to create the signup screen."""

    def __init__(
        self,
        root,
        width=500,
        height=500,
        appearance_mode="light",
        color_theme="green",
    ) -> None:
        """Constructor for the Signup class.

        Args:
            root (ctk window/frame): where the widgets will be placed.
            width (int, optional): width of the window. Defaults to 500.
            height (int, optional): height of the window. Defaults to 500.
        """
        ctk.set_appearance_mode(appearance_mode)
        ctk.set_default_color_theme("assets/SiluetaPaletteInit.json")

        self.signup_frame = ctk.CTkFrame(root, width=width, height=height)
        self.signup_completed = False

        self.width = width
        self.height = height

        self.__enrollid = ctk.StringVar()
        self.__userName = ctk.StringVar()
        self.__name = ctk.StringVar()
        self.__apellido = ctk.StringVar()
        self.__email = ctk.StringVar()
        self.__password = ctk.StringVar()

        self.text_font = ctk.CTkFont(family="Rockwell", size=20, weight="bold")
        self.small_text_font = ctk.CTkFont(
            family="Rockwell", size=14, weight="normal"
        )

        self.database = BaseDeDatos("Signup Screen")

    def widgets(self):
        """Function to create widgets for the login screen.

        Args:
            app (ctk.Ctk()): The root window.
        """
        self.title = ctk.CTkLabel(
            self.signup_frame, text="SignUp to #########", font=self.text_font
        ).place(relx=0.5, rely=0.05, anchor=ctk.CENTER)

        ctk.CTkLabel(
            self.signup_frame,
            text="UserName",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.10, anchor=ctk.NW)

        ctk.CTkEntry(
            self.signup_frame,
            textvariable=self.__userName,
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.15, width=300, height=30, anchor=ctk.NW)

        ctk.CTkLabel(
            self.signup_frame,
            text="Name",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.25, anchor=ctk.NW)

        ctk.CTkEntry(
            self.signup_frame,
            textvariable=self.__name,
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.30, width=300, height=30, anchor=ctk.NW)

        ctk.CTkLabel(
            self.signup_frame,
            text="Apellido",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.40, anchor=ctk.NW)

        ctk.CTkEntry(
            self.signup_frame,
            textvariable=self.__apellido,
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.45, width=300, height=30, anchor=ctk.NW)

        ctk.CTkLabel(
            self.signup_frame,
            text="Email*",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.55, anchor=ctk.NW)

        ctk.CTkEntry(
            self.signup_frame,
            textvariable=self.__email,
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.60, width=300, height=30, anchor=ctk.NW)

        ctk.CTkLabel(
            self.signup_frame, text="Password*", font=self.small_text_font
        ).place(relx=0.1, rely=0.70, anchor=ctk.NW)
        ctk.CTkEntry(
            self.signup_frame,
            show="*",
            font=self.small_text_font,
            textvariable=self.__password,
        ).place(relx=0.1, rely=0.75, width=300, height=30, anchor=ctk.NW)

        self.register = ctk.CTkButton(
            self.signup_frame,
            text="Register",
            font=self.text_font,
            command=self.submit,
            corner_radius=10,
        ).place(relx=0.5, rely=0.90, width=150, height=40, anchor=ctk.CENTER)

    def enableEntry(self):
        self.room_entry.configure(state="normal", fg_color="white")
        self.room_entry.focus()
        self.room_entry.update()

    def disableEntry(self):
        self.room_entry.configure(state="disabled")
        self.room_entry.configure(fg_color="lightgrey")
        self.room_entry.update()

    def submit(self):
        """Function to check meet the requirements and submit the data to the database."""

        if (
            (self.__name.get() == "")
            or (self.__email.get() == "")
            or (self.__password.get() == "")
            or (self.__apellido.get() == "")
            or (self.__userName.get() == "")
        ):
            print(self.__enrollid.get())
            ctk.CTkLabel(
                self.signup_frame,
                text="Please fill all the fields",
                font=self.small_text_font,
            ).place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

        elif not re.match(
            r"^(?=.*[A-Z])", self.__userName.get()
        ):
            ctk.CTkLabel(
                self.signup_frame,
                text="Please enter a valid userName ID!",
                corner_radius=10,
                font=self.small_text_font,
            ).place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

        elif not self.database.signup(self.get_credentials()):
            ctk.CTkLabel(
                self.signup_frame,
                text="User already exists",
                font=self.small_text_font,
            ).place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

        else:
            self.signup_frame.after(1000, self.signin_delay)

            ctk.set_appearance_mode("dark")

            for widget in self.signup_frame.winfo_children():
                widget.destroy()

            ctk.CTkLabel(
                self.signup_frame, text="Signing In...", font=self.text_font
            ).pack(pady=40, padx=50, fill=ctk.BOTH, expand=True)

    def signin_delay(self):
        """Loading screen for 1 second before redirecting to the dashboard page."""
        self.signup_completed = True

    def get_credentials(self) -> tuple:
        """Returns the signup information"""

        return (
            self.__userName.get(),
            self.__name.get(),
            self.__apellido.get(),
            self.__password.get(),
            self.__email.get(),
        )

    def return_signup_frame(self) -> ctk.CTkFrame:
        """Show the signupwindow"""
        self.widgets()

        return self.signup_frame