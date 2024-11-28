from Model.ConexionDB import ConexionDB
from tkinter import messagebox

class Usuario():
    def __init__(self):
        self.__nombre = None
        self.__contrasena = None

    def iniciarSesion(self, nombreUsuario, password, loggin):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Select * from jugadores")
        listaUsuario = cursor.fetchall()
        for usuario in listaUsuario:
            if(usuario[1] == nombreUsuario and usuario[2] == password):
                self.nombre = usuario[1]
                self.contrasena = usuario[2]
            else:
                messagebox.showinfo("informacion", "Acceso Correcto USuario")  
                miConexion.cerrarConexion()
                return
        messagebox.showerror("Advertencia", "El nombre de usuario y/o contraseña no existe, verifique e intente nuevamente!")

    def crearUsuario(self, nombreUsu, passwordUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO jugadores (nombre, contrasena) VALUES (?, ?)", (nombreUsu, passwordUsu))
        conexion.commit()
        miConexion.cerrarConexion


    def existeUsuario(self, nombreUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM jugadores WHERE nombre = ?", (nombreUsu,))
        conexion.commit()
        miConexion.cerrarConexion
        