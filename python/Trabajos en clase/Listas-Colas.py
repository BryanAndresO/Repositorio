#Escribe un programa que permita crear una lista de nombres y luego muestre los
#nombres en orden alfabético.
nombres = ['Juan', 'Pedro', 'María', 'Ana']
nombres_ordenados = sorted(nombres)
print(nombres_ordenados)

#Implementa una Pila utilizando una estructura de datos adecuada y realiza las
#operaciones de apilar y desapilar.

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

p = Pila()
p.apilar('HOLA MUNDO')
p.apilar('¿cÓMO ESTAS?')
p.apilar('¿cÓMO TE HA DIO?')
print(p.desapilar())
print(p.desapilar())
print(p.desapilar())

#Crea una Cola que permita almacenar números enteros y realiza las operaciones
#de encolar y desencolar.

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        return self.items.pop(0)

c = Cola()
c.encolar(1)
c.encolar(2)
c.encolar(3)
print(c.desencolar())
print(c.desencolar())
print(c.desencolar())
