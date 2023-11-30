import sqlite3
import tkinter as tk
from tkinter import Label, Entry, Button, Listbox, END, messagebox, BooleanVar

class GestorPreguntasRespuestas(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.master.title("Gestor de Preguntas y Respuestas")
        
        # Crear la base de datos y la conexión
        self.conexion = self._crear_base_datos()

        # Establecer las dimensiones de la ventana
        self.master.geometry("1000x500")

        # Crear los paneles
        self.panel_preguntas = tk.Frame(self.master)
        self.panel_preguntas.rowconfigure(1, weight=1)
        self.panel_preguntas.columnconfigure(0, weight=1)
        self.panel_respuestas = tk.Frame(self.master)

        # Agregar los paneles a la ventana
        self.panel_preguntas.grid(row=0, column=0, padx=10, pady=10)
        self.panel_respuestas.grid(row=0, column=1, padx=10, pady=10)

        # Crear la barra de búsqueda del panel de preguntas
        self.barra_busqueda_preguntas = tk.Entry(self.panel_preguntas)
        self.barra_busqueda_preguntas.grid(row=0, column=0, padx=10, pady=10)
        self.barra_busqueda_preguntas.grid_propagate(False)

        # Crear la lista de preguntas del panel de preguntas
        self.lista_preguntas = tk.Listbox(self.panel_preguntas)
        self.lista_preguntas.grid(row=1, column=0, padx=10, pady=10)
        self.lista_preguntas.grid_propagate(False)

        # Asociar el evento de selección de pregunta a la función
        self.lista_preguntas.bind('<<ListboxSelect>>', self._mostrar_respuestas_seleccionadas)

        # Crear el botón de agregar pregunta del panel de preguntas
        self.boton_agregar_pregunta = tk.Button(self.panel_preguntas, text="Agregar pregunta", command=self._manejar_insercion)
        self.boton_agregar_pregunta.grid(row=2, column=0, padx=10, pady=10)
        self.boton_agregar_pregunta.grid_propagate(False)

        # Crear botones y funciones de borrado
        self._crear_interfaz_borrado()

        # Crear la barra de búsqueda del panel de respuestas
        self.barra_busqueda_respuestas = tk.Entry(self.panel_respuestas)
        self.barra_busqueda_respuestas.grid(row=0, column=0, padx=10, pady=10)
        self.barra_busqueda_respuestas.grid_propagate(False)

        # Crear la lista de respuestas del panel de respuestas
        self.lista_respuestas = tk.Listbox(self.panel_respuestas)
        self.lista_respuestas.grid(row=1, column=0, padx=10, pady=10)
        self.lista_respuestas.grid_propagate(False)

        # Crear el botón de agregar respuesta del panel de respuestas
        self.boton_agregar_respuesta = tk.Button(self.panel_respuestas, text="Agregar respuesta", command=self._agregar_respuesta)
        self.boton_agregar_respuesta.grid(row=2, column=0, padx=10, pady=10)
        self.boton_agregar_respuesta.grid_propagate(False)

        # Crear la lista de preguntas y respuestas
        self._mostrar_preguntas_y_respuestas()

    def _crear_base_datos(self):
        conexion = sqlite3.connect("base_de_datos.db")
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS preguntas (
                id INTEGER PRIMARY KEY,
                pregunta TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS respuestas (
                id INTEGER PRIMARY KEY,
                pregunta_id INTEGER,
                respuesta TEXT,
                correcta INTEGER,
                FOREIGN KEY (pregunta_id) REFERENCES preguntas (id)
            )
        """)

        conexion.commit()
        return conexion

    def _mostrar_preguntas_y_respuestas(self):
        cursor = self.conexion.cursor()

        cursor.execute("SELECT * FROM preguntas")
        preguntas = cursor.fetchall()

        self.lista_preguntas.delete(0, END)
        for pregunta in preguntas:
            self.lista_preguntas.insert(END, f"{pregunta[0]}. {pregunta[1]}")

    def _mostrar_respuestas_seleccionadas(self, event):
        seleccion_pregunta = self.lista_preguntas.curselection()
        if seleccion_pregunta:
            pregunta_id = int(self.lista_preguntas.get(seleccion_pregunta)[0].split('.')[0])
            cursor = self.conexion.cursor()

            cursor.execute("SELECT * FROM respuestas WHERE pregunta_id=?", (pregunta_id,))
            respuestas = cursor.fetchall()

            self.lista_respuestas.delete(0, END)
            for respuesta in respuestas:
                self.lista_respuestas.insert(END, f"{respuesta[0]}. {respuesta[2]} (Correcta: {respuesta[3]})")

    def _agregar_respuesta(self):
        seleccion_pregunta = self.lista_preguntas.curselection()
        if seleccion_pregunta:
            pregunta_id = int(self.lista_preguntas.get(seleccion_pregunta)[0].split('.')[0])
            respuesta_texto = self.barra_busqueda_respuestas.get()
            correcta = 0  # Cambiar a 1 si la respuesta es correcta, según tu lógica.

            if respuesta_texto:
                cursor = self.conexion.cursor()

                cursor.execute("""
                    INSERT INTO respuestas (pregunta_id, respuesta, correcta)
                    VALUES (?, ?, ?)
                """, (pregunta_id, respuesta_texto, correcta))

                self.conexion.commit()

                # Actualizar la lista de respuestas en la interfaz
                self._mostrar_respuestas_seleccionadas(None)
                self.barra_busqueda_respuestas.delete(0, 'end')
            else:
                messagebox.showwarning("Advertencia", "Ingrese texto en la respuesta.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una pregunta antes de agregar una respuesta.")

    def _insertar_pregunta(self, pregunta_texto):
        cursor = self.conexion.cursor()

        cursor.execute("""
            INSERT INTO preguntas (pregunta)
            VALUES (?)
        """, (pregunta_texto,))

        pregunta_id = cursor.lastrowid
        self.conexion.commit()

        return pregunta_id

    def _borrar_pregunta_seleccionada(self):
        seleccion_pregunta = self.lista_preguntas.curselection()
        if seleccion_pregunta:
            pregunta_id = int(self.lista_preguntas.get(seleccion_pregunta)[0].split('.')[0])
            cursor = self.conexion.cursor()

            # Borrar respuestas asociadas a la pregunta
            cursor.execute("DELETE FROM respuestas WHERE pregunta_id=?", (pregunta_id,))

            # Borrar la pregunta
            cursor.execute("DELETE FROM preguntas WHERE id=?", (pregunta_id,))

            self.conexion.commit()

            # Actualizar la lista de preguntas y respuestas en la interfaz
            self._mostrar_preguntas_y_respuestas()
            self.lista_respuestas.delete(0, END)  # Limpiar la lista de respuestas en la interfaz

    def _borrar_respuesta_seleccionada(self):
        seleccion_respuesta = self.lista_respuestas.curselection()
        if seleccion_respuesta:
            respuesta_id = int(self.lista_respuestas.get(seleccion_respuesta)[0].split('.')[0])
            cursor = self.conexion.cursor()

            # Borrar la respuesta
            cursor.execute("DELETE FROM respuestas WHERE id=?", (respuesta_id,))

            self.conexion.commit()

            # Actualizar la lista de respuestas en la interfaz
            self._mostrar_respuestas_seleccionadas(None)
            self.lista_respuestas.delete(self.lista_respuestas.curselection())  # Limpiar la lista de respuestas en la interfaz

    def _crear_interfaz_borrado(self):
        # Botón y función para borrar pregunta y respuestas
        self.boton_borrar_pregunta = tk.Button(self.panel_preguntas, text="Borrar pregunta", command=self._borrar_pregunta_seleccionada)
        self.boton_borrar_pregunta.grid(row=3, column=0, padx=10, pady=10)
        self.boton_borrar_pregunta.grid_propagate(False)

        # Botón y función para borrar respuesta
        self.boton_borrar_respuesta = tk.Button(self.panel_respuestas, text="Borrar respuesta", command=self._borrar_respuesta_seleccionada)
        self.boton_borrar_respuesta.grid(row=3, column=0, padx=10, pady=10)
        self.boton_borrar_respuesta.grid_propagate(False)

    def _manejar_insercion(self):
        pregunta_texto = self.barra_busqueda_preguntas.get()

        if pregunta_texto:
            try:
                pregunta_id = self._insertar_pregunta(pregunta_texto)
                messagebox.showinfo("Éxito", "Pregunta insertada correctamente.")
                self._mostrar_preguntas_y_respuestas()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo insertar la pregunta: {e}")
        else:
            messagebox.showwarning("Advertencia", "Ingrese texto en la pregunta.")

    def ejecutar(self):
        self.master.mainloop()

# Crear una instancia del gestor y ejecutar la aplicación
root = tk.Tk()
gestor = GestorPreguntasRespuestas(root)
gestor.ejecutar()
