import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Loggin():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0, 0)
        self.ventana.config(width=500, height=450)
        self.ventana.config(bg="#FFFFFF")
        self.ventana.title("Inicio de sesion")

        #Iconos
        self.IconoLoggin = tk.PhotoImage(file=r"Juego/Src/imagenLoggin-2.png")

        #Frame que agrupa el contenido
        self.frame = tk.Frame(self.ventana, width=390, height=350, bg="#F0F0F0")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.lblIcono = tk.Label(self.frame, image=self.IconoLoggin, bg="#F0F0F0")
        self.lblIcono.place(x=30, y=0.1)

        self.lblTitulo = tk.Label(self.frame, text="Happy Cóndor", font=("Comic Sans MS", 28, "bold"), bg="#F0F0F0")
        self.lblTitulo.place(x=125, y=40)

        #Campo de entrada
        self.txtUsuario = tk.Entry(self.frame, width=25)
        self.txtUsuario.place(x=80, y=140)

        self.txtPassword = tk.Entry(self.frame, width=25)
        self.txtPassword.place(x=80, y=190)

        #Botones
        self.btnIngresar = tk.Button(self.frame, text="Ingresar", width=8)
        self.btnIngresar.place(x=80, y=240)

        self.btnLimpiar = tk.Button(self.frame, text="Limpiar", width=8)
        self.btnLimpiar.place(x=208, y=240)

        self.btnCrearCuenta = tk.Button(self.frame, text="Crear Cuenta", width=22)
        self.btnCrearCuenta.place(x=80, y=280)

        self.ventana.mainloop()