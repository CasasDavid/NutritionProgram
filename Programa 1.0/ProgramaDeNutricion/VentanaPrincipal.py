"""Home screen of the application."""
import customtkinter as ctk

from ProgramaDeNutricion.centerwin import center_window
from ProgramaDeNutricion.LogIn import Login
from ProgramaDeNutricion.Registro import Signup


class HomeScreen:
    """Home screen of the application."""

    def __init__(
        self,
        width: int = 500,
        height: int = 500,
        appearance_mode: str = "light",
    ) -> None:

        self.width = width
        self.height = height

        self.root = ctk.CTk()
        self.root.resizable(False, False)
        center_window(self.root, self.width, self.height)

        ctk.set_appearance_mode(appearance_mode)
        ctk.set_default_color_theme("assets/SiluetaPaletteInit.json")

        # exits the program when the window is closed by the user
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        self.root.title("Silueta - principal")

        self.selected_tab = ""
        self.__user_enrollment_id = ""

        self.tabview = ctk.CTkTabview(self.root, width=200, corner_radius=10)

        self.font = ctk.CTkFont(family="Rockwell", size=15)

    def homescreen(self) -> None:
        """Display the homescreen."""

        center_window(self.root, self.width, self.height)

        self.tabview.add("Login")
        self.tabview.add("Signup")
        self.tabview.pack(fill="both", expand=True, anchor=ctk.CENTER)

        login_object = Login(
            color_theme="green",
            root=self.tabview.tab("Login"),
            width=self.width,
            height=self.height,
            appearance_mode="dark",
        )
        login_tab_frame = login_object.return_login_frame()
        login_tab_frame.pack(fill="both", expand=True, anchor=ctk.CENTER)

        signup_object = Signup(
            root=self.tabview.tab("Signup"),
            width=self.width,
            height=self.height,
            appearance_mode="light",
            color_theme="green",
        )
        signup_tab_frame = signup_object.return_signup_frame()
        signup_tab_frame.pack(fill="both", expand=True, anchor=ctk.CENTER)

        login_object.display()

        while True:

            self.root.update()

            if login_object.login_completed:
                print("User logged in successfully.")
                self.__userName = login_object.get_credentials()[0]
                break

            if signup_object.signup_completed:
                print("User signed up successfully.")
                self.__userName = signup_object.get_credentials()[0]
                break

        self.root.destroy()
        self.root.mainloop()

    def get_user_enrollment_id(self) -> str:
        """Return the enrollment id of the user."""
        return self.__userName

    def show_homescreen(self) -> None:
        """Show the homescreenwindow"""
        self.homescreen()