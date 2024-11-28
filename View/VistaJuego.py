import tkinter as tk
from tkinter import *
import random

class VistaJuego:

    def destroy(self, event):
        self.ventana.destroy()

    def __init__(self, loggin, jugador):  
        self.ventana = tk.Toplevel(loggin)  
        self.ventana.title("Juego Principal")
        self.ventana.geometry("800x600")
        
        self.lblJugador = tk.Label(self.ventana, text=f"Jugador: {jugador.nombre}")
        self.lblJugador.place(x=20, y=20)  

        self.canvas = tk.Canvas(self.ventana, width=760, height=400, bg="white")
        self.canvas.place(x=20, y=60)  

        self.btnCerrar = tk.Button(self.ventana, text="Cerrar")
        self.btnCerrar.place(x=700, y=550)  
        self.btnCerrar.bind("<Button-1>",self.destroy)

        self.ventana.mainloop() 