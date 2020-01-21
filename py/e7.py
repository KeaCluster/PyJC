print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 200
b = 33
if b > a:
  print("b es mayor que a")
else:
  print("b es menor que  a")
#Cualquier str es true , amenos que este vacio 
#Cualquier numero es true, excepto 0 
#Cualquier lista,tulpa set y diccionario es true, excepto los vacios 
print(bool('abc'))
print(bool(123))
print(bool(["manzanas","cerezas","bananas"]))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
x = 200
print(isinstance(x,int))