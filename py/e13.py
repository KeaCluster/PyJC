#Condiciones 

print("Ingresar dos valores numericos")
y = input()
x = input()

if y > x : print(str(y) + " es mayor que " + str(x))
elif x == y: print(str(y) + " es igual a " + str(x))
else:  print(str(x) + " es mayor que " +str(y))

#Para usar Or o And 
print("Ingresa una palabra y dos letras para buscar")
a = raw_input("Ingrese la palabra: ")
b = raw_input("Ingrese el caracter 1 ")
c = raw_input("Ingrese el caracter 2 ")
if b in a and c in a: 
    print("ambas letras estan en la palabra")
elif b in a or c in a: 
    print("solo una letra esta en la palabra")
else: 
    print("ninguna letra se encuentra en la palabra :(")