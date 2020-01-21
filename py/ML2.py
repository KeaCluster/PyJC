#Data Distribution
import numpy
#Crear una base de datos con 250 datos aleatorias en un rango de 0 a 6 
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)
#Histograma
import matplotlib.pyplot as plt
plt.hist(x, 6)
plt.show()

#Base de datos mayor 
x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()

#Normal Data Distribution Gauss
import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()