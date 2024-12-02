import tkinter as tk
from tkinter import *
import random
from Tooltip import Tooltip

from View.ventanaPerder import VentanaPerder

class VistaJuego:

    def moverCon(self, event):
        if not self.perder:
            self.y -= 30
            if self.y < 0:
                self.y = 0
            self.canvas.coords(self.condorP, self.x, self.y)

    def moverCondor(self):
        if self.perder: 
            return
        self.y += 5
        if self.y > self.canvas.winfo_height() - 30: 
            self.y = self.canvas.winfo_height() - 30
        self.canvas.coords(self.condorP, self.x, self.y)

        if not self.perder:
            self.ventana.after(50, self.moverCondor)

    def teerminarJuego(self):
        self.perder = True
        self.jugador.actualizarPuntos(self.jugador.nombre, self.puntuacion)
        VentanaPerder(self.ventana, self.puntuacion, self.jugador.nombre, self)

    def reiniciarJuego(self):
        self.x = 80
        self.y = 250
        self.puntos = 0
        self.perder = False
        self.canvas.coords(self.condorP, self.x, self.y)
        self.canvas.coords(self.tubosA, 1200, -550)
        self.canvas.coords(self.tubosB, 1200, 550)
        self.canvas.itemconfigure(self.puntos, text="0")
        self.moverCondor()
        self.moverTubo()

    def moverTubo(self):
        if self.perder:  # Verifica si el juego terminó
            return
        self.canvas.move(self.tubosA, -self.velocidad, 0)
        self.canvas.move(self.tubosB, -self.velocidad, 0)
        if self.canvas.coords(self.tubosB)[0] < -100:
            self.puntuacion += 1
            self.velocidad += 1 
            self.canvas.itemconfigure(self.puntos, text=str(self.puntuacion))
            h = self.canvas.winfo_height()
            num = random.choice([i for i in range(160, h, 160)])
            self.canvas.coords(self.tubosB, self.canvas.winfo_width(), num + 160)
            self.canvas.coords(self.tubosA, self.canvas.winfo_width(), num - 900)

        if self.canvas.coords(self.tubosB):
            if self.canvas.bbox(self.condorP)[0] < self.canvas.bbox(self.tubosB)[2] and self.canvas.bbox(self.condorP)[2] > self.canvas.bbox(self.tubosB)[0]:
                if self.canvas.bbox(self.condorP)[1] < self.canvas.bbox(self.tubosA)[3] or self.canvas.bbox(self.condorP)[3] > self.canvas.bbox(self.tubosB)[1]:
                    self.teerminarJuego()

        if not self.perder:
            self.ventana.after(50, self.moverTubo)

    def destroy(self, event):
        self.ventana.destroy()

    def __init__(self, loggin, jugador):  
        self.ventana = tk.Toplevel(loggin)  
        self.ventana.title("Juego Principal")
        self.ventana.config(width=1020, height=785)
        self.ventana.resizable(0, 0)

        self.jugador = jugador
        self.x = 80
        self.y = 250
        self.puntuacion = 0 
        self.velocidad = 5
        self.perder = False

        # Imágenes
        self.imagenTubob = tk.PhotoImage(file=r"Juego/Src/tubo.png")
        self.imagenTuboA = tk.PhotoImage(file=r"Juego/Src/tubo2.png")
        self.imagenCondorV = tk.PhotoImage(file=r"Juego/Src/condorVolando.png")
        self.imagenCondorP = tk.PhotoImage(file=r"Juego/Src/condorPlaniando.png")
        
        # Texto
        self.lblJugador = tk.Label(self.ventana, text=f"Jugador: {jugador.nombre}")
        self.lblJugador.place(x=30, y=1)  

        # Canvas
        self.canvas = tk.Canvas(self.ventana, width=1000, height=730, bg="#63BFFF")
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")  

        self.condorP = self.canvas.create_image(self.x, self.y, anchor="nw", image=self.imagenCondorP)
        self.puntos = self.canvas.create_text(75, 30, text="0", font=("Impact", 40))
        self.tubosA = self.canvas.create_image(1200, -550, anchor="nw", image=self.imagenTuboA)
        self.tubosB = self.canvas.create_image(1200, 550, anchor="nw", image=self.imagenTubob)

        # Botones
        self.btnCerrar = tk.Label(self.ventana, text="Cerrar")
        self.btnCerrar.place(x=940, y=760)  
        Tooltip(self.btnCerrar, "Presione para salir del juego.")
        self.btnCerrar.bind("<Button-1>", self.destroy)

        # Eventos
        self.ventana.bind("<space>", self.moverCon)
        
        # After
        self.ventana.after(50, self.moverCondor)
        self.ventana.after(50, self.moverTubo)

        self.ventana.mainloop()
