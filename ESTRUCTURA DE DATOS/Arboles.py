class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def crear_arbol():
    opcion = int(input("Ingrese cuantos nodos dedesea: "))
    
    if opcion == -1:
        # Recibir nodos infinitos
        raiz = Nodo(None)
        while True:
            valor = input("Ingrese un valor para el nodo (x para detener): ")
            if valor == "x":
                break
            nodo = Nodo(valor)
            insertar_nodo(raiz, nodo)
            
    elif opcion == 0:
        # Árbol vacío
        raiz = None
        
    elif opcion > 0:
        # Número de nodos específico
        raiz = Nodo(None)
        for i in range(opcion):
            valor = int(input(f"Ingrese el valor para el nodo {i+1}: "))
            nodo = Nodo(valor)
            insertar_nodo(raiz, nodo)
            
    else:
        print("Opción no válida")
        return None
    
    return raiz

def insertar_nodo(raiz, nodo):
    if raiz.valor is None:
        raiz.valor = nodo.valor
    elif nodo.valor < raiz.valor:
        if raiz.izquierdo is None:
            raiz.izquierdo = nodo
        else:
            insertar_nodo(raiz.izquierdo, nodo)
    else:
        if raiz.derecho is None:
            raiz.derecho = nodo
        else:
            insertar_nodo(raiz.derecho, nodo)

def recorrer_preorder(raiz):
    if raiz is not None:
        print(raiz.valor, end=" ")
        recorrer_preorder(raiz.izquierdo)
        recorrer_preorder(raiz.derecho)

def recorrer_inorder(raiz):
    if raiz is not None:
        recorrer_inorder(raiz.izquierdo)
        print(raiz.valor, end=" ")
        recorrer_inorder(raiz.derecho)

def recorrer_postorder(raiz):
    if raiz is not None:
        recorrer_postorder(raiz.izquierdo)
        recorrer_postorder(raiz.derecho)
        print(raiz.valor, end=" ")

def contar_hojas(raiz):
    if raiz is None:
        return 0
    elif raiz.izquierdo is None and raiz.derecho is None:
        return 1
    else:
        return contar_hojas(raiz.izquierdo) + contar_hojas(raiz.derecho)

def calcular_altura(raiz):
    if raiz is None:
        return 0
    else:
        altura_izq = calcular_altura(raiz.izquierdo)
        altura_der = calcular_altura(raiz.derecho)
        return max(altura_izq, altura_der) + 1

def es_completo(raiz):
    if raiz is None:
        return True
    elif raiz.izquierdo is None and raiz.derecho is None:
        return True
    elif raiz.izquierdo is not None and raiz.derecho is not None:
        return es_completo(raiz.izquierdo) and es_completo(raiz.derecho)
    else:
        return False

def contar_nodos(raiz):
    if raiz is None:
        return 0
    else:
        return contar_nodos(raiz.izquierdo) + contar_nodos(raiz.derecho) + 1

# Ejemplo de uso
arbol = crear_arbol()

while True:
    print("\n--- Menú ---")
    print("1. Recorrer el árbol de forma preorder")
    print("2. Recorrer el árbol de forma inorder")
    print("3. Recorrer el árbol de forma postorder")
    print("4. Revisar el número de hojas del árbol")
    print("5. Revisar la altura del árbol")
    print("6. Decir si el árbol es completo o no")
    print("7. Decir el número de nodos")
    print("8. Salir")
    
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        print("Recorrido Preorder:")
        recorrer_preorder(arbol)
    elif opcion == 2:
        print("Recorrido Inorder:")
        recorrer_inorder(arbol)
    elif opcion == 3:
        print("Recorrido Postorder:")
        recorrer_postorder(arbol)
    elif opcion == 4:
        hojas = contar_hojas(arbol)
        print(f"Número de hojas del árbol: {hojas}")
    elif opcion == 5:
        altura = calcular_altura(arbol)
        print(f"Altura del árbol: {altura}")
    elif opcion == 6:
        if es_completo(arbol):
            print("El árbol es completo")
        else:
            print("El árbol no es completo")
    elif opcion == 7:
        nodos = contar_nodos(arbol)
        print(f"Número de nodos del árbol: {nodos}")
    elif opcion == 8:
        break
    else:
        print("Opción no válida")

print("gracias por utilizar nuestros servicios")

