# Universidad de los Andes
# Fisica computacional
# Tarea 4
# Autores
#	Andres Felipe Garcia Albarracin
#	Andrea Rozo Mendez

# Importa la libreria numpay
import numpy as np

# Leer un archivo
# @param: nombre del archivo
# @return: matriz de los datos leidos
def leer(nombreArchivo):
	infile = open(nombreArchivo,'r')
	text = infile.readlines()
	matrix = []
	# Vector de recorrido
	listaRecorrido = range(len(text))
	listaRecorrido.pop(0)
	listaRecorrido.pop(0)
	for i in listaRecorrido:
		datosFila = text[i].split()
		for j in datosFila:
			matrix = matrix + [float(j)]
	return matrix


# Crea la matriz de la regresion G
# @param: matriz leida en el archivo
# @return: matriz G para la regresion
def matrizG(matrix):
	m = [[1,matrix[0],0.5*matrix[0]*matrix[0]]]
	i = 3
	G = np.matrix(m)
	while i < (len(matrix))-3:
		m = [[1,matrix[i],0.5*matrix[i]*matrix[i]]]
		G = np.concatenate((G,m))
		i=i+3
	return G

# Hace la regresion
# @param: matriz con los datos
# @return: vector con [g, voy, vox]



matriz1 = leer("experimentID_0_theta_0.0.txt")
matriz2 = matrizG(matriz1)
print matriz2
