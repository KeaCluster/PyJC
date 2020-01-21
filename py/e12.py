#Diccionario (Desordenado , cambiable , indexado)
carro = { 
    "Marca" : "Ford",
    "Model" : "Mustang",
    "Anio" : 1964
}
#Obtener valores de un diccionario
print(carro)
x = carro["Model"]
print(x)
y = carro.get("Model")
print(y)
#Cambiar Valores 
carro["Anio"]= 2018
print(carro)

#Imprime llaves
for x in carro:
    print(x)
#Imprime Valores 
for x in carro: 
    print(carro[x])
for x in carro.values():
    print(x)
#Imprimir llaves y datos
for x, y in carro.items(): 
    print(x , y)

#Agregar Datos y llaves 
carro["Color"]="Rojo"
print(carro)

#Diccionario dentro de un diccionario 
frutas =  {
    "manzana" : {
        "color" : "rojo",
        "precio" : 12
    },
    "pera" : {
        "color" : "verde",
        "precio" : 15
    },
    "fresa" : {
        "color" : "rojo" ,
        "precio" : 24
    }
}
print(frutas)
#Opcion alterna 
Manzana = {
    "Color" : "rojo" ,
    "Precio" : 12
}
Pera = {
    "Color" : "verde",
    "precio" : 15
}
Fresa = {
    "color" : "rojo",
    "precio" : 24
}
Frutas = {
    "Manzana" : Manzana,
    "Pera" : Pera,
    "Fresa" : Fresa
}
print(Frutas)