#Variables y declaraciones 
x = 5 #x es entero 
print( "Valor inicial de x " + str(x))
x = "Sally" #x ahora es strng 
print("nuevo valor de x " + x) 
x = 'Sally' #o importa el tipo de comillas 
print("Sally sigue siendo la misma " + x )
#Declarar muchas variables 
x, y, z, = "naranja", "banana" , "cereza"
print("Ejemplo de declaracion de multiples variables")
print(x)
print(y)
print(z)
#Darle el mismo valor a multiples variables 
x = y = z = "Lil Sally"
print(x)
print(y)
print(z)
#Concatenar 
    #strg
y = " walk "
z = x + y 
print(z + " es lo mismo que " + x + y)
    #numeros
x, y = 5 , 10
print(x + y)
    #numero y enteros
print(z + x )