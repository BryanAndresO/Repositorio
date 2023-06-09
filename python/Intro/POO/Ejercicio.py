class Jaco:
    def __init__(self, nombre, edad, sexo, altura, etnia) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.altura = altura
        self.etnia = etnia
        
class hijitoJaco(Jaco,):
    def __init__(self, nombre, edad, sexo, altura, etnia, bonita) -> None:
        super().__init__(nombre, edad, sexo, altura, etnia)
        self.bonita = bonita

def imprimir():
    
    print(f'Hola mi nombre es :  {self.nombre}')
    print(f'fMi edad es : {self.edad}')
    print(f'sexo {self.sexo}')
    print(f'Su altura: {self.altura}')
    print(f'Etia: {self.etnia}')
    print(f'Bonita : {self.bonita}')
    

hijito_jaco = hijitoJaco('bryan', 20, 'cada que afloja', 1.70, 'zaraguro', 'pamela')
hijito_jaco.imprimir()