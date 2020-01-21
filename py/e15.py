#Definir funcion
def impresion():
    print("(>-u-)>  <(-u-<)")
#Llamar funcion
impresion()
#argumentos en una funcion 
def impresion2(texto):
    print("(>-u-)>" + texto + "<(-u-<)")
impresion2("hola")
impresion2("(>-.-<)")
#recibir varios argumentos 
def funcion(*ninos):
    print("El mas joven es " + ninos[2] )
funcion("jose", "paco", "pedro","ramon")
#Utilizar un diccionario
def funcion2(**ex):
    print("Su carro es un " + ex["Marca"])
funcion2(Marca ="Ford",Model = "Mustang",Anio = 1964)
#Retornar valores 
def por5(x): 
    return 5 * x 
print(por5(5))

#LAMBDA
x = lambda a : a + 10 
print(x(5))
x =lambda a , b : a * b
print(x(5,6))

#Funcion y lambda 
def funcion3(n): 
    return lambda a: a * n
doble = funcion3(2)
print(doble(11))