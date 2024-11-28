import tkinter as tk
from tkinter import *
import random

class VistaJuego:

    def moverCon(self, event):
        if self.x and self.y:
            if not self.perder:
                self.y -= 30
                self.canvas.coords(self.condorP, self.x, self.y)

    def moverCondor(self):
        if self.x and self.y:
            self.y += 5
            self.canvas.coords(self.condorP, self.x, self.y)
            if self.y < 0 or self.y > self.ventana.winfo_height():
                self.perder = True
            if not self.perder:
                self.ventana.after(50, self.moverCondor)

    def teerminarJuego(self, event):
        self.perder
        self.perder = True

    def destroy(self, event):
        self.ventana.destroy()

    def __init__(self, loggin, jugador):  
        self.ventana = tk.Toplevel(loggin)  
        self.ventana.title("Juego Principal")
        self.ventana.config(width=1000, height=600)
        self.ventana.resizable(0,0)

        self.x = 80
        self.y = 250
        self.puntuacion = 0 
        self.velocidad = 10
        self.perder = False

        #Imagenes
        self.imagenTubo = tk.PhotoImage(file=r"Juego/Src/tubo.png")
        self.imagenCondorV = tk.PhotoImage(file=r"Juego/Src/condorVolando.png")
        self.imagenCondorP = tk.PhotoImage(file=r"Juego/Src/condorPlaniando.png")
        
        #texto
        self.lblJugador = tk.Label(self.ventana, text=f"Jugador: {jugador.nombre}")
        self.lblJugador.place(x=30, y=1)  

        #canvas
        self.canvas = tk.Canvas(self.ventana, width=980, height=545, bg="#63BFFF")
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")  

        self.condorP = self.canvas.create_image(self.x, self.y, anchor="nw", image=self.imagenCondorP)
        self.puntos = self.canvas.create_text(75, 30, text="0", font=("3D Egoistism outline", 30))
        self.tubos = self.canvas.create_image(1200, -550, anchor="nw", image=self.imagenTubo)

        #botones
        self.btnCerrar = tk.Label(self.ventana, text="Cerrar")
        self.btnCerrar.place(x=940, y=573)  
        self.btnCerrar.bind("<Button-1>",self.destroy)

        #Eventos
        self.ventana.bind("<space>", self.moverCon)
        self.ventana.after(50, self.moverCondor)

        self.ventana.mainloop() 