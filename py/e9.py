#listas (los datos son cambiables , agregables , ordenados y permite duplicar)
colores = ["rojo","azul","verde"]
print(colores)
#imprime la pocision 
print(colores[1])
#imprime la posicion inversa 
print(colores[-1])
frutas = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#Imprime un rango 
print(frutas[2:5])
#imprime hasta un rango 
print(frutas[:4])
#imprime desde el rango  
print(frutas[2:])
#imprime en rango inverso 
print(frutas[-4:-1])
#cambiar en una lista 
colores[1]= "amarillo"
print(colores)
#crear un loop de for
for x in colores :
    print(x)
#encontrar un valor en una lista 
if "rojo" in colores : 
    print("El roso se encuenta en la lista")
    print(len(colores))
#Agregar un dato a la lista 
colores.append("azul")
print(colores)
    #agregar en una pocision 
colores.insert(2,"naranja")
print(colores)
#remover objetos
colores.remove("amarillo")
colores.pop(1)
print(colores)
del colores[0]
print(colores)
del colores
#copiar una lista 
'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
'''
#limpiar una lista 
'''
frutas.clear()
print(frutas)
'''
#join de listas 
    #Agregar de una sola pasada 
lista1 = ["a","b","c"]
lista2 = [1,2,3]
lista3 = lista1 + lista2
print(lista3) 
    #Agregar uno por uno 
for x in lista2: 
    lista1.append(x)
print(lista1)
    #Por metodo de extension 
lista1=["a","b","c"]
lista1.extend(lista2)
print(lista1)

#convertir una lista en un cosntructor 
thislista = list(("Manzana","Banana","Cereza"))
print(thislista)