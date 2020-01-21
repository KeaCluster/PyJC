#Set (no ordenada , indexada)
frutas={"Manzana","Banana","Cereza"}
print(frutas)
print("Banana" in frutas)
#Agregar a un set
frutas.add("Naranja")
print(frutas)
#Actualizar todo un sett
frutas.update(["Naranja","Mango","Uvas"])
print(frutas)
#Remover un dato de un set
frutas.remove("Mango") #si el dato no exista dara error
print(frutas)
frutas.discard("Uvas") #si el dato no existe no da error 

