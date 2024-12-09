import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class CrearUsuario():
     
    def mostrarAyuda(self, event):
        texto_ayuda = (
        "Atajos Del Juego:\n"
        "- Presione 'g' para guardar el usuario.\n"
        "- Presiona 'l' para limpiar los campos.\n"
        "- presione 'F1' para mostrar este ayuda. \n" 
        )
        messagebox.showinfo("Ayuda", texto_ayuda)

    def validarCampos(self, event):
        if len(self.txtNombre.get()) > 25:
            self.txtNombre.delete(len(self.txtNombre.get()) - 1, END)
        if len(self.txtContrasena.get()) > 25:
            self.txtContrasena.delete(len(self.txtContrasena.get()) - 1, END)

        nombreValido = len(self.txtNombre.get()) >= 3 and self.txtNombre.get().strip() != ""
        contrasenaValida = len(self.txtContrasena.get()) >= 6 and self.txtContrasena.get().strip() != ""
        if nombreValido and contrasenaValida:
            self.btnGuardar.config(state="normal")
        else:
            self.btnGuardar.config(state="disabled")

    def guardarUsuario(self, event):
        nombre = self.txtNombre.get().strip()  
        contrasena = self.txtContrasena.get().strip()
        if not nombre or not contrasena:  
            messagebox.showerror("Error", "Por favor, ingrese un nombre y una contraseña válidos.")
            return
        if self.Usuario.existeUsuario(nombre): 
            messagebox.showerror("Error", "El nombre de usuario ya existe. Por favor, elige otro.")
            return
        self.Usuario.crearUsuario(nombre, contrasena)
        messagebox.showinfo("Confirmación", "¡Nuevo usuario registrado con éxito!")
        self.limpiarCampos(event)

    def limpiarCampos(self, event):
        self.txtNombre.delete(0, END)
        self.txtContrasena.delete(0, END)
        self.btnGuardar.config(state="disabled")

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Crear Nuevo Usuario")
        self.ventana.config(bg="#FFFFFF")
        self.ventana.config(width=360, height=385)
        self.ventana.resizable(0, 0)
        self.ventana.focus_set()

        self.Usuario = Usuario

        #iconos 
        self.IconoAgregar = tk.PhotoImage(file=r"Juego/Src/user_add.png")
        self.IconoLimpiar = tk.PhotoImage(file=r"Juego/Src/textfield_delete.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Juego\Src\Ayuda2.png (1).png")

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
        Tooltip(self.txtNombre, "Ingrese su nombre de usuario, mínimo 3 caracteres, máximo 25 caracteres.")
        self.txtNombre.bind("<KeyRelease>", self.validarCampos)

        self.txtContrasena = tk.Entry(self.frame)
        self.txtContrasena.place(x=50, y=170)
        Tooltip(self.txtContrasena, "Ingrese su contraseña, mínimo 6 caracteres, máximo 25 caracteres.")
        self.txtContrasena.bind("<KeyRelease>", self.validarCampos)

        #Botones
        self.btnGuardar = tk.Button(self.frame, text="Guardar", state="disabled", bg="#F0F0F0", image=self.IconoAgregar, compound="left")
        self.btnGuardar.place(x=50, y=230, width=190)
        Tooltip(self.btnGuardar, "Guarde los datos del nuevo usuario.")
        self.btnGuardar.bind("<Button-1>", self.guardarUsuario)

        self.btnLimpiar = tk.Button(self.frame, text="Limpiar", bg="#F0F0F0", image=self.IconoLimpiar, compound="left")
        self.btnLimpiar.place(x=50, y=265, width=190)
        Tooltip(self.btnLimpiar, "Limpiar los campos de texto.")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)

        self.lblAyuda = tk.Label(self.frame, image=self.iconoAyuda)
        self.lblAyuda.place(relx=1, y=10, anchor="ne")
        Tooltip(self.lblAyuda, "Muestra ayuda sobre cómo usar esta ventana.")
        self.lblAyuda.bind("<Button-1>", self.mostrarAyuda)

        # Atajos
        self.ventana.bind("<g>", self.guardarUsuario)
        self.ventana.bind("<l>", self.limpiarCampos)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()