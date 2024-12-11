import tkinter as tk
from tkinter import *
import tkinter as tk
from Tooltip import Tooltip

from tkinter import messagebox

from View.tablaPuntacion import ConsultarPuntaje

class VentanaPerder:

    def mostrarAyuda(self, event):
        texto_ayuda = (
        "Atajos Del Juego:\n"
        "- Presione 'Escape' para reiniciar.\n"
        "- Presiona 'space' para mostar la tabla de puntaje.\n"
        "- Presione 'F1' para mostrar este ayuda.\n" 
        )
        messagebox.showinfo("Ayuda", texto_ayuda)

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
        self.ventanaP.focus_set()

        #iconos
        self.IconoReiniciar = tk.PhotoImage(file=r"Juego/Src/Reiniciar.png")
        self.IconoClasificacion = tk.PhotoImage(file=r"Juego/Src/Clasificacion.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Juego\Src\Ayuda2.png (1).png")
                 
        #texto
        self.lblPerder = tk.Label(self.ventanaP, text="¡Has Perdido!", font=("Impact", 20))
        self.lblPerder.place(relx=0.5, rely=0.3, anchor="center")

        # Mostrar el nombre del jugador y la puntuación
        self.lblJugador = tk.Label(self.ventanaP, text=f"Jugador: {jugador}", font=("Arial", 14))
        self.lblJugador.place(relx=0.5, rely=0.5, anchor="center")
        
        self.lblPuntos = tk.Label(self.ventanaP, text=f"Puntuación: {puntos}", font=("Arial", 14))
        self.lblPuntos.place(relx=0.5, rely=0.6, anchor="center")

        #Botones 
        self.btnReiniciar = tk.Button(self.ventanaP, image=self.IconoReiniciar)
        self.btnReiniciar.place(x=50, y=140)
        Tooltip(self.btnReiniciar, "Haz clic para reiniciar el juego.")
        self.btnReiniciar.bind("<Button-1>", self.reiniciar)
        
        self.lblMostrarTabla = tk.Label(self.ventanaP, image=self.IconoClasificacion)
        self.lblMostrarTabla.place(relx=0.9, rely=0.05, anchor="ne")
        Tooltip(self.lblMostrarTabla, "Haz clic para ver la tabla de clasificación.")
        self.lblMostrarTabla.bind("<Button-1>", self.mostrarTabla)

        self.btnAyuda = tk.Label(self.ventanaP, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.85, rely=0.8, anchor="center")
        Tooltip(self.btnAyuda, "Presione para ver las atajos del juego.")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)


        self.vistaJuego = vistaJuego

        # Atajos
        self.ventanaP.bind("<Escape>", self.reiniciar)
        self.ventanaP.bind("<space>", self.mostrarTabla)
        self.ventanaP.bind("<F1>", self.mostrarAyuda)

        self.ventanaP.mainloop()