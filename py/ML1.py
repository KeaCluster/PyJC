#Machine Learning 
'''
Tipos de datos
Para analizar los datos, es importante saber con que tipo 
de datos estamos tratando
Los datos numericos son numeros y se pueden dividir en dos categorias numericas:
Datos discretos
- numeros que estan limitados a enteros. Ejemplo: la cantidad de autos que pasan.
Datos continuos
- numeros de valor infinito. Ejemplo: el precio de un articulo o el tamanio de un articulo
Los datos categoricos son valores que no se pueden medir entre si. 
Ejemplo: un valor de color, o cualquier valor de si / no.
Los datos ordinales son como datos categoricos, pero se pueden medir entre si. 
Ejemplo: calificaciones escolares donde A es mejor que B y asi sucesivamente
'''
#>>pip3 install numpy
#>>pip3 install matplotlib
#>>pip3 install scipy
#>>pip3 install scikit-image
#>>pip3 install --upgrade pip
#>>pip3 install pandas
#>>pip3 install sklearn
#>>pip3 install pydotplus
#>>pip3 install graphviz
#Mean- Media
    #Sum(xi + xn)/n
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)
#Median- Mediana 
x = numpy.median(speed)
print(x)
speed=[7, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]
x = numpy.median(speed)
print(x)
#Mode- Modo
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)
#Desviacion estandar
    #Muestra Sum(x - X)^2 / n-1
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)
#Varianza
speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)
#Percentiles
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x)