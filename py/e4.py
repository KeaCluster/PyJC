"""
Tipos de datos 
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""
# Ejemplos de tipos 
x= "soy un texto (-u-)/"
print("STR")
print(x)
print(type(x))
x = 20 
print("INT")
print(x)
print(type(x))
x = 3.141516
print("FLOAT")
print(x)
print(type(x))
x = 7+5j
print("COMPLEX")
print(x)
print(type(x))
x = ["apple", "banana", "cherry"]
print("LIST")
print(x)
print(type(x))
x = ("apple", "banana", "cherry")
print("TUPLE")
print(x)
print(type(x))
x = range(6)
print("RANGE")
print(x)
print(type(x))
x = {"name" : "John", "age" : 36}
print("DICT")
print(x)
print(type(x))
x = {"apple", "banana", "cherry"}
print("SET")
print(x)
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print("FROZENSET")
print(x)
print(type(x))
x = True
print("BOOL")
print(x)
print(type(x))
x = b"Hello"
print("BYTES")
print(x)
print(type(x))
x = bytearray(5)
print("BYTEARRAY")
print(x)
print(type(x))
x = memoryview(bytes(5))
print("MEMORYVIEW")
print(x)
print(type(x))
