class Nodo: 
    def __init__(self, valor): 
        self.valor: int = valor 
        self.hijo_izquierdo = None
        self.hijo_derecho = None 

def crear_arbol(): 
    numero_nodos= int(input("escriba el numero de nodos del arbol")) 
    if numero_nodos == -1: 
        arbol_infinito() 
    else: 
        if numero_nodos == 0: 
            print("None")  
        else: 
            if numero_nodos is not int: 
                print("el valor ingresado no es valido")
                return crear_arbol() 
            else:  
                return armar_nodo_usuario()
            
    def arbol_infinito(self): 
            salir =str(input("si desea parar escriba una x en minuscula")) 

    def armar_nodo_usuario(self): 
        pass 


n=Nodo(2)
crear_arbol()               