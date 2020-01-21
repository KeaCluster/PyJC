#soy un comentario 
a = """
Mambru se fue a la guerra,
que dolor, que dolor, que pena,
Mambru se fue a la guerra,
no se cuando vendra.
Do-re-mi, do-re-fa,
no se cuando vendra.
"""
print(a)
#los str tambien son arrays 
x = 'yamete kudasai '
#imprimir una posicion 
print(x[1])
#imprimir rango determinado 
print(x[0:6])
#imprimier alreves un texto 
print(x[-8:-1])
#contar un str
print(len(a))
print(len(x))
#metodos en un str 
    #remover espacios blancos 
print(a.strip())
    #Mayusculas y Minusculas 
print(x.lower())
print(x.upper())
    #Remplazar letras o caracteres 
print(a.replace("a", "X"))
    #Separar strings 
c = "bai bai motherfuckers"
print(c.split(" "))
    #Buscar dentro de un string 
d = """Por eso esperaba con la carita empapada 
A que llegaras con rosas, con mil rosas para mi """
y = "rosas" in d 
print(y)
y = "rosas" not in d
print(y)

#Concatenar
a = "Huele a"
b = "gas."
c = a + " " + b + " Fuga!!!"
print(c)
#concatenar un str y un int 
#Opcion 1 
a = "El numero ganador es "
b = 36 
c = a + str(b)
print(c)
#metodo 2 
a = "El numero de la suerte es {}"
print(a.format(b))
    #ejemplo
Can= 3 
Ord= 5 
Pre= 10.50
Orden= "Tiene que pagar de la orden {} por {} piezas con un precio de {} el total de {}"
print(Orden.format(Ord,Can,Pre, Can * Pre))
#Funciones str
"""
capitalize () Convierte el primer caracter a mayuscula
casefold () Convierte una cadena en minusculas
center () Devuelve una cadena centrada
count () Devuelve el numero de veces que ocurre un valor especificado en una cadena
encode () Devuelve una version codificada de la cadena
endswith () Devuelve verdadero si la cadena termina con el valor especificado
expandtabs () Establece el tamano de la pestana de la cadena
find () Busca en la cadena un valor especificado y devuelve la posicion donde se encontro
format () Formatea los valores especificados en una cadena
format_map () Formatea los valores especificados en una cadena
index () Busca en la cadena un valor especificado y devuelve la posicion donde se encontro
isalnum () Devuelve True si todos los caracteres de la cadena son alfanumericos
isalpha () Devuelve True si todos los caracteres de la cadena estan en el alfabeto
isdecimal () Devuelve True si todos los caracteres de la cadena son decimales
isdigit () Devuelve True si todos los caracteres de la cadena son digitos
isidentifier () Devuelve True si la cadena es un identificador
islower () Devuelve True si todos los caracteres de la cadena estan en minusculas
isnumeric () Devuelve True si todos los caracteres de la cadena son numericos
isprintable () Devuelve True si todos los caracteres de la cadena son imprimibles
isspace () Devuelve True si todos los caracteres de la cadena son espacios en blanco
istitle () Devuelve True si la cadena sigue las reglas de un titulo
isupper () Devuelve True si todos los caracteres de la cadena son mayusculas
join () Une los elementos de un iterable al final de la cadena
ljust () Devuelve una version justificada a la izquierda de la cadena
lower () Convierte una cadena en minusculas
lstrip () Devuelve una version de corte izquierda de la cadena
maketrans () Devuelve una tabla de traduccion para usar en las traducciones
particion () Devuelve una tupla donde la cadena se divide en tres partes
replace () Devuelve una cadena donde un valor especificado se reemplaza con un valor especificado
rfind () Busca en la cadena un valor especificado y devuelve la ultima posicion de donde se encontro
rindex () Busca en la cadena un valor especificado y devuelve la ultima posicion de donde se encontro
rjust () Devuelve una version justificada correcta de la cadena
rpartition () Devuelve una tupla donde la cadena se divide en tres partes
rsplit () Divide la cadena en el separador especificado y devuelve una lista
rstrip () Devuelve una version de corte derecha de la cadena
split () Divide la cadena en el separador especificado y devuelve una lista
splitlines () Divide la cadena en los saltos de linea y devuelve una lista
comienza con () Devuelve verdadero si la cadena comienza con el valor especificado
strip () Devuelve una version recortada de la cadena
swapcase () Intercambia mayusculas y minusculas se convierte en mayusculas y viceversa
title () Convierte el primer caracter de cada palabra en mayusculas
translate () Devuelve una cadena traducida
upper () Convierte una cadena en mayusculas
zfill () Rellena la cadena con un numero especificado de valores 0 al principio
"""
#Octales y Hexadecimales 
octal = "\110\145\154\154\157"
hexa = "\x48\x65\x6c\x6c\x6f"
print(octal + " " + hexa)