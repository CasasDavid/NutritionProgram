import customtkinter as ctk 
import tkinter as tk

class VentanaUsuario:
    def __init__(
            self,
            userName: str = "",
        ) -> None:
        #Defino las caracteristicas básicas del frame
        self.user_id = userName
        self.text_font = ctk.CTkFont(
            family="Rockwell", size=20, weight="normal"
        )
        self.small_text_font = ctk.CTkFont(
            family="Rockwell", size=18, weight="normal"
        )


    def Vista_Usuario(self,db_object):
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
        user_details = db_object.get_signupdetails(self.user_id)

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
    
        return self.dashboard_frame