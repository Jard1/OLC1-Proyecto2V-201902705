import os
import tkinter as tk
from tkinter import *
from tkinter import ttk,scrolledtext,filedialog

import analisisTokensEntrada as analisisTokensEntrada
from Analizador.gramatica import ejecutarAnalisis
from graficadorReportes import graficadorReportes

class controladorInterfaz():

    def __init__(self, txtInput,txtConsola, scroll_editor, lineasCodigo, lbArchivoValor):

        self.txtInput = txtInput
        self.scroll_editor = scroll_editor
        self.lineasCodigo = lineasCodigo
        self.lbArchivoValor = lbArchivoValor
        self.txtConsola = txtConsola

    def llenar_lineas(self, text, lineas):
        
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
        text.yview_moveto(self.scroll_editor.get()[0])


    def actualizar_texto(self):
        ultima_posicion = self.txtInput.index('insert')
        ultima_posicion_scroll = self.scroll_editor.get()[0]
        texto_actual = self.txtInput.get('1.0','end')
        saltos = texto_actual.count('\n')
        self.txtInput.delete('1.0','end')
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
                self.txtInput.insert(str(token_info[1]) + '.' + str(token_info[2]), token_info[0], token_info[3])
        self.txtInput.mark_set('insert', ultima_posicion)
        self.txtInput.yview_moveto(ultima_posicion_scroll)



    def abrirArchivo(self): 
        #global rutaArchivo
        rutaArchivo = filedialog.askopenfilename(filetypes=(("Archivos JPR", "*.jpr*"),("All files", "*.*") ))

        if rutaArchivo != "":
            fileText = open(rutaArchivo)
            
            text = fileText.read()
            self.txtInput.delete(1.0, END)
            self.txtInput.insert(INSERT, text)
            fileText.close()

            self.lbArchivoValor.config(text=rutaArchivo)

        return rutaArchivo
        #actualizar_lineas(None)

    def guardarComo(self):    
        #global rutaArchivo

        save = filedialog.asksaveasfile(filetypes=(("Archivos JPR", "*.jpr*"),("All files", "*.*") ))
        if save != None:
            with open(save.name, "w+") as fileSave:
                fileSave.write(self.txtInput.get(1.0, END))
            fileInput = save.name

    def guardar(self, rutaArchivo):
        #global rutaArchivo
        if rutaArchivo == "": 
            #si no hay ninguna ruta, es porque es un archivo nuevo
            guardarComo()
        else: 
            with open(rutaArchivo.name, "w") as fileSave: 
                fileSave.write(self.txtInput.get(1.0, END))
    def nuevo(self): 
        self.txtInput.delete(1.0, END)
        rutaArchivo=""
        self.lbArchivoValor.config(text=rutaArchivo)

    def ejecutar(self):
        graficador = graficadorReportes()

        self.txtConsola.delete(1.0, END)
        textoEntrada = self.txtInput.get(1.0,END)

        salida,errores = ejecutarAnalisis(textoEntrada)
        self.txtConsola.insert(INSERT, salida)
        
        graficador.graficarTablaErrores(errores)

    def abrirReporteErrores(self):
        os.system('ReporteErrores.html')

    def abrirAST(self):
        os.system('arbolAST.svg')
