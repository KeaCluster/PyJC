"""
La funcion clave para trabajar con archivos en Python es la funcion open ().
La funcion open () toma dos par ametros; nombre de archivo y modo.
Hay cuatro metodos diferentes (modos) para abrir
"r" - Leer - 
Valor predeterminado. Abre un archivo para leer, error si el archivo no existe
"a" - Agregar - 
Abre un archivo para agregar, crea el archivo si no existe
"w" - Escribir - 
Abre un archivo para escribir, crea el archivo si no existe
"x" - Crear - 
Crea el archivo especificado, devuelve un error si el archivo existe

Adem as, puede especificar si el archivo debe manejarse en modo binario o de texto
"t" - Texto - 
Valor predeterminado. Modo de texto
"b" - Binario - 
Modo binario (por ejemplo, im agenes)
"""
#Leer archivos 
f = open("demofile.txt", "r")
print(f.read())
#Escribir archivos 
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("demofile2.txt", "r")
print(f.read())
#Crear archivos
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("demofile3.txt", "r")
print(f.read())
#Borrar archivos
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
#Borrar folder
import os
os.rmdir("myfolder")