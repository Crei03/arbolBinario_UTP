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
    
    def pre_order(self, nodo):      #Funcion para recorrer el arbol en pre orden
        resultado = []
        if nodo is not None:
            resultado.append(nodo.dato)
            resultado.extend(self.pre_order(nodo.izquierda))
            resultado.extend(self.pre_order(nodo.derecha))
        return resultado
    
    def in_order(self, nodo):       #Funcion para recorrer el arbol en orden
        resultado = []
        if nodo is not None:
            resultado.extend(self.in_order(nodo.izquierda))
            resultado.append(nodo.dato)
            resultado.extend(self.in_order(nodo.derecha))
        return resultado
    
    def post_order(self, nodo):     #Funcion para recorrer el arbol en post orden 
        resultado = []
        if nodo is not None:
            resultado.extend(self.post_order(nodo.izquierda))
            resultado.extend(self.post_order(nodo.derecha))
            resultado.append(nodo.dato)
        return resultado
    
    def reiniciar(self):
        if self.raiz is not None:
            self.raiz.izquierda = None
            self.raiz.derecha = None
            
    def eliminar(self, nodo, dato):
        if nodo is None:
            return nodo

        # Si el dato a eliminar es menor que el dato del nodo actual, ve al subárbol izquierdo
        if dato < nodo.dato:
            nodo.izquierda = self.eliminar(nodo.izquierda, dato)

        # Si el dato a eliminar es mayor que el dato del nodo actual, ve al subárbol derecho
        elif dato > nodo.dato:
            nodo.derecha = self.eliminar(nodo.derecha, dato)

        # Si el dato es igual al dato del nodo, este es el nodo que debemos eliminar
        else:
            # Caso 1: El nodo es una hoja
            if nodo.izquierda is None and nodo.derecha is None:
                nodo = None

            # Caso 2: El nodo tiene un solo hijo (derecha)
            elif nodo.izquierda is None:
                nodo = nodo.derecha

            # Caso 2: El nodo tiene un solo hijo (izquierda)
            elif nodo.derecha is None:
                nodo = nodo.izquierda

            # Caso 3: El nodo tiene dos hijos
            else:
                if self.profundidad(nodo.izquierda) <= self.profundidad(nodo.derecha):
                    # Si el subárbol izquierdo es menos profundo o igual, usa el máximo en el izquierdo
                    temp = self.max_value_node(nodo.izquierda)
                    nodo.dato = temp.dato
                    nodo.izquierda = self.eliminar(nodo.izquierda, temp.dato)
                else:
                    # Si el subárbol derecho es menos profundo, usa el mínimo en el derecho
                    temp = self.min_value_node(nodo.derecha)
                    nodo.dato = temp.dato
                    nodo.derecha = self.eliminar(nodo.derecha, temp.dato)

        return nodo


    def min_value_node(self, nodo):
        actual = nodo
        # El valor mínimo está en el nodo más a la izquierda
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def max_value_node(self, nodo):
        current = nodo
        # El valor máximo está en el nodo más a la derecha
        while actual.derecha is not None:
            actual = actual.derecha
        return actual

    def profundidad(self, nodo):
        if nodo is None:
            return 0
        else:
            izquierda_profundidad = self.profundidad(nodo.izquierda)
            derecha_profundidad = self.profundidad(nodo.derecha)
            return max(izquierda_profundidad, derecha_profundidad) + 1

