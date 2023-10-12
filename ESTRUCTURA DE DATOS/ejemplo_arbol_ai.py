def crear_arbol(n):
  """Crea un árbol binario con n nodos."""
  if n == -1:
    # Crear un árbol infinito.
    return crear_arbol_infinito()
  elif n == 0:
    # Crear un árbol vacío.
    return None
  elif n > 0:
    # Crear un árbol con n nodos.
    return crear_arbol_n(n)
  else:
    # Mostrar un mensaje informando que la opción no es válida.
    print("Opción no válida.")
def crear_arbol_infinito():
  """Crea un árbol binario infinito."""
  # Crear la raíz del árbol.
  raiz = Nodo(None, None, None)
  # Crear los hijos de la raíz.
  raiz.izquierda = Nodo(None, None, None)
  raiz.derecha = Nodo(None, None, None)
  # Crear los hijos de los hijos de la raíz.
  raiz.izquierda.izquierda = Nodo(None, None, None)
  raiz.izquierda.derecha = Nodo(None, None, None)
  raiz.derecha.izquierda = Nodo(None, None, None)
  raiz.derecha.derecha = Nodo(None, None, None)
  # ...
  # Devolver la raíz del árbol.
  return raiz
def crear_arbol_n(n):
  """Crea un árbol binario con n nodos."""
  # Crear la raíz del árbol.
  raiz = Nodo(None, None, None)
  # Crear los hijos de la raíz.
  raiz.izquierda = Nodo(None, None, None)
  raiz.derecha = Nodo(None, None, None)
  # Crear los hijos de los hijos de la raíz.
  raiz.izquierda.izquierda = Nodo(None, None, None)
  raiz.izquierda.derecha = Nodo(None, None, None)
  raiz.derecha.izquierda = Nodo(None, None, None)
  raiz.derecha.derecha = Nodo(None, None, None)
  # ...
  # Devolver la raíz del árbol.
  return raiz