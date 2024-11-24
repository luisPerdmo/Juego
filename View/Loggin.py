import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Loggin():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0, 0)
        self.ventana.config(width=550, height=350)
        self.ventana.title("Inicio de sesion")


        self.ventana.mainloop()