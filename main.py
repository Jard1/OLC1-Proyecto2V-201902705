from tkinter import *
import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

rutaArchivo = ""
FilaCount = 1
ColumnaCount = 1


class Ctxt(Text): 

    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)
        count = IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#**********************************************INTERFAZ**************************************************************

#----------------------------Ventana ROOT-------------------------------------
root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(str(w-10)+"x"+str(h-175))
root.title("JPR Editor - 201902705 - Proyecto Compiladores 1")

#---------------------------------FRAME DE ABAJO--------------------------------------------
frameAbajo = Frame()
frameAbajo.pack(side = "bottom", fill = "x")
frameAbajo.config(bg = "orange", width = w, height = "150")
#---------------------Label archivo------------------------
lbFile = Label(frameAbajo, text = "Archivo: ", fg = "white", bg = "orange")
lbFile.config(font = ("Arial", 15))
lbFile.grid(row = 0, column = 0)

lbFilaValor = Label(frameAbajo, text= rutaArchivo, fg="white", bg= "orange")
lbFilaValor.config(font = ("Arial", 15))
lbFilaValor.grid(row = 0, column = 1)
##------------------Label numero fila----------------
lbFila = Label(frameAbajo, text = "\t\t\t\t Fila:", fg = "white", bg = "orange")
lbFila.config(font = ("Arial", 15))
lbFila.grid(row = 0, column = 2)

lbFilaValor = Label(frameAbajo, text= FilaCount, fg="white", bg= "orange")
lbFilaValor.config(font = ("Arial", 15))
lbFilaValor.grid(row = 0, column = 3)

##----------Label numero columna------------------
lbColumna = Label(frameAbajo, text = " | Columna:", fg = "white", bg = "orange")
lbColumna.config(font = ("Arial", 15))
lbColumna.grid(row = 0, column = 4)

lbColumnaValor = Label(frameAbajo, text= ColumnaCount, fg="white", bg= "orange")
lbColumnaValor.config(font = ("Arial", 15))
lbColumnaValor.grid(row = 0, column = 5)

#------------------------------------Frame principal----------------------------------------------------

FramePrincipal = Frame()
FramePrincipal.pack(fill = "both", expand = "yes")
FramePrincipal.config(bg = "#3c3c3c", width = "920", height = "550")

##-------------------Label titulo--------------------------
lbTitulo = Label(FramePrincipal, text = "JPR Editor", fg = "white", bg = "#3c3c3c")
lbTitulo.config(font = ("Arial", 20))
lbTitulo.grid(row = 0, column = 1)

##-------Label of Output------##
lblOutput = Label(FramePrincipal, text = "Debugger", fg = "white", bg= "#3c3c3c")
lblOutput.config(font = ("Arial", 14))
lblOutput.grid(row = 0, column = 2)

#----------------Botones----------------
btnDebugger = Button(FramePrincipal, text = "Siguiente", bg = "yellow", width = "15", height = "1")
btnDebugger.config(font = ("Arial", 16))
btnDebugger.grid(row = 1, column = 2)

btnAnalizer = Button(FramePrincipal, text = "Ejecutar", fg = "white", bg = "green", width = "15", height = "1")
btnAnalizer.config(font = ("Arial", 16))
btnAnalizer.grid(row = 0, column = 0)


##-------Bar Menú------##
barMenu = Menu(root)

##-------File Menu------##
fileMenu = Menu(barMenu, tearoff = 0)
fileMenu.add_command(label = "Nuevo archivo jpr")
fileMenu.add_command(label = "Abrir archivo jpr")
fileMenu.add_command(label = "Guardar...")
fileMenu.add_command(label = "Guardar Como...")
barMenu.add_cascade(label = "Archivo", menu= fileMenu)

##-------Reports Menu------##
reportMenu = Menu(barMenu, tearoff = 0)
reportMenu.add_command(label = "Tabla de simbolos")
reportMenu.add_command(label = "Arbol AST")
reportMenu.add_separator()
reportMenu.add_command(label = "Reporte de errores")
barMenu.add_cascade(label =  "Reportes", menu = reportMenu)

##-------Text Area for Input--------##
txtInput = scrolledtext.ScrolledText(FramePrincipal, wrap = WORD, width = 80, height = 35, bg = "#1e1e1e", fg="white")
txtInput.focus()
txtInput.grid(row = 2, column = 0, pady = 0, padx= 15)
txtInput.config(font = ("Arial", 13))
txtInput.bind("<Button>")
txtInput.bind("<KeyRelease>")
##-------Text Area for Output--------##
txtConsola = scrolledtext.ScrolledText(FramePrincipal, wrap = WORD, width = 70, height = 33, bg = "#1e1e1e", fg="white")
#txtConsola.bind("<Key>", lambda a: "break")
txtConsola.grid(row = 2, column = 2)

root.config(menu = barMenu)

def current_row(flag): 
    global FilaCount
    if flag: 
        FilaCount += 1
        lbFilaValor.config(text = FilaCount)
    else: 
        FilaCount -= 1
        lbFilaValor.config(text = FilaCount)

def current_column(flag): 
    global ColumnaCount
    if flag: 
        ColumnaCount += 1
        lbColumnaValor.config(text = ColumnaCount)
    else: 
        ColumnaCount -= 1
        lbColumnaValor.config(text = ColumnaCount)

def position(e): 
    if e.keysym == "Up": 
        current_row(False)
    elif e.keysym == "Down": 
        current_row(True)
    elif e.keysym == "Left": 
        current_column(False)
    elif e.keysym == "Right": 
        current_column(True)
    elif e.keysym == "Return": 
        current_row(True)

def positionPush(e = None): 
    global FilaCount
    global ColumnaCount
    #messagebox.showinfo("hola", e.keysym)

    positions = txtInput.index("current").split('.')
    lbFilaValor.config(text = positions[0])
    rowCount = int(positions[0])
    column = int(positions[1]) + 1
    ColumnaCount = column
    lbColumnaValor.config(text = column)


root.mainloop()