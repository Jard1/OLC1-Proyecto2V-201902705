
class graficadorReportes:
    
    def __init__(self):
        self.contenidoTablaErrores = ""

    def graficarTablaErrores(self, listaErrores):
        
        self.contenidoTablaErrores = "<!DOCTYPE html>\n<html>\n<head>\n<style>table {font-family: arial, sans-serif;width: 100%;}\n"
        self.contenidoTablaErrores += "td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}\ntr:nth-child(even){background-color: #ffd6a5;}"
        self.contenidoTablaErrores += "tr:nth-child(odd) {background-color: #ffadad;}\n</style>\n</head>"
        self.contenidoTablaErrores += "<body>\n<h2>Reporte Errores</h2>\n"
        self.contenidoTablaErrores += "<table>\n<tr><th># Error</th><th>Tipo de error</th><th>Descripción</th><th>Linea</th><th>Columna</th></tr>"

        cont =0
        for error in listaErrores:
            cont+=1
            self.contenidoTablaErrores += "<tr><th>"+str(cont)+"</th><th>"+str(error.getTipo())+"</th><th>"+str(error.getDescripcion())+"</th><th>"+str(error.getFila())+"</th><th>"+str(error.getColumna())+"</th></tr>"

        self.contenidoTablaErrores += "</table></body></html>"
        #print(self.contenidoTablaErrores)
        self.generarHtmlErrores()

    def generarHtmlErrores(self):
        archivo = open('ReporteErrores.html','w')
        archivo.write(self.contenidoTablaErrores)
        archivo.close()