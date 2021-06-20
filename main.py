import os
import tkinter as tk
from tkinter import *
from tkinter import ttk,scrolledtext,filedialog
import analisisTokensEntrada as analisisTokensEntrada
from Analizador.gramatica import ejecutarAnalisis
from graficadorReportes import graficadorReportes
 
#**********************************************************Funcionalidad************************************************************
 
def analisis_formato_entrada():
    
    ultima_posicion = txtInput.index('insert')
    ultima_posicion_scroll = scroll_editor.get()[0]
    texto_actual = txtInput.get('1.0','end')
    saltos = texto_actual.count('\n',None)
    
    txtInput.delete('1.0','end')
    analisisTokensEntrada.entrada = texto_actual
    analisisTokensEntrada.lexer.input(texto_actual)
    contador_saltos = 0
    for t in analisisTokensEntrada.lexer:
        token_info = analisisTokensEntrada.ultimo_token
        if token_info[0] == '\n':
            contador_saltos = contador_saltos + 1
        if t.type == 'COMENTARIOMULTI':
            contador_saltos = contador_saltos + t.value.count('\n')
        if contador_saltos < saltos:
            txtInput.insert(str(token_info[1]) + '.' + str(token_info[2]), token_info[0], token_info[3])
    txtInput.mark_set('insert', ultima_posicion)
    txtInput.yview_moveto(ultima_posicion_scroll)

FilaCount = 1
ColumnaCount = 1
rutaArchivo = ""
def accion_scroll(*L):
    operacion = L[0]
    lineas = L[1]
    if operacion == 'scroll':
        unidades = L[2]
        txtInput.yview_scroll(lineas,unidades)
        lineasCodigo.yview_scroll(lineas,unidades)
    elif operacion == 'moveto':
        txtInput.yview_moveto(lineas)
        lineasCodigo.yview_moveto(lineas)

def accion_scroll_console(*L):
    operacion = L[0]
    lineas = L[1]
    if operacion == 'scroll':
        unidades = L[2]
        #txtInput.yview_scroll(lineas,unidades)
        #lineasCodigo.yview_scroll(lineas,unidades)
    elif operacion == 'moveto':
        None
        #txtInput.yview_moveto(lineas)
        #lineasCodigo.yview_moveto(lineas)
def accion_scroll_horizontal( *L):
    operacion = L[0]
    lineas = L[1]
    if operacion == 'scroll':
        unidades = L[2]
        txtInput.xview_scroll(lineas,unidades)
    elif operacion == 'moveto':
        txtInput.xview_moveto(lineas)

def llenar_lineas( text, lineas):
    
    numeros = ''
    if lineas > 999:
        text['width'] = len(str(lineas))
    for n in range(1,lineas+1):
        if n != lineas:
            numeros = numeros + str(n) + '\n'
        else:
            numeros = numeros + str(n)
    if lineas == 0:
        text.delete('1.0','end')
        text.insert('1.0','1')
    else:
        text.delete('1.0','end')
        text.insert('1.0',numeros)
    text.yview_moveto(scroll_editor.get()[0])

def actualizar_lineas_texto(event):
    analisis_formato_entrada()
    texto_actual = txtInput.get('1.0','end')
    lineas = texto_actual.count('\n',None)
    llenar_lineas(lineasCodigo,lineas)

def actualizar_lineas(event):
    texto_actual = txtInput.get('1.0','end')
    lineas = texto_actual.count('\n',None)
    llenar_lineas(lineasCodigo,lineas)

def sincronizar_lineas(event):
    lineasCodigo.yview_moveto(scroll_editor.get()[0])

def abrirArchivo(): 
    global rutaArchivo
    rutaArchivo = filedialog.askopenfilename(filetypes=(("Archivos JPR", "*.jpr*"),("All files", "*.*") ))

    if rutaArchivo != "":
        fileText = open(rutaArchivo)
        
        text = fileText.read()
        txtInput.delete(1.0, END)
        txtInput.insert(INSERT, text)
        fileText.close()

        lbArchivoValor.config(text=rutaArchivo)
        analisis_formato_entrada()

