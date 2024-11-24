import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Loggin():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0, 0)
        self.ventana.config(width=500, height=450)
        self.ventana.title("Inicio de sesion")

        #Iconos
        self.IconoLoggin = tk.PhotoImage(file=r"Juego/Src/imagenLoggin-2.png")

        #Frame que agrupa el contenido
        self.frame = tk.Frame(self.ventana, width=390, height=350, bg="#FFFFFF")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.lblIcono = tk.Label(self.frame, image=self.IconoLoggin, bg="#FFFFFF")
        self.lblIcono.place(x=30, y=0.1)

        self.lblTitulo = tk.Label(self.frame, text="Happy Cóndor", font=("Comic Sans MS", 28, "bold"), bg="#FFFFFF")
        self.lblTitulo.place(x=125, y=40)

        self.txtUsuario = tk.Entry(self.frame, width=25)
        self.txtUsuario.place(x=80, y=140)
        
        self.txtPassword = tk.Entry(self.frame, width=25)
        self.txtPassword.place(x=80, y=190)
    
        self.ventana.mainloop()