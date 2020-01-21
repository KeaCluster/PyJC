#Decision Tree
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
#Leer archivo con los datos de los shows 
df = pandas.read_csv("shows.csv") 
#print(df)
#Evalua valores binarios 
    #Nacionalidades
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
    #Si se asistio o no al show
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
#print(df)
#Caracteristica 
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
#Crear arbol de decisiones
#Instalar Graphviz
"""
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')
img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
"""
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
print("[1] Significa 'GO'")
print("[0] Significa 'NO'")
print(dtree.predict([[40, 10, 6, 1]]))
