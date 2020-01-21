#Multiple Regression  3th Dimension
import pandas
from sklearn import linear_model
#Leer csv con datos carro, modelo, volumen, peso, co2 
df = pandas.read_csv("cars.csv")
#Valores independientes
X = df[['Weight', 'Volume']]
#valores dependientes 
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predecir la emision de CO2 de un automovil donde el peso es de 2300g, 
#y el volumen es de 1300ccm:
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)
#Hemos pronosticado que un automovil con motor de 1.3 litros y un peso de 
# 2.3 kg liberara aproximadamente 107 gramos de CO2 por cada kilometro que conduzca.

#Coeficiente 
print(regr.coef_)
#El coeficiente es un factor que describe la relacion con una variable desconocida.
#Ejemplo: si x es una variable, entonces 2x es x dos veces. x es la variable 
# desconocida, y el numero 2 es el coeficiente.
#En este caso, podemos pedir el valor del coeficiente de peso contra CO2 y 
# el volumen contra CO2. Las respuestas que obtenemos nos dicen que sucederia si 
# aumentamos o disminuimos uno de los valores independientes.

#EXPLICACION
"""
La matriz de resultados representa los valores de los coeficientes de peso y valor.

Peso: 0.00755095
Volumen: 0.00780526

Estos valores nos dicen que si el peso aumenta en 1 g, la emision de CO2 aumenta en 0.00755095 g.
Y si el tamanio del motor (Volumen) aumenta en 1 cm3, la emision de CO2 aumenta en 0.00780526 g.
"""