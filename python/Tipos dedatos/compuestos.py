lista = []

print(type(lista))

lista =["Ecuador", "Peru", "Brasil"]
print(lista)

lista=["Juan", 45,6.5,True,["Ecuador", "Peru", "Brasil"]]
print(lista) 

lista= ["Ecuador", "Peru", "Brasil"]
#append me permite agrager un elemento a la lista
lista.append("México")
print(lista)


lista2 = lista.copy()
print(lista2)

#Borra  los elementos de una lisat "clear"
#lista2 = lista.clear()
#print(lista2)


lista2 = lista.copy()
#COUT me permite contar los elementos en una lista
print(lista2.count("Peru"))
listas2 = lista.append("Colombia")
listas2 = lista.append("Bolivia")
print(lista2.count("Colombia"))
print(lista2)

print(len(lista2))

print (lista[4])

lista2[3] = "Peru"
print(lista2)

#Eliminna elementos de una lista

lista2.pop
print(lista)

lista2.remove("Brasil")
print(lista2)


lista2.reverse()
print(lista2)


lista2.sort()
print(lista2)


lista3 = [4,6, "b", "b", "c"]
#lista3.sort()
#print(lista3)






#Tuplas : Estas no so n mutanles, es decir que no son mosdificables


tupla = () #Variable vacia
tupla2 = ("Juan", "Pedro", "Maria")
print(tupla2)

print(tupla2.count("Juan"))
print(tupla2.index("Maria"))

print(lista2.index("Ecuador"))

# print(tupla2.index(🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣))

print(tupla2[2])
print(tupla2[1])


lista = list(tupla2)
print(type(lista))

lista.append("Mario")
print(lista)

tupla2 = tuple(lista)
print(tupla2)



#Range

rango = range(6)
print(rango)

#Set

set = {2,3,4,5,6,6,4}
print(set)
print(type(set))


#Diccionarios

cliente001 = {
    "Nombre": "Bryan",
    "Cedula": 1754336160,
    "Celular": "0983070886",
    "Correo": "bryanfamiliat@gmail.com"
}

print(cliente001)

print(type(cliente001))

print(cliente001["Correo"])

print(cliente001.get("Celular"))

cliente001["Nombre"] = "Andres"
print(cliente001)

