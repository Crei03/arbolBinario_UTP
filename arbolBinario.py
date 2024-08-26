class Nodo:
    def __init__(self, dato):       #Constructor
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self,dato):        #Constructor
        self.raiz = Nodo(dato)
    

    def agregar_recursivo(self, nodo, dato):    #Funcion privada para agregar nodos
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.agregar_recursivo(nodo.derecha, dato)
    
    def __buscar(self,nodo,dato):
        if nodo is None:
            return None
        if nodo.dato == dato:
            return nodo
        if dato < nodo.dato:
            return self.__buscar(nodo.izquierda,dato)
        else:
            return self.__buscar(nodo.derecha,dato)
    
    def __buscar_Nivel(self,nodo,dato,nivel):
        if nodo is None:
            return None
        if nodo.dato == dato:
            return nivel
        if dato < nodo.dato:
            return self.__buscar_Nivel(nodo.izquierda,dato,nivel+1)
        else:
            return self.__buscar_Nivel(nodo.derecha,dato,nivel+1)
        
    #Funciones publicas
    def agregar(self, dato):        #Funcion para agregar nodos
        self.agregar_recursivo(self.raiz, dato)
    
    def buscar(self, nodo, dato):
        if self.__buscar(nodo,dato) is None:
            print("\nNo se encontro el dato")
        else:
            print("\nSe encontro el dato en el nivel: ",self.__buscar_Nivel(nodo,dato,0))
    
    def in_order(self, nodo):       #Funcion para recorrer el arbol en orden
        if nodo is not None:
            self.in_order(nodo.izquierda)
            print(nodo.dato, end=" ")
            self.in_order(nodo.derecha)
    
    def pre_order(self, nodo):      #Funcion para recorrer el arbol en pre orden
        if nodo is not None:
            print(nodo.dato, end=" ")
            self.pre_order(nodo.izquierda)
            self.pre_order(nodo.derecha)

    
    def post_order(self, nodo):     #Funcion para recorrer el arbol en post orden 
        if nodo is not None:
            self.post_order(nodo.izquierda)
            self.post_order(nodo.derecha)
            print(nodo.dato, end=" ")

