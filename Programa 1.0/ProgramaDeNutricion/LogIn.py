import re

import customtkinter as ctk
from PIL import Image

from ProgramaDeNutricion.BaseDatos import BaseDeDatos


class Login:
    """Class to handle the login screen."""

    def __init__(
        self,
        appearance_mode: str = "dark",
        color_theme: str = "green",
        width: int = 500,
        height: int = 500,
        root=None,
    ) -> None:
        """Initialize the login screen.

        Args:
            appearance_mode (str, optional): Determines appearance. Defaults to "light".
            color_theme (str, optional): Determines accent color. Defaults to "green".
            width (int, optional): Sets width of the window. Defaults to 500.
            height (int, optional): Sets height of the window. Defaults to 500.
            root (_type_, optional): Tkinter window where the widgets need to be placed. Defaults to None.
        """

        self.width = width
        self.height = height

        ctk.set_appearance_mode(appearance_mode)
        ctk.set_default_color_theme("assets/SiluetaPaletteInit.json")
        self.login_frame = ctk.CTkFrame(
            root, width=self.width, height=self.height
        )

        self.__userName = ctk.StringVar()
        self.__password = ctk.StringVar()

        self.login_completed = False

        self.db = BaseDeDatos("Login Screen")
        self.title_font = ctk.CTkFont(
            family="Rockwell", size=25, weight="bold"
        )
        self.text_font = ctk.CTkFont(family="Rockwell", size=15)
        self.button_font = ctk.CTkFont(
            family="Rockwell", size=16, weight="bold"
        )

    def display(self) -> None:
        """Display the login screen."""

        self.title = ctk.CTkLabel(
            self.login_frame,
            text="Login Here!",
            font=self.title_font,
            corner_radius=10,
        )

        self.enrollmentid = ctk.CTkLabel(
            self.login_frame,
            text="User Name:",
            font=self.text_font,
            corner_radius=10,
        )
        self.enrollmentid_entry = ctk.CTkEntry(
            self.login_frame,
            textvariable=self.__userName,
            width=220,
            font=self.text_font,
        )

        self.pswrd_CTkLabel = ctk.CTkLabel(
            self.login_frame,
            text="Password:",
            font=self.text_font,
            corner_radius=10,
        )
        self.pswrd_entry = ctk.CTkEntry(
            self.login_frame, textvariable=self.__password, width=220, show="*"
        )

        self.submit_button = ctk.CTkButton(
            self.login_frame,
            text="Submit",
            font=self.button_font,
            width=150,
            height=40,
            corner_radius=10,
            command=self.submit,
        )

        self.enrollmentid_entry.bind("<Return>", lambda event: self.submit())
        self.pswrd_entry.bind("<Return>", lambda event: self.submit())

        self.title.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        self.enrollmentid_entry.place(relx=0.6, rely=0.4, anchor=ctk.CENTER)
        self.enrollmentid.place(relx=0.2, rely=0.4, anchor=ctk.CENTER)
        self.enrollmentid_entry.focus()

        self.pswrd_entry.place(relx=0.6, rely=0.55, anchor=ctk.CENTER)
        self.pswrd_CTkLabel.place(relx=0.2, rely=0.55, anchor=ctk.CENTER)

        self.submit_button.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)

    def submit(self) -> bool:
        """Submit the login details.

        Returns:
            True if the details are entered, else False.
        """

        if self.__userName.get() == "" or self.__password.get() == "":
            ctk.CTkLabel(
                self.login_frame,
                text="Please enter all the details!",
                corner_radius=10,
                font=self.text_font,
            ).place(relx=0.51, rely=0.9, anchor=ctk.CENTER)

        # elif not re.match(
        #     r"^(?=.*[A-Z])", self.__password.get()
        # ):
        #     ctk.CTkLabel(
        #         self.login_frame,
        #         text="Please enter a valid password (Must contain uppercase letter)",
        #         corner_radius=10,
        #         font=self.text_font,
        #     ).place(relx=0.51, rely=0.9, anchor=ctk.CENTER)

        elif not (self.db.login(self.get_credentials())):
            ctk.CTkLabel(
                self.login_frame,
                text="Invalid credentials!",
                corner_radius=10,
                font=self.text_font,
            ).place(relx=0.51, rely=0.9, anchor=ctk.CENTER)

        else:
            self.login_frame.after(1000, self.login_delay)

            for widget in self.login_frame.winfo_children():
                widget.destroy()

            ctk.set_appearance_mode("dark")

            ctk.CTkLabel(
                self.login_frame, text="Logging in...", font=self.text_font
            ).place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def login_delay(self) -> None:
        """Delay the login screen."""
        self.login_completed = True

    def get_credentials(self) -> tuple:
        """Get the credentials entered by the user.

        Returns:
            tuple: The userName and password entered by the user.
        """
        return (self.__userName.get(), self.__password.get())

    def return_login_frame(self) -> ctk.CTkFrame:
        """Return the login frame."""
        return self.login_frame