def guardarComo():    
    global rutaArchivo

    save = filedialog.asksaveasfile(filetypes=(("Archivos JPR", "*.jpr*"),("All files", "*.*") ))
    if save != None:
        with open(save.name, "w+") as fileSave:
            fileSave.write(txtInput.get(1.0, END))
        fileInput = save.name

def guardar():
    global rutaArchivo
    if rutaArchivo == "": 
        #si no hay ninguna ruta, es porque es un archivo nuevo
        guardarComo()
    else: 
        with open(rutaArchivo.name, "w") as fileSave: 
            fileSave.write(txtInput.get(1.0, END))
def nuevo(): 
    txtInput.delete(1.0, END)
    rutaArchivo=""
    lbArchivoValor.config(text=rutaArchivo)

def ejecutar():
    graficador = graficadorReportes()

    txtConsola.delete(1.0, END)
    textoEntrada = txtInput.get(1.0,END)

    salida,errores = ejecutarAnalisis(textoEntrada)
    txtConsola.insert(INSERT, salida)
    
    graficador.graficarTablaErrores(errores)

def abrirReporteErrores():
    os.system('ReporteErrores.html')

#******************************************************INTERFAZ GRAFICA********************************************************************

#----------------------------Ventana ROOT-------------------------------------
root = Tk()
root.config(bg="#3c3c3c")
root.geometry("1500x675")
root.title("JPR Editor - 201902705 - Proyecto Compiladores 1")

#--------------------------------------Menu de opciones------------------------------------

#-------------Menu archivo------------------------
barMenu = Menu(root)
fileMenu = Menu(barMenu, tearoff = 0)
fileMenu.add_command(label = "Nuevo...", command=nuevo)
fileMenu.add_command(label = "Abrir...", command = abrirArchivo)
fileMenu.add_command(label = "Guardar...", command = guardar )
fileMenu.add_command(label = "Guardar Como...", command=guardarComo)
barMenu.add_cascade(label = "Archivo", menu= fileMenu)

#--------------Menu opciones-----------------------
reportMenu = Menu(barMenu, tearoff = 0)
reportMenu.add_command(label = "Tabla de simbolos")
reportMenu.add_command(label = "Arbol AST")
reportMenu.add_separator()
reportMenu.add_command(label = "Reporte de errores", command=abrirReporteErrores)
barMenu.add_cascade(label =  "Reportes", menu = reportMenu)
root.config(menu = barMenu)

#--------------------------------------------------Frame de arriba--------------------------------------------------

frameArriba = Frame()
frameArriba.pack(side = "top" , fill="x")
frameArriba.config(bg = "#3c3c3c",  height = "50")

btnAnalizer = Button(frameArriba, text = "Ejecutar", fg = "white", bg = "green", width = "15", height = "1", command=ejecutar)
btnAnalizer.config(font = ("Arial", 16))
btnAnalizer.grid(row = 0, column = 0, padx= 230, pady=10)

#---------------Debugger-------------------

lblDebugger = Label(frameArriba, text = "Debugger:", fg = "white", bg= "#3c3c3c")
lblDebugger.config(font = ("Arial", 14))
lblDebugger.grid(row = 0, column = 2, padx= 50)

btnDebugger = Button(frameArriba, text = "Siguiente", bg = "yellow", width = "15", height = "1" )
btnDebugger.config(font = ("Arial", 16))
btnDebugger.grid(row = 0, column = 3)



#-------------------------------------------------Frame principal----------------------------------------------------

FramePrincipal = Frame()
FramePrincipal.pack()
FramePrincipal.config(bg = "#3c3c3c")

FrameInput = Frame(FramePrincipal)
FrameInput.config(bg = "#3c3c3c", width = 80, height = 35)
FrameInput.grid(row = 0, column = 0)

#------------------------------------------------INPUT ----------------------------------------------------------

scroll_editor = Scrollbar(FrameInput,orient=tk.VERTICAL,command=accion_scroll)
scroll_editor_horizontal = Scrollbar(FrameInput,orient=tk.HORIZONTAL,command=accion_scroll_horizontal)


