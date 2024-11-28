import tkinter as tk
from tkinter import *
from tkinter import messagebox

class CrearUsuario():

    def validarCampos(self, event):
        nombreValido = len(self.txtNombre.get()) >= 3 and self.txtNombre.get().strip() != ""
        contrasenaValida = len(self.txtContrasena.get()) >= 6 and self.txtContrasena.get().strip() != ""
        if nombreValido and contrasenaValida:
            self.btnGuardar.config(state=tk.NORMAL)
        else:
            self.btnGuardar.config(state=tk.DISABLED)

    def guardarUsuario(self, event):
        nombre = self.txtNombre.get().strip()  
        contrasena = self.txtContrasena.get().strip()
        if not nombre or not contrasena:  
            messagebox.showerror("Error", "Por favor, ingrese un nombre y una contraseña válidos.")
            return
        if self.Usuario.existeUsuario(nombre):  # Verificamos si el usuario ya existe
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
        self.ventana.title("Crear Nuevo Usuario")
        self.ventana.config(bg="#FFFFFF")
        self.ventana.config(width=360, height=385)
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        #Frame que agrupa el contenido
        self.frame = tk.Frame(self.ventana, width=300, height=325, bg="#F0F0F0")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        #Textos
        self.lbltitulo = tk.Label(self.frame, text="Crear Usuario", font=("Comic Sans MS", 28, "bold"), bg="#F0F0F0")
        self.lbltitulo.place(relx=0.5, y=40, anchor="center")

        self.lblNombre = tk.Label(self.frame, text="Nombre*:", anchor="w", bg="#F0F0F0")
        self.lblNombre.place(x=54, y=100)

        self.lblContrasena = tk.Label(self.frame, text="Password*:", anchor="w", bg="#F0F0F0")
        self.lblContrasena.place(x=54, y=150)
        
        #Campo de Entrada
        self.txtNombre = tk.Entry(self.frame)
        self.txtNombre.place(x=50, y=120)
        self.txtNombre.bind("<KeyRelease>", self.validarCampos)

        self.txtContrasena = tk.Entry(self.frame)
        self.txtContrasena.place(x=50, y=170)
        self.txtContrasena.bind("<KeyRelease>", self.validarCampos)

        #Botones
        self.btnGuardar = tk.Button(self.frame, text="Guardar", state=tk.DISABLED, bg="#F0F0F0")
        self.btnGuardar.place(x=50, y=230, width=190)
        self.btnGuardar.bind("<Button-1>", self.guardarUsuario)

        self.btnLimpiar = tk.Button(self.frame, text="Limpiar", bg="#F0F0F0")
        self.btnLimpiar.place(x=50, y=265, width=190)
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)

        self.ventana.mainloop()