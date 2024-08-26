import turtle
from arbolBinario import ArbolBinario
import tkinter as tk
from tkinter import simpledialog, messagebox



class controlUi:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Arbol Binario")
        
        self.arbol_app = arbolBinarioApp(50)
        
        
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
        # Solicita el dato para insertar
        dato = simpledialog.askinteger("Input", "Ingrese el dato del nodo:")
        
        if dato is None:
            msg = "Dato inválido\n"
            self.send_terminal(msg)
            return  # Termina la función si no se ingresa un dato válido
        
        # Inserta el nodo en el árbol
        self.arbol_app.arbol.agregar(dato)
        msg = f"Dato {dato} insertado en el árbol.\n"
        self.send_terminal(msg)
        
        # Muestra mensaje de dibujo
        msg = "Dibujando árbol...\n"
        self.send_terminal(msg)
        
        # Dibuja el árbol en la ventana de Turtle
        self.arbol_app.dibujar_arbol(self.arbol_app.arbol.raiz, 0, 100, 0, 120)
        
        # Asegúrate de que Turtle actualice la ventana
        self.arbol_app.screen.update()

        
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
        
class arbolBinarioApp:
    def __init__(self, raiz_dato):
        # Inicializa el árbol binario con un nodo raíz
        self.arbol = ArbolBinario(raiz_dato)
        self.screen_setup()
        
    def dibujar_nodo(self, nodo, x, y):
        self.t.ht()
        self.t.color("yellow")
        self.t.speed(0)
        self.t.pensize(2)
        self.t.penup()
        self.t.goto(x, y - 20)  # Posiciona para dibujar el círculo
        self.t.pendown()
        self.t.circle(20)  # Dibuja el círculo
        self.t.penup()
        self.t.goto(x, y - 10)  # Ajusta para escribir el dato
        self.t.write(nodo.dato, align="center", font=("Arial", 14, "bold"))
    
    def dibujar_linea(self, x1, y1, x2, y2):
        self.t.penup()
        self.t.goto(x1, y1 - 20)
        self.t.pendown()
        self.t.goto(x2, y2 + 20)
        self.t.penup()

    def dibujar_arbol(self, nodo, x, y, nivel, ancho):
        if nodo is not None:
            self.dibujar_nodo(nodo, x, y)  # Asegúrate de pasar coordenadas x, y numéricas
            if nodo.izquierda is not None:
                x_izq = x - (ancho * 2) / (2 ** nivel)
                y_izq = y - 75
                self.dibujar_linea(x, y, x_izq, y_izq)
                self.dibujar_arbol(nodo.izquierda, x_izq, y_izq, nivel + 1, ancho)
            if nodo.derecha is not None:
                x_der = x + (ancho * 2) / (2 ** nivel)
                y_der = y - 75
                self.dibujar_linea(x, y, x_der, y_der)
                self.dibujar_arbol(nodo.derecha, x_der, y_der, nivel + 1, ancho)
                
    def screen_setup(self):
        # Inicializa la ventana de turtle
        self.screen = turtle.Screen()  # Asigna a self.screen
        self.screen.title("Árbol Binario")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.t = turtle.Turtle()
        
if __name__ == '__main__':
    root = tk.Tk()
    app = controlUi(root)
    root.mainloop()