#----------------------------------------------Pregunta 1 ------------------------------------------------------------


#Verificar si una lista está ordenada de forma ascendente

def esta_ordenada_ascendente(lista):
    return lista == sorted(lista)

# Ejemplo de uso
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [5, 4, 3, 2, 1]

if esta_ordenada_ascendente(lista_1):
    print("La lista 1 está ordenada de forma ascendente.")
else:
    print("La lista 1 no está ordenada de forma ascendente.")

if esta_ordenada_ascendente(lista_2):
    print("La lista 2 está ordenada de forma ascendente.")
else:
    print("La lista 2 no está ordenada de forma ascendente.")


#-----------------------------------------------Pregunta 2 -----------------------------------------------------------
#Implementar una pila utilizando una lista

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

    def obtener_tamano(self):
        return len(self.items)


# Ejemplo de uso
pila = Pila()
print("La pila está vacía:", pila.esta_vacia())

pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print("Tamaño de la pila:", pila.obtener_tamano())

elemento = pila.desapilar()
print("Elemento desapilado:", elemento)

print("Tamaño de la pila después de desapilar:", pila.obtener_tamano())



#--------------------- --------------------------Pregunta 3 -----------------------------------------------------------
#Verificar si una palabra es un palíndromo utilizando una pila
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

def es_palindromo(palabra):
    pila = Pila()
    for letra in palabra:
        pila.apilar(letra)

    palabra_invertida = ""
    while not pila.esta_vacia():
        letra = pila.desapilar()
        palabra_invertida += letra

    return palabra == palabra_invertida

# Ejemplo de uso
palabra_1 = "radar"
palabra_2 = "python"

if es_palindromo(palabra_1):
    print(palabra_1, "es un palíndromo.")
else:
    print(palabra_1, "no es un palíndromo.")

if es_palindromo(palabra_2):
    print(palabra_2, "es un palíndromo.")
else:
    print(palabra_2, "no es un palíndromo.")
    
    


#--------------------- --------------------------Pregunta 4 -----------------------------------------------------------
#Implementar una cola utilizando una lista

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop(0)

    def obtener_tamano(self):
        return len(self.items)

# Ejemplo de uso
cola = Cola()
print("La cola está vacía:", cola.esta_vacia())

cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

print("Tamaño de la cola:", cola.obtener_tamano())

elemento = cola.desencolar()
print("Elemento desencolado:", elemento)

print("Tamaño de la cola después de desencolar:", cola.obtener_tamano())



#--------------------- --------------------------Pregunta 5 -----------------------------------------------------------
#Implementar una cola utilizando una lista



def es_simetrica(lista):
    longitud = len(lista)
    for i in range(longitud // 2):
        if lista[i] != lista[longitud - i - 1]:
            return False
    return True

# Ejemplo de uso
lista_1 = [1, 2, 3, 2, 1]
lista_2 = [1, 2, 3, 4, 5]

if es_simetrica(lista_1):
    print("La lista 1 es simétrica.")
else:
    print("La lista 1 no es simétrica.")

if es_simetrica(lista_2):
    print("La lista 2 es simétrica.")
else:
    print("La lista 2 no es simétrica.")
