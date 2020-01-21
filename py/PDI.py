#Define la dimension de la imagen
"""
from skimage import io, color
img = io.imread('baboon.png')
dimension = color.guess_spatial_dimensions(img) #Funcion descontinuada
print(dimension)
"""
#Da las dimensiones de color de la imagen 
import skimage.io as io
from skimage.color import rgb2gray 
img = io.imread('baboon.png')
print(img.shape)

#Convertir en gris la imagen
img = io.imread('baboon.png')
img_grayscale = rgb2gray(img)
io.imsave('baboon-gs.png',img_grayscale)
show_grayscale = io.imshow(img_grayscale)
io.show()

#Filtro Sobel
from skimage import data, io, filters
img = io.imread('baboon-gs.png')
edges = filters.sobel(img)
io.imshow(edges)
io.show()