import tkinter as tk
from tkinter.simpledialog import Dialog

class DebuggerDialog(Dialog):
    def __init__(self, linea):
        self.linea = linea
        Dialog.__init__(self, None, 'Debugger')#,bg='#3c3c3c')
    def destroy(self):
        Dialog.destroy(self)
    def body(self, master):
        master.config(bg='#3c3c3c')
        master.pack(expand=tk.YES)
        w = tk.Label(master, text='Linea actual: '+str(self.linea), justify=tk.LEFT,bg='#3c3c3c',fg='white')
        w.grid(row=0, padx=5, sticky=tk.W)
        return w
    def buttonbox(self):
        box = tk.Frame(self)
        w = tk.Button(box, text="Siguiente", width=18, command=self.ok, default=tk.ACTIVE,bg='yellow')
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="Salir", width=10, command=self.cancel,bg='red',fg='white')
        w.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.config(bg='#3c3c3c')
        box.pack(expand=tk.YES)
    def validate(self):
        self.result = True
        return 1
    def ok(self, event=None):
        self.result = True
        self.destroy()
    def cancel(self,event=None):
        self.result = False
        self.destroy()
