#Tulpas (los datos son incambiables, es ordenada)
frutas = ("Manzana","Banana","Cereza")
print(frutas)
    #Imprimir una pocision 
print(frutas[1])
    #Imprimir en orden negativo
print(frutas[-1])
froot= ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    #Imprimir un rango
print(froot[2:5])
    #Imprimir rango inverso 
print(froot[-4:-1])
#Convertir una tulpa en una lista
y = list(froot)
y[1] = "kiwi"
#Convertir lista en tulpa
x = tuple(y)
print(y)
print(x)

tulpa=("abc",)#Esto es una tulpa
print(type(tulpa))
notulpa=("abc")#esto no es una tulpa
print(type(notulpa))
