# class Abuelo:
    
#     def __init__(self, nombre) -> None:
#         self.nombre= nombre

# class Padre(Abuelo):
    
#     def __init__(self, nombre, profesion) -> None:
#         super().__init__(nombre)
#         self.profesion = profesion
        
#     def habilidad(self):
#         return f"Yo puedo cantar"
    
# class Hijo(Padre):
    
#     def __init__(self, nombre, profesion) -> None:
#         super().__init__(nombre, profesion)
        
        
# Juan = Hijo("Juan", "Ingeniero")
# print(Juan.nombre)
# print(Juan.habilidad())
# print(Juan.profesion)


#--------------------Ejercioo de Herencia Multinivel --------------------------


class Animal:
    def __init__(self, especie):
        self.especie = especie
        print("Animal creado")

    def quien_soy(self):
        print("Soy un animal")

    def comer(self):
        print("Comiendo")


class Mascota(Animal):
    def __init__(self, especie, nombre):
        super().__init__(especie)
        self.nombre = nombre 
        
    def quien_soy(self):
        print(f"Soy una mascota y mi nombre es {self.nombre}")
        print(f"soy de una especeie {self.especie}")
        
        


class Perro(Mascota):
    def __init__(self, especie, nombre):
        super().__init__(especie, nombre)
        
    def quien_soy(self):
        print("Soy un perro")


perrito = Perro("Canislupus","Sammy")
perrito.quien_soy()
