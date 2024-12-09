import tkinter as tk    
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class ConsultarPuntaje():

    def __init__(self, usuario):
        self.ventana= tk.Toplevel()
        self.ventana.config(width=600,height=100)
        self.ventana.title("Tabla de Jugadores")

        self.usuario=usuario

        self.lbltitulo=tk.Label(self.ventana,text="Clasificacion")
        self.lbltitulo.pack()

        self.tabla=ttk.Treeview(self.ventana)
        self.tabla["columns"]=["ID","Nombre","Puntaje"]
        self.tabla.heading("#1",text="ID", anchor="center")
        self.tabla.heading("#2",text="Nombre", anchor="center")
        self.tabla.heading("#3",text="Puntaje", anchor="center")
        

        self.listaUsuario=usuario.consultarTabla()

        for usuario in self.listaUsuario:
            self.tabla.insert("","end",values=[usuario[0],usuario[1],usuario[3]])

        self.tabla["show"]="headings"
        self.tabla.column("#1",width=50)  
        self.tabla.column("#2",width=100)
        self.tabla.column("#3",width=100)

        self.scorllbar=ttk.Scrollbar(self.ventana,orient="vertical",command=self.tabla.yview)
        self.tabla.config(yscrollcommand=self.scorllbar.set)
        self.scorllbar.pack(side="right",fill="y")  

        self.tabla.pack(fill="both",expand=True)

        self.botones=tk.Frame(self.ventana)
        self.botones.config(width=600,height=100)
        self.botones.pack(fill="both", expand=True)

        self.ventana.mainloop()