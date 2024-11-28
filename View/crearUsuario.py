import tkinter as tk
from tkinter import *
from tkinter import messagebox

class CrearUsuario():

    def validarCampos(self, event):
        
        nombre_valido = len(self.txtNombre.get()) >= 3
        contrasena_valida = len(self.txtContrasena.get()) >= 6  

        if nombre_valido and contrasena_valida:
            self.btnGuardar.config(state=tk.NORMAL)
        else:
            self.btnGuardar.config(state=tk.DISABLED)

    def guardarUsuario(self, event):
        nombre = self.txtNombre.get()
        contrasena = self.txtContrasena.get()

        if self.Usuario.existeUsuario(nombre):
            messagebox.showerror("Error", "El nombre de usuario ya existe. Por favor, elige otro.")
            return

        self.Usuario.crearUsuario(nombre, contrasena)
        messagebox.showinfo("Confirmación", "¡Nuevo usuario registrado con éxito!")
        self.limpiarCampos()

    def limpiarCampos(self):
        self.txtNombre.delete(0, END)
        self.txtContrasena.delete(0, END)
        self.btnGuardar.config(state=tk.DISABLED)

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.resizable(0, 0)
        self.ventana.title("Crear Nuevo Usuario")
        self.ventana.config(width=360, height=385)

        self.Usuario = Usuario

        self.lbltitulo = tk.Label(self.ventana, text="Crear Usuario", font=("Arial", 14, "bold"))
        self.lbltitulo.place(relx=0.5, y=40, anchor="center")

        self.lblNombre = tk.Label(self.ventana, text="Nombre*:", anchor="w")
        self.lblNombre.place(x=50, y=100, width=80, height=25)

        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(x=150, y=100, width=160, height=25)
        self.txtNombre.bind("<KeyRelease>", self.validarCampos)

        self.lblContrasena = tk.Label(self.ventana, text="Contraseña*:", anchor="w")
        self.lblContrasena.place(x=50, y=150, width=80, height=25)

        self.txtContrasena = tk.Entry(self.ventana)
        self.txtContrasena.place(x=150, y=150, width=160, height=25)
        self.txtContrasena.bind("<KeyRelease>", self.validarCampos)

        self.btnGuardar = tk.Button(self.ventana, text="Guardar", state=tk.DISABLED)
        self.btnGuardar.place(x=85, y=260, width=80, height=30)
        self.btnGuardar.bind("<Button-1>", self.guardarUsuario)

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar")
        self.btnLimpiar.place(x=195, y=260, width=80, height=30)
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)

        self.ventana.mainloop()