#Evalua tu modelo 
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2) #Mantiene el resultado de un bloque 

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)
#Ajustar el conjunto de datos
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

#Mide la relacion de XY 
from sklearn.metrics import r2_score
r2 = r2_score(train_y, mymodel(train_x))
print(r2)

#Predecir valor de cuanto gastara un consumidor en 5 minutos en la tienda
print(mymodel(5))