"""Database module"""
import sqlite3
import uuid

class Database:
    """Database class"""

    def __init__(self, module_name: str = "Not Provided") -> None:
        """Initialize the database connection and cursor."""
        try:
            self.connection = sqlite3.connect("Program/DataBase/DataBase.db")
            self.cursor = self.connection.cursor()
            print("Database connection successful -", module_name)

        except sqlite3.OperationalError as error:
            print("Error: ", error)

    def get_patients(self) -> list:
        """Get a patients from the database.

        Returns:
            list: All patiends details
        """
        self.cursor.execute("SELECT * FROM PatientTable")
        return self.cursor.fetchall()

    def get_col_headings(self, table_name: str) -> list:
        """Get the column headings of the patients table.

        Args:
            table_name: Name of the table

        Returns:
            list: Column headings
        """

        self.cursor.execute(f"SELECT * FROM {table_name}")
        return [description[0] for description in self.cursor.description]

    def signup(self, credentials: tuple) -> bool:
        """Add a new user to the database.

        Args:
            credentials (tuple): User credentials

        Returns:
            bool: True if signup successful, False otherwise
        """

        username = credentials[0]
        Nombre = credentials[1]
        Apellido = credentials[2]
        password = credentials[3]
        email = credentials[4]
        enrollid = str(uuid.uuid4())

        try:
            self.cursor.execute(
                "INSERT INTO credentials VALUES (?, ?, ?, ?, ?,?)",
                (enrollid, username, Nombre, Apellido, email, password),
            )
            self.connection.commit()

            print("Signup successful")
            return True

        except sqlite3.IntegrityError as e:
            # Verificar el código de error para determinar la causa específica
            error_code = e.args[0]

            if error_code == sqlite3.SQLITE_CONSTRAINT and "UNIQUE constraint failed: credentials.enrollid" in str(e):
                print("Error: Enrollment ID already exists")
                return False
            elif error_code == sqlite3.SQLITE_CONSTRAINT and "UNIQUE constraint failed: credentials.username" in str(e):
                print("Error: Username already exists")
                return False
            elif error_code == sqlite3.SQLITE_CONSTRAINT and "UNIQUE constraint failed: credentials.email" in str(e):
                print("Error: Email address already exists")
                return False
            else:
                print("Error: Database operation failed")
                return False

    def get_signupdetails(self, username: str) -> list:
        """Get the signup details of the user.

        Args:
            username (str): username ID of the user

        Returns:
            list: Signup details
        """
        self.cursor.execute(
            "SELECT * FROM credentials WHERE username = (?)",
            (username,),
        )
        return self.cursor.fetchone()

    def login(self, credentials: tuple) -> bool:
        """Verify the login credentials of the user.

        Args:
            credentials (tuple): [Enrollment ID, Password]

        Returns:
            bool: True if credentials are correct, False otherwise
        """
        self.cursor.execute(
            "SELECT * FROM credentials WHERE username = (?)",
            (credentials[0],),
        )

        fetched = self.cursor.fetchone()

        if fetched:

            if fetched[5] == credentials[1]:
                print("Login Credentials verified")
                return True

            print("Wrong password entered")

        print("Wrong enrollment ID entered")
        return False

    def get_medicine_record(self, enrollment_id) -> list:
        """Get the medicine record from the database.

        Returns:
            list: Medicine record
        """
        self.cursor.execute(
            "SELECT * FROM MRECORD WHERE enrollid = (?)", (enrollment_id,)
        )
        return self.cursor.fetchall()

    def get_medicine_details(self, mid: str) -> list:
        """Get the medicine details from the database.

        Returns:
            list: Medicine details
        """
        self.cursor.execute("SELECT * FROM medicines WHERE MID = (?)", (mid,))
        return self.cursor.fetchone()

    def add_orders(self, mid_list: list, enrollment_id: str) -> None:
        """Add orders to the database.

        Args:
            mid_list (list): List of medicine IDs
            enrollment_id (str): Enrollment ID of the user
        """

        for mid in mid_list:
            self.cursor.execute(
                "INSERT INTO MRECORD (enrollid ,MID) VALUES (?, ?)",
                (
                    enrollment_id,
                    mid,
                ),
            )

        print(f"{len(mid_list)} orders added to the database")
        self.connection.commit()

    def add_patient(self, credentials: tuple) -> bool:
        """Add a new user to the database.

        Args:
            credentials (tuple): Patient credentials

        Returns:
            bool: True if user creation successful, False otherwise
        """
        
        SK = str(uuid.uuid4())
        nombre = credentials[0]
        apellido = credentials[1]
        ID = credentials[2] 
        telefono=credentials[3]
        email = credentials[4]
        estatura = credentials[5]
        peso=credentials [6]
        edad = credentials[7]
        genero=credentials[8]
        alergias=credentials[9]
        actividad=credentials[10]
        examenes=credentials[11]
        ##AGREGAR EL RESTO DE VARIABLES PARA QUE SE VEA COMO EL FORMATO

        try:
            self.cursor.execute(
                "INSERT INTO PatientTable VALUES (?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?, ?, ?)",
                (SK, nombre, apellido, ID, telefono, email, estatura, peso, edad, genero, alergias, actividad, examenes),
            )
            self.connection.commit()

            print("USER CREATED")
            return True

        except sqlite3.IntegrityError as e:
            # Verificar el código de error para determinar la causa específica
            error_code = e.args[0]

            # if error_code == sqlite3.SQLITE_CONSTRAINT and "UNIQUE constraint failed: credentials.ID" in str(e):
            #     print("Error: Ya existe un usuario con ese ID")
            #     return False
            # elif error_code == sqlite3.SQLITE_CONSTRAINT and "UNIQUE constraint failed: credentials.email" in str(e):
            #     print("Error: Correo en formato inválido")
            #     return False
            # elif error_code == sqlite3.SQLITE_CONSTRAINT and "UNIQUE constraint failed: credentials.Nombre" in str(e):
            #     print("Error: La extensión máxima del nombre es 30 caracteres")
            #     return False
            # else:
            #     print("Error: Database operation failed")
            #     return False
            
    def upload_patient(self, credentials: tuple ,SK) -> bool:
        """Add a new user to the database.

        Args:
            credentials (tuple): Patient credentials

        Returns:
            bool: True if user creation successful, False otherwise
        """
        
        nombre = credentials[0]
        apellido = credentials[1]
        ID = credentials[2] 
        telefono=credentials[3]
        email = credentials[4]
        estatura = credentials[5]
        peso=credentials [6]
        edad = credentials[7]
        genero=credentials[8]
        alergias=credentials[9]
        actividad=credentials[10]
        examenes=credentials[11]
        ##AGREGAR EL RESTO DE VARIABLES PARA QUE SE VEA COMO EL FORMATO

        try:
            self.cursor.execute(
                "UPDATE PatientTable SET Nombre=?, Apellido=?, ID=?, Telefono=?, Email=?, Estatura=?, Peso=?, Edad=?, Género=?, Alergias=?, Actividad=?, Exámenes=? WHERE SK=?",
                (nombre, apellido, ID, telefono, email, estatura, peso, edad, genero, alergias, actividad, examenes, SK),
            )
            self.connection.commit()


            print("USER UPDATED")
            return True

        except sqlite3.IntegrityError as e:
            # Verificar el código de error para determinar la causa específica
            error_code = e.args[0]

            if error_code == sqlite3.SQLITE_CONSTRAINT and "UNIQUE constraint failed: credentials.ID" in str(e):
                print("Error: Ya existe un usuario con ese ID")
                return False
            elif error_code == sqlite3.SQLITE_CONSTRAINT and "UNIQUE constraint failed: credentials.email" in str(e):
                print("Error: Correo en formato inválido")
                return False
            elif error_code == sqlite3.SQLITE_CONSTRAINT and "UNIQUE constraint failed: credentials.Nombre" in str(e):
                print("Error: La extensión máxima del nombre es 30 caracteres")
                return False
            else:
                print("Error: Database operation failed")
                return False

    def view_client_info(self, patient_id: str) -> dict:
        """Get patient information based on SK.

        Args:
            patient_id (str): Patient ID (SK).

        Returns:
            dict: Patient information as a dictionary.
                  Returns an empty dictionary if the patient is not found.
        """
        try:
            self.cursor.execute(
                "SELECT * FROM PatientTable WHERE SK = ?",
                (patient_id,),
            )
            patient_info = self.cursor.fetchone()

            if patient_info:
                # Convierte la fila de la base de datos a un diccionario para facilitar su uso
                patient_dict = {
                    "SK": patient_info[0],
                    "Nombre": patient_info[1],
                    "Apellido": patient_info[2],
                    "ID": patient_info[3],
                    "Telefono":patient_info[4],
                    "email": patient_info[5],
                    "estatura": patient_info[6],
                    "Peso":patient_info[7],
                    "edad": patient_info[8],
                    "Genero":patient_info[9],
                    "Alergias":patient_info[10],
                    "Actividad":patient_info[11],
                    "Examenes":patient_info[12],

                    # Agrega más campos según sea necesario
                }
                return patient_dict
            else:
                print(f"No se encontró un paciente con SK: {patient_id}")
                return {}

        except Exception as e:
            print(f"Error al obtener información del paciente: {e}")
            return {}
        
    def insertar_registro(self,register: tuple):
    # Insertar datos en la tabla Registro'
        try:
            self.cursor.execute(
                "INSERT INTO PatientTable VALUES (?, ?, ?, ?, ?)",
                (register[0], register[1], register[2], register[3], register[4]),
            )
            self.connection.commit()

            print("Registro creado")

        except Exception as e:
            print(f"Error al crear registro del paciente: {e}")
            return {}

    def view_client_register(self, patient_id: str) -> dict:
        """Get patient information based on SK del paciente.

        Args:
            patient_id (str): Patient ID (SK).

        Returns:
            dict: Patient information as a dictionary.
                  Returns an empty dictionary if the patient is not found.
        """
        try:
            self.cursor.execute(
                "SELECT * FROM Registro WHERE paciente = ? ORDER BY Fecha DESC LIMIT 5",
                (patient_id,),
            )
            patient_info = self.cursor.fetchall()

            if patient_info:

                return patient_info
            else:
                print(f"No se encontró un paciente con SK: {patient_id}")
                return {}

        except Exception as e:
            print(f"Error al obtener información del paciente: {e}")
            return {}
