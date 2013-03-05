# Universidad de los Andes
# Fisica computacional
# Tarea 4
# Autores
#	Andres Felipe Garcia Albarracin
#	Andrea Rozo Mendez

# Importa la libreria numpay
import numpy as np

# Librerias para el manejo de archivos
import os, sys

# Constante
numVarsRegresion = 3;

# Identifica los archivos en la carpeta de trabajo
def leerCarpeta(path):
	dirs = os.listdir( path )
	return dirs

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


# Halla la covarianza entre dos vectores
# @param: Vector1
# @param: Vector2
# @return: covarianza
def calcularCovarianza(vector1, vector2):
	m1 = np.mean(vector1)
	m2 = np.mean(vector2)
	suma = 0;
	for i in range(len(vector1)):
		suma = suma + (vector1.item(i,0)-m1)*(vector2.item(i,0)-m2)
	return suma/(len(vector1)-1)

# Halla la matriz de covarianza
# Observacion: El requerimiento solicita "verificar si los valores obtenidos para la gravedad son independientes
#	de los valores iniciales de las velocidades iniciales". No se incluye theta en el analisis
# @param: Matriz de datos: [gravedad, vox, voy]
def calcularMatrizCovarianza(matrizDatos):
	v1 = matrizDatos[:,0].copy()
	v2 = matrizDatos[:,1].copy()
	v3 = matrizDatos[:,2].copy()
	v1 = np.transpose(v1)
	v2 = np.transpose(v2)
	v3 = np.transpose(v3)
	o11 = calcularCovarianza(v1,v1)
	o12 = calcularCovarianza(v1,v2)
	o13 = calcularCovarianza(v1,v3)
	o22 = calcularCovarianza(v2,v2)
	o23 = calcularCovarianza(v2,v3)
	o33 = calcularCovarianza(v3,v3)
	o1 = [[o11,o12,o13]]
	print "o1", o1
	o2 = [[o12,o22,o23]]
	o3 = [[o13,o23,o33]]
	matrizCov = np.matrix(o1)
	matrizCov = np.concatenate((matrizCov,o2))
	matrizCov = np.concatenate((matrizCov,o3))
	return matrizCov


# Cuerpo principal del codigo
	# Lee los archivos dentro de la carpeta dir
ruta = "./hw4_data"
archivos = leerCarpeta(ruta) # vector con el nombre de los archivos
print archivos[0]
numeroArchivos = len(archivos)

	# Matriz de trabajo
	# [gravedad, vox, voy, theta, ID]	
matrizParam = np.zeros((numeroArchivos,5))

	# Parametros de la regresion
for ar in archivos:
	elem = ar.split("_")
	ID = elem[1]
	finalstr = elem[3].split(".")
	theta = '.'.join([finalstr[0],finalstr[1]])
	print ID, theta

