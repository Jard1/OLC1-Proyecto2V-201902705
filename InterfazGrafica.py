from tkinter import *
from tkinter import ttk,scrolledtext,filedialog

from controladorInterfaz import controladorInterfaz

class InterfazGrafica():

    def __init__(self, root, titulo, tamano):

        root.config(bg="#3c3c3c")
        self.rutaArchivo = ""
        root.title(titulo)
        root.geometry(tamano)
        self.generarInterfaz(root)
        self.controlador = controladorInterfaz(self.txtInput,self.txtConsola,self.scroll_editor,self.text_lineas_editor, self.lbArchivoValor)

    def generarInterfaz(self, root):

        #--------------------------------------Menu de opciones------------------------------------

        #-------------Menu archivo------------------------
        barMenu = Menu(root)
        fileMenu = Menu(barMenu, tearoff = 0)
        fileMenu.add_command(label = "Nuevo...", command=self.nuevo)
        fileMenu.add_command(label = "Abrir...", command = self.abrirArchivo)
        fileMenu.add_command(label = "Guardar...", command = self.guardar )
        fileMenu.add_command(label = "Guardar Como...", command=self.guardarComo)
        barMenu.add_cascade(label = "Archivo", menu= fileMenu)

        #--------------Menu opciones-----------------------
        reportMenu = Menu(barMenu, tearoff = 0)
        reportMenu.add_command(label = "Tabla de simbolos")
        reportMenu.add_command(label = "Arbol AST")
        reportMenu.add_separator()
        reportMenu.add_command(label = "Reporte de errores", command=self.abrirReporteErrores)
        barMenu.add_cascade(label =  "Reportes", menu = reportMenu)
        root.config(menu = barMenu)

        #--------------------------------------------------Frame de arriba--------------------------------------------------

        frameArriba = Frame()
        frameArriba.pack(side = "top" , fill="x")
        frameArriba.config(bg = "#3c3c3c",  height = "50")

        btnAnalizer = Button(frameArriba, text = "Ejecutar", fg = "white", bg = "green", width = "15", height = "1", command=self.ejecutar)
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

        #-----------------------------------------------------------INPUT ----------------------------------------------------------

        self.scroll_editor = Scrollbar(FrameInput,orient=VERTICAL,command=self.accion_scroll)
        self.scroll_editor_horizontal = Scrollbar(FrameInput,orient=HORIZONTAL,command=self.accion_scroll_horizontal)

        self.text_lineas_editor = Text(FrameInput,bg='white',width=3, height =35)
        #self.controlador.llenar_lineas(self.text_lineas_editor,0)
        self.text_lineas_editor.grid(row = 0, column = 0)

        self.txtInput = scrolledtext.ScrolledText(FrameInput, wrap=NONE, undo=True, width = 80, height = 35, bg = "#1e1e1e", fg="white", insertbackground='white')
        #self.txtInput.config(xscrollcommand=self.scroll_editor_horizontal.set)

        #inputInicial = "#ejemplo de comentario\nmain() {\n \tvar a = 0; \n\tif(a==5-5){\n\t\tprint(\" el valor de a es: \" + a);\n\t}\n}"
        #self.txtInput.insert(INSERT, inputInicial)
        #analisis_formato_entrada()
        #actualizar_lineas(None)

        self.text_lineas_editor['yscrollcommand'] = self.scroll_editor.set
        self.txtInput['yscrollcommand'] = self.scroll_editor.set
        self.txtInput['xscrollcommand'] = self.scroll_editor_horizontal.set

        self.scroll_editor.grid(row=0,column=2,sticky=N+S)
        self.scroll_editor_horizontal.grid(row=2,column=0,columnspan=3,sticky=W+E)

        self.txtInput.bind('<Any-KeyPress>',self.actualizar_lineas)
        self.txtInput.bind('<Any-KeyRelease>',self.actualizar_lineas_texto)
        self.txtInput.bind('<MouseWheel>',self.sincronizar_lineas)

        self.txtInput.tag_config('reservada',foreground='blue')
        self.txtInput.tag_config('cadena',foreground='orange')
        self.txtInput.tag_config('numero',foreground='MediumPurple1')
        self.txtInput.tag_config('comentario',foreground='gray')
        self.txtInput.tag_config('normal',foreground='white')


        self.txtInput.grid(row = 0, column = 1) #pady = 0, padx= 0

        #-----------------------------------------------------OUTPUT---------------------------------------------------------

        FrameConsola = Frame(FramePrincipal)
        FrameConsola.config(bg = "#3c3c3c", width = 80, height = 35)
        FrameConsola.grid(row = 0, column = 2)

        scroll_consola_x = Scrollbar(FrameConsola, orient=HORIZONTAL)
        scroll_consola_x.grid(row=3, column=2, sticky=N+S+E+W)

        scroll_consola_y = Scrollbar(FrameConsola)
        scroll_consola_y.grid(row=0, column=3, sticky=N+S+E+W)

        self.txtConsola = Text(FrameConsola, bg = "#1e1e1e", fg="#00BB2D", insertbackground='white', width = 80, height = 35)
        self.txtConsola.grid(row=0,column=2)

        #-----------------------------------------------Frame Abajo-------------------------------------------------------------

        frameAbajo = Frame()
        frameAbajo.pack(side = "bottom" ,fill="x",)
        frameAbajo.config(bg = "orange",  height = "55")

        #-----------------------Ruta archivo--------------------------------------

        lbFile = Label(frameAbajo, text = "Archivo: ", fg = "white", bg = "orange")
        lbFile.config(font = ("Arial", 15))
        lbFile.grid(row = 0, column = 0)

        self.lbArchivoValor = Label(frameAbajo, text= self.rutaArchivo, fg="white", bg= "orange")
        self.lbArchivoValor.config(font = ("Arial", 15))
        self.lbArchivoValor.grid(row = 0, column = 1)

        ##----------------------Label numero fila----------------------------------
        lbFila = Label(frameAbajo, text = "\t\t\t  Fila:", fg = "white", bg = "orange")
        lbFila.config(font = ("Arial", 15))
        lbFila.grid(row = 0, column = 2)

        lbFilaValor = Label(frameAbajo, text= "FilaCount", fg="white", bg= "orange")
        lbFilaValor.config(font = ("Arial", 15))
        lbFilaValor.grid(row = 0, column = 3)

        ##-------------------------Label numero columna------------------
        lbColumna = Label(frameAbajo, text = " | Columna:", fg = "white", bg = "orange")
        lbColumna.config(font = ("Arial", 15))
        lbColumna.grid(row = 0, column = 4)

        lbColumnaValor = Label(frameAbajo, text= "ColumnaCount", fg="white", bg= "orange")
        lbColumnaValor.config(font = ("Arial", 15))
        lbColumnaValor.grid(row = 0, column = 5)


    def nuevo(self):
        self.controlador.nuevo()
    def abrirArchivo(self):
        self.rutaArchivo = self.controlador.abrirArchivo()
        #self.controlador.actualizar_texto()
        #self.actualizar_lineas(0)
        self.actualizar_lineas_texto()

    def abrirReporteErrores(self):
        self.controlador.abrirReporteErrores()
    def guardarComo(self):
        self.controlador.guardarComo()
    def guardar(self):
        self.controlador.guardar()
    def ejecutar(self):
        self.controlador.ejecutar()
    #--------------------------------------------------------------------------------

    def accion_scroll(self, *L):
        operacion = L[0]
        lineas = L[1]
        if operacion == 'scroll':
            unidades = L[2]
            self.txtInput.yview_scroll(lineas,unidades)
            self.text_lineas_editor.yview_scroll(lineas,unidades)
        elif operacion == 'moveto':
            self.txtInput.yview_moveto(lineas)
            self.text_lineas_editor.yview_moveto(lineas)
    def accion_scroll_horizontal(self, *L):
        operacion = L[0]
        lineas = L[1]
        if operacion == 'scroll':
            unidades = L[2]
            self.txtInput.xview_scroll(lineas,unidades)
        elif operacion == 'moveto':
            self.txtInput.xview_moveto(lineas)

    def actualizar_lineas_texto(self, e=None):
        self.controlador.actualizar_texto()
        self.texto_actual = self.txtInput.get('1.0','end')
        lineas = self.texto_actual.count('\n')#,None)
        #self.llenar_lineas(self.text_lineas_editor,lineas)
        self.controlador.llenar_lineas(self.text_lineas_editor,lineas)

    def actualizar_lineas(self, e=None):
        self.texto_actual = self.txtInput.get('1.0','end')
        lineas = self.texto_actual.count('\n')#,None)
        #self.llenar_lineas(self.lineasCodigo,lineas)
        self.controlador.llenar_lineas(self.text_lineas_editor,0)
        
    def sincronizar_lineas(self, e=None):
        self.text_lineas_editor.yview_moveto(self.scroll_editor.get()[0])
