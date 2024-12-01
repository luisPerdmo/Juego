from Model.ConexionDB import ConexionDB
from tkinter import messagebox
from View.VistaJuego import VistaJuego

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
                messagebox.showinfo("Informacion", "Acceso Correcto Usuario")
                mijuego = VistaJuego(loggin, self)
                miConexion.cerrarConexion()
                return
            messagebox.showerror("Advertencia", "El nombre de usuario y/o contraseña no existe, verifique e intente nuevamente!")
            miConexion.cerrarConexion()

    def actualizarPuntos(self, nombreUsu, puntos):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("SELECT puntaje FROM jugadores WHERE nombre = ?", (nombreUsu,))
        resultado = cursor.fetchone()

        if resultado and puntos > resultado[0]:
            cursor.execute("UPDATE jugadores SET puntaje = ? WHERE nombre = ?", (puntos, nombreUsu))
            conexion.commit()

        miConexion.cerrarConexion()
            
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
        resultado = cursor.fetchone()
        miConexion.cerrarConexion
        return resultado is not None
    
    def consultarTabla(self):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Select * from jugadores")
        listaUsuario = cursor.fetchall()
        return listaUsuario
        