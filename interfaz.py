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
        # Crear un frame para los botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack()

        # Crear botones para manejar el arbol binario usando grid
        self.btnDibujar = tk.Button(frame_botones, text="Insertar nodo", command=self.dibujar_arbol)
        self.btnDibujar.grid(row=0, column=0, padx=10, pady=5)

        self.btnRecorrer = tk.Button(frame_botones, text="Recorrer arbol", command=self.recorrer_arbol)
        self.btnRecorrer.grid(row=0, column=1, padx=10, pady=5)

        self.btnBuscarNodo = tk.Button(frame_botones, text="Buscar nodo", command=self.buscar_nodo)
        self.btnBuscarNodo.grid(row=0, column=2, padx=10, pady=5)

        self.btnDeleteNodo = tk.Button(frame_botones, text="Eliminar nodo", command=self.eliminar_nodo)
        self.btnDeleteNodo.grid(row=0, column=3, padx=10, pady=5)
        
        self.btnCargarDatos = tk.Button(frame_botones, text="Cargar datos", command=self.cargar_datos)
        self.btnCargarDatos.grid(row=1, column=1, pady=5)

        self.btnReiniciar = tk.Button(frame_botones, text="Reiniciar arbol", command=self.reiniciar_arbol)
        self.btnReiniciar.grid(row=1, column=0, pady=10)
         
        
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
        msg = f"Dibujando árbol...\n"
        self.send_terminal(msg)
        
        # Dibuja el árbol en la ventana de Turtle
        self.arbol_app.dibujar_arbol(self.arbol_app.arbol.raiz, 0, 100, 0, 120)
        
        # Asegúrate de que Turtle actualice la ventana
        self.arbol_app.screen.update()

        
    def recorrer_arbol(self):
        orden = simpledialog.askstring("Input", "Ingrese orden (pre, in, post):")
        
        if orden in ["pre", "in", "post"]:
            resultado = self.arbol_app.recorrer_arbol(orden)
            if resultado:
                msg = f"Árbol recorrido en orden {orden}: {', '.join(map(str, resultado))}\n"
            else:
                msg = "No se pudo recorrer el árbol.\n"
        else:
            msg = "Orden inválido.\n"
        
        self.send_terminal(msg)
        
    def buscar_nodo(self):
        nodo = simpledialog.askinteger("Input", "Ingrese el dato del nodo a buscar:")
        #Invocar al método de busqueda del arbol binario
        #TODO
        msg = "" #Mensaje de respuesta de la busqueda
        
    def cargar_datos(self):
        while(True):
            opt = simpledialog.askstring("Input", "Escoga la opción que desea cargar\n1.- Letras\n2.- Nombres\n3.- Números")

            if opt == "1":
                msg = ("Cargando datos...")
                self.send_terminal(msg)
                break
            elif opt == "2":
                msg = ("Cargando datos...")
                self.send_terminal(msg)
                break
            elif opt == "3":
                msg = ("Cargando datos...")
                self.send_terminal(msg)
                break
            elif opt == None:
                msg = "Operación cancelada.\n"
                self.send_terminal(msg)
                break
            else:
                messagebox.showerror("Error", "Opción inválida")
        
    def send_terminal(self,msg):
        self.terminal.config(state=tk.NORMAL)  # Habilita la edición temporalmente
        self.terminal.insert(tk.END, msg)  # Inserta el mensaje al final
        self.terminal.config(state=tk.DISABLED)  # Deshabilita la edición nuevamente 
        
    def reiniciar_arbol(self):
        while (True):
            confirmacion = simpledialog.askstring("Input", "¿Está seguro que desea reiniciar el árbol? (s/n)")
            
            if confirmacion == "s" or confirmacion == "S":
                self.arbol_app.reiniciar_arbol()
                msg = "El árbol ha sido reiniciado.\nSolo la raíz permanece.\n"
                self.send_terminal(msg)
                break
            else:
                if confirmacion == "n" or confirmacion == "N":
                    msg = "Operación cancelada.\n"
                    self.send_terminal(msg)
                    break
                else:
                    messagebox.showerror("Error", "Opción inválida")
            
    def eliminar_nodo(self):
        dato = simpledialog.askinteger("Input", "Ingrese el dato del nodo a eliminar:")

        if dato is not None:
            self.arbol_app.eliminar_nodo(dato)
            msg = f"Nodo con dato {dato} eliminado del árbol.\n"
        else:
            msg = "Dato inválido.\n"

        self.send_terminal(msg)
   
class arbolBinarioApp:
    def __init__(self, raiz_dato):
        # Inicializa el árbol binario con un nodo raíz
        self.arbol = ArbolBinario(raiz_dato)
        self.screen_setup()
    
    def recorrer_arbol(self, orden):
        if orden == "pre":
            recorrido = self.arbol.pre_order(self.arbol.raiz)
        elif orden == "in":
            recorrido = self.arbol.in_order(self.arbol.raiz)
        elif orden == "post":
            recorrido = self.arbol.post_order(self.arbol.raiz)
        else:
            return None
        return recorrido
    
    def eliminar_nodo(self, dato):
        self.arbol.raiz = self.arbol.eliminar(self.arbol.raiz, dato)
        self.t.clear()  # Limpiar el dibujo anterior
        self.dibujar_arbol(self.arbol.raiz, 0, 100, 0, 120)  # Redibujar el árbol
        self.screen.update()
    
    def reiniciar_arbol(self):
        self.arbol.reiniciar()
        # Redibuja el árbol para mostrar solo la raíz
        self.t.clear()  # Limpia el dibujo de los nodos
        self.screen.bgcolor("black")
        self.screen.update()
     
        
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