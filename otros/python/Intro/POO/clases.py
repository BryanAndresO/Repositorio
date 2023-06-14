class habilidades():
    def __init__(self,nombre,edad,carrera,habilidad):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.habilidad= habilidad
        
    def miPerfil(self):
        return f"Mi nombre es {self.nombre}, tengo {self.edad} estudio {self.carrera} y mi habilidad es {self.habilidad}" 
    
    def __str__(self):
        return self.miPerfil()

Bryan = habilidades("Andres",18,"TI","Matar de iras")
print(Bryan)
