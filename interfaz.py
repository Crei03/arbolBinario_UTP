import turtle
import tkinter as tk
from tkinter import simpledialog, messagebox


class controlUi:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Arbol Binario")
        
        # Crear el widget Text como terminal
        self.terminal = tk.Text(self.root, height=10, width=50, state=tk.DISABLED)
        self.terminal.pack(pady=10)
        
        # Crear botones para manejar el arbol binario
        self.btnDibujar = tk.Button(self.root, text="Insertar nodo", command=self.dibujar_arbol)
        self.btnDibujar.pack(side= tk.LEFT, padx=10 , pady=10)
        
        self.btnRecorrer = tk.Button(self.root, text="Recorrer arbol", command=self.recorrer_arbol)
        self.btnRecorrer.pack(side= tk.LEFT, padx=10 , pady=10)
        
        self.btnBuscarNodo = tk.Button(self.root, text="Buscar nodo", command=self.buscar_nodo)
        self.btnBuscarNodo.pack(side= tk.LEFT, padx=10 , pady=10)
        
        self.btnCargarDatos = tk.Button(self.root, text="Cargar datos", command=self.cargar_datos)
        self.btnCargarDatos.pack(side= tk.LEFT, padx=10 , pady=10)
        
        
    def dibujar_arbol(self):
        msg = "Dibujando arbol...\n"
        self.send_terminal(msg)
        
    def recorrer_arbol(self):
        opt = simpledialog.askstring("Input", "Ingrese orden (pre, in, post):")
        
        if opt == "pre":
            msg = "Recorriendo arbol en preorden...\n"
        elif opt == "in":
            msg = "Recorriendo arbol en inorden...\n"
        elif opt == "post":
            msg = "Recorriendo arbol en postorden...\n"
        else:
            msg = "Opción inválida\n"
        
        self.send_terminal(msg)
        
    def buscar_nodo(self):
        nodo = simpledialog.askinteger("Input", "Ingrese el dato del nodo a buscar:")
        #Invocar al método de busqueda del arbol binario
        
        msg = "" #Mensaje de respuesta de la busqueda
        
    def cargar_datos(self):
        opt = simpledialog.askstring("Input", "Escoga la opción que desea cargar\n1.- Letras\n2.- Nombres\n3.- Números")
        
        #TODO hacer validación de la opción seleccionada
    
    
    def send_terminal(self,msg):
        self.terminal.config(state=tk.NORMAL)  # Habilita la edición temporalmente
        self.terminal.insert(tk.END, msg)  # Inserta el mensaje al final
        self.terminal.config(state=tk.DISABLED)  # Deshabilita la edición nuevamente 


if __name__ == '__main__':
    root = tk.Tk()
    app = controlUi(root)
    root.mainloop()