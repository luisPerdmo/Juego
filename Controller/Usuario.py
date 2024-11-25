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
        cursor.execute("Select * from usuario")
        listaUsuario = cursor.fetchall()
        for usuario in listaUsuario:
            if(usuario[1] == nombreUsuario and usuario[2] == password):
                self.nombre = usuario[1]
                self.contrasena = usuario[2]
        messagebox.showerror("Advertencia", "El nombre de usuario y/o contraseña no existe, verifique e intente nuevamente!")
