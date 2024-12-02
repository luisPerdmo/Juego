import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip


from Controller.Usuario import Usuario
from View.crearUsuario import CrearUsuario  
from View.VistaJuego import VistaJuego

class Loggin():

    def validarCampos(self, event):
        if len(self.txtUsuario.get()) > 15:
            self.txtUsuario.delete(len(self.txtUsuario.get()) - 1, END)
        if len(self.txtPassword.get()) > 15:
            self.txtPassword.delete(len(self.txtPassword.get()) - 1, END)
        if len(self.txtUsuario.get()) >= 3 and len(self.txtPassword.get()) >= 3:
            if len(self.txtUsuario.get()) <= 15 and len(self.txtPassword.get()) <= 15:
                self.btnIngresar.config(state="normal")
            else:
                self.btnIngresar.config(state="disabled")

    def verCaracteres(self, event):
        if(self.bandera == True):
            self.txtPassword.config(show='*')
            self.btnVer.config(image=self.IconoOcul)
            self.bandera = False
        else:
            self.txtPassword.config(show='')
            self.btnVer.config(image=self.IconoVer)
            self.bandera = True

    def limpiarCampos(self, event):
        self.txtUsuario.delete(0, END)
        self.txtPassword.delete(0, END)
        self.txtUsuario.delete(0, END)
        self.txtPassword.delete(0, END)
      
    def ingresar(self, event):
        self.miUsuario = Usuario()
        self.miUsuario.iniciarSesion(self.txtUsuario.get(), self.txtPassword.get(), self.ventana)
    
    def abrirVentanaCrearUsuario(self, event):
        CrearUsuario(Usuario())

    def vistaJuego(self, event):
        juego = VistaJuego(self.ventana, self.miUsuario)

    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Introduce tu usuario y contraseña. Si no tienes cuenta, crea una nueva.")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0, 0)
        self.ventana.config(width=500, height=450)
        self.ventana.config(bg="#FFFFFF")
        self.ventana.title("Inicio de sesion")

        #Variables
        self.bandera = False
        self.caracteresUsuario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.']
        self.caracteresPassword = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        #Iconos
        self.IconoOcul = tk.PhotoImage(file=r"Juego/Src/Ocultar.png")
        self.IconoVer = tk.PhotoImage(file=r"Juego/Src/Ver.png")
        self.IconoLoggin = tk.PhotoImage(file=r"Juego/Src/imagenLoggin-2.png")
        self.IconoAyuda = tk.PhotoImage(file=r"Juego/Src/Ayuda2.png (1).png")

        #Frame que agrupa el contenido
        self.frame = tk.Frame(self.ventana, width=390, height=350, bg="#F0F0F0")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        #Texto
        self.lblIcono = tk.Label(self.frame, image=self.IconoLoggin, bg="#F0F0F0")
        self.lblIcono.place(x=30, y=0.1)

        self.lblTitulo = tk.Label(self.frame, text="Happy Cóndor", font=("Comic Sans MS", 28, "bold"), bg="#F0F0F0")
        self.lblTitulo.place(x=125, y=40)

        self.lblUsuario = tk.Label(self.frame, text="Usuario*:", bg="#F0F0F0")
        self.lblUsuario.place(x=85, y=120)

        self.lblPassword = tk.Label(self.frame, text="Password*:", bg="#F0F0F0")
        self.lblPassword.place(x=85, y=170)

        #Campo de entrada
        self.txtUsuario = tk.Entry(self.frame, width=25)
        self.txtUsuario.place(x=80, y=140)
        Tooltip(self.txtUsuario, "Ingrese su nombre de usuario, solo letras minusculas, n/ min 3 caracteres , max 25 caracteres.")
        self.txtUsuario.bind("<KeyRelease>", self.validarCampos)

        self.txtPassword = tk.Entry(self.frame, width=25, show="*")
        self.txtPassword.place(x=80, y=190)
        Tooltip(self.txtPassword, "Ingrese su contraseña de usuario, solo letras minusculas, n/ min 3 caracteres , max 15 caracteres.")
        self.txtPassword.bind("<KeyRelease>", self.validarCampos)

        #Botones
        self.btnVer = tk.Button(self.frame, image=self.IconoVer, width=25, height=20, bg="#FFFFFF")
        self.btnVer.place(x=320, y=190)
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)

        self.btnIngresar = tk.Button(self.frame, text="Ingresar", width=8)
        self.btnIngresar.place(x=80, y=240)
        Tooltip(self.btnIngresar, "Presione para iniciar sesión si ha completado correctamente los campos.")
        self.btnIngresar.bind("<Button-1>", self.ingresar)

        self.btnLimpiar = tk.Button(self.frame, text="Limpiar", width=8)
        self.btnLimpiar.place(x=208, y=240)
        Tooltip(self.btnLimpiar, "Presione para limpiar los campos de texto.")
        self.btnLimpiar.bind("<Button-1>" , self.limpiarCampos)

        self.btnCrearCuenta = tk.Button(self.frame, text="Crear Cuenta", width=22)
        self.btnCrearCuenta.place(x=80, y=280)
        Tooltip(self.btnCrearCuenta, "Presione para abrir la ventana de creación de cuenta.")
        self.btnCrearCuenta.bind("<Button-1>" , self.abrirVentanaCrearUsuario)

        self.lblAyuda = tk.Label(self.frame, width=25, height=25, image=self.IconoAyuda)
        self.lblAyuda.place(x=350, y=10) 
        Tooltip(self.lblAyuda, "Presione para obtener información sobre cómo usar la aplicación.")
        self.lblAyuda.bind("<Button-1>", self.mostrarAyuda)

        self.ventana.mainloop()