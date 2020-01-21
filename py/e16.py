#Clases/Objetos
    #Crear una clase 
class clase:
    x=5 
p1 = clase()
print(p1.x)

class persona: 
    def __init__(per, nombre, edad): 
        per.nombre = nombre
        per.edad = edad 
p1 = persona("jose", 23)
print(p1.nombre)
print(p1.edad)
