x , y , z = 1 , 2.8 ,1j 
print(x)
print(type(x)) #int
print(y)
print(type(y)) #float
print(z)
print(type(z)) #complex
#Conversiones 
    # int a float
a = float(x)
    #float a int 
b = int(y)
    #int a complex 
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#Funcion Random 
import random 
x = random.randrange(0,100)
print(x)
print(random.randrange(1,100))