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
# @param: matriz con los datos: [1, t, t^2/2]
# @param: vector de datos y o x
# @return: vector con [m1 m2 m3]
def regresion(matrizDatos, vectorDatos):
	g = matrizDatos
	gt = np.transpose(g)
	x = gt*g
	xinv = np.linalg.inv(x)
	y = xinv*gt
	m = y*vectorDatos
	return m


#Lee los datos
matriz1 = leer("experimentID_0_theta_0.0.txt")
# Vector de posiciones en x
x = [matriz1[1]]
i = 4
dx = np.matrix(x)
while i < (len(matriz1))-3:
	x = [[matriz1[i]]]
	dx = np.concatenate((dx,x))
	i=i+3
# Vector de posiciones en y
y = [matriz1[2]]
i = 5
dy = np.matrix(y)
while i < (len(matriz1))-3:
	y = [[matriz1[i]]]
	dy = np.concatenate((dy,y))
	i=i+3
#Matriz G
G = matrizG(matriz1)
#Regresion en x
mx = regresion(G,dx)
#Regresion en y
my = regresion(G,dy)

#g,v0x,v0y
v0x = mx[1]
v0y = my[1]
g = my[2]

print "g = ",g,"m/s2\n","v0x = ",v0x,"m/s\n","v0y = ",v0y,"m/s\n"