lineasCodigo = tk.Text(FrameInput,bg='white',width=3, height =35)
llenar_lineas(lineasCodigo,0)
lineasCodigo.grid(row = 0, column = 0)

txtInput = tk.Text(FrameInput, bg = "#1e1e1e", fg="white", insertbackground='white', width = 80, height = 35)#width = 80, height = 35,

inputInicial = "#ejemplo de comentario\nmain() {\n \tvar a = 0; \n\tif(a==5-5){\n\t\tprint(\" el valor de a es: \" + a);\n\t}\n}"
txtInput.insert(INSERT, inputInicial)
analisis_formato_entrada()

lineasCodigo['yscrollcommand'] = scroll_editor.set
txtInput['yscrollcommand'] = scroll_editor.set
txtInput['xscrollcommand'] = scroll_editor_horizontal.set

txtInput.tag_config('reservada',foreground='blue')
txtInput.tag_config('cadena',foreground='orange')
txtInput.tag_config('numero',foreground='MediumPurple1')
txtInput.tag_config('comentario',foreground='gray')
txtInput.tag_config('normal',foreground='white')

scroll_editor.grid(row=0,column=2,sticky=tk.N+tk.S)
scroll_editor_horizontal.grid(row=2,column=0,columnspan=3,sticky=tk.W+tk.E)

txtInput.bind('<Any-KeyPress>',actualizar_lineas)
txtInput.bind('<Any-KeyRelease>',actualizar_lineas_texto)
txtInput.bind('<MouseWheel>',sincronizar_lineas)
txtInput.grid(row = 0, column = 1) #pady = 0, padx= 0

#-----------------------------------------------------OUTPUT---------------------------------------------------------

FrameConsola = Frame(FramePrincipal)
FrameConsola.config(bg = "#3c3c3c", width = 80, height = 35)
FrameConsola.grid(row = 0, column = 2)

scroll_consola_x = Scrollbar(FrameConsola, orient=HORIZONTAL)
scroll_consola_x.grid(row=3, column=2, sticky=N+S+E+W)

scroll_consola_y = Scrollbar(FrameConsola)
scroll_consola_y.grid(row=0, column=3, sticky=tk.N+tk.S+tk.E+tk.W)

txtConsola = tk.Text(FrameConsola, bg = "#1e1e1e", fg="#00BB2D", insertbackground='white', width = 80, height = 35, yscrollcommand=scroll_consola_y.set, xscrollcommand=scroll_consola_x.set)
txtConsola.grid(row=0,column=2)



#-----------------------------------------------Frame Abajo-------------------------------------------------------------

frameAbajo = Frame()
frameAbajo.pack(side = "bottom" ,fill="x",)
frameAbajo.config(bg = "orange",  height = "55")

#-----------------------Ruta archivo--------------------------------------

lbFile = Label(frameAbajo, text = "Archivo: ", fg = "white", bg = "orange")
lbFile.config(font = ("Arial", 15))
lbFile.grid(row = 0, column = 0)

lbArchivoValor = Label(frameAbajo, text= rutaArchivo, fg="white", bg= "orange")
lbArchivoValor.config(font = ("Arial", 15))
lbArchivoValor.grid(row = 0, column = 1)

##----------------------Label numero fila----------------------------------
lbFila = Label(frameAbajo, text = "\t\t\t  Fila:", fg = "white", bg = "orange")
lbFila.config(font = ("Arial", 15))
lbFila.grid(row = 0, column = 2)

lbFilaValor = Label(frameAbajo, text= FilaCount, fg="white", bg= "orange")
lbFilaValor.config(font = ("Arial", 15))
lbFilaValor.grid(row = 0, column = 3)

##-------------------------Label numero columna------------------
lbColumna = Label(frameAbajo, text = " | Columna:", fg = "white", bg = "orange")
lbColumna.config(font = ("Arial", 15))
lbColumna.grid(row = 0, column = 4)

lbColumnaValor = Label(frameAbajo, text= ColumnaCount, fg="white", bg= "orange")
lbColumnaValor.config(font = ("Arial", 15))
lbColumnaValor.grid(row = 0, column = 5)



root.mainloop()

