import tkinter as tk
from tkinter import *

import tkinter as tk
from View.tablaPuntacion import ConsultarPuntaje

class VentanaPerder:

    def mostrarTabla(self, event):
        ConsultarPuntaje(self.vistaJuego.jugador)


    def reiniciar(self, event):
        self.vistaJuego.reiniciarJuego()
        self.ventanaP.destroy()


    def __init__(self, ventanaPerder,  puntos, jugador, vistaJuego):
        self.ventanaP = tk.Toplevel(ventanaPerder)
        self.ventanaP.title("Juego terminado")
        self.ventanaP.geometry("300x200")
        self.ventanaP.resizable(0, 0)

        #iconos
        self.IconoReiniciar = tk.PhotoImage(file=r"Juego/Src/Reiniciar.png")
        self.IconoClasificacion=tk.PhotoImage(file=r"Juego/Src/Clasificacion.png")

        #texto
        self.lblPerder = tk.Label(self.ventanaP, text="¡Has perdido!", font=("Impact", 20))
        self.lblPerder.place(relx=0.5, rely=0.3, anchor="center")

        # Mostrar el nombre del jugador y la puntuación
        self.lblJugador = tk.Label(self.ventanaP, text=f"Jugador: {jugador}", font=("Arial", 14))
        self.lblJugador.place(relx=0.5, rely=0.5, anchor="center")
        
        self.lblPuntos = tk.Label(self.ventanaP, text=f"Puntuación: {puntos}", font=("Arial", 14))
        self.lblPuntos.place(relx=0.5, rely=0.6, anchor="center")

        #Botones 
        self.btnReiniciar = tk.Button(self.ventanaP, image=self.IconoReiniciar)
        self.btnReiniciar.place(x=50, y=140)
        self.btnReiniciar.bind("<Button-1>", self.reiniciar)
        
        self.lblMostrarTabla = tk.Label(self.ventanaP, image=self.IconoClasificacion)
        self.lblMostrarTabla.place(relx=0.9, rely=0.05, anchor="ne")
        self.lblMostrarTabla.bind("<Button-1>", self.mostrarTabla)

        self.vistaJuego = vistaJuego

        self.ventanaP.mainloop()