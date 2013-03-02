# Universidad de los Andes
# Fisica computacional
# Tarea 4
# Autores
#	Andres Felipe Garcia Albarracin
#	Andrea Rozo Mendez

# Importa la libreria numpay
import numpy as np

# Leer un archivo
# @Param: nombre del archivo
# @Return: matriz de los datos leidos
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


# Hace la regresion
# @param: matriz con los datos: [1, t, t^2/2]
# @param: vector de datos y o x
# @return: vector con [m1 m2 m3]
def regresion(matrizDatos, vectorDatos):
	g = matrizDatos
	gt = np.transpose(g)
	# x = gt*g
	x = gt*g
	xinv = np.linalg.inv(x)
	y = xinv*gt
	m = y*vectorDatos
	return m




matriz1 = leer("experimentID_0_theta_0.0.txt")
a = np.matrix('1 2;3 4; 5 6')
print a
v = np.matrix('3;2;3')
regresion(a,v)
#print matriz1
