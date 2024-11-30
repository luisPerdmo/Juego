import tkinter as tk
from tkinter import *

class VentanaPerder:

    def reiniciar(self):
        self.vistaJuego.reiniciarJuego()
        self.ventanaP.destroy()


    def __init__(self, ventanaPerder,  puntos, jugador, vistaJuego):
        self.ventanaP = tk.Toplevel(ventanaPerder)
        self.ventanaP.title("Juego terminado")
        self.ventanaP.geometry("300x200")
        self.ventanaP.resizable(0, 0)

        #iconos
        self.IconoReiniciar = tk.PhotoImage(file=r"Juego/Src/Reiniciar.png")

        #texto
        self.lblPerder = tk.Label(self.ventanaP, text="¡Has perdido!", font=("Impact", 20))
        self.lblPerder.place(relx=0.5, rely=0.3, anchor="center")

        # Mostrar el nombre del jugador y la puntuación
        self.lblJugador = tk.Label(self.ventanaP, text=f"Jugador: {jugador}", font=("Arial", 14))
        self.lblJugador.place(relx=0.5, rely=0.5, anchor="center")
        
        self.lblPuntos = tk.Label(self.ventanaP, text=f"Puntuación: {puntos}", font=("Arial", 14))
        self.lblPuntos.place(relx=0.5, rely=0.6, anchor="center")

        #Botones 
        self.btnReiniciar = tk.Button(self.ventanaP, image=self.IconoReiniciar, command=self.reiniciar)
        self.btnReiniciar.place(x=50, y=140)

        self.vistaJuego = vistaJuego

        self.ventanaP.mainloop()