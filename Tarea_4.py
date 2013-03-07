# Universidad de los Andes
# Fisica computacional
# Tarea 4
# Autores
#	Andres Felipe Garcia Albarracin
#	Andrea Rozo Mendez

# Importacion de las librerias a emplear
import numpy as np
import pylab
import os, sys

# Constantes
numVarsRegresion = 3;
ruta = "./hw4_data"

# Identifica los archivos en la carpeta de trabajo
def leerCarpeta(path):
	dirs = os.listdir( path )
	return dirs

# Leer un archivo
# @param: nombre del archivo
# @return: matriz de los datos leidos
def leer(nombreArchivo):
	infile = open(ruta + "/" + nombreArchivo,'r')
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
	o11 = calcularCovarianza(v1,v1)
	o12 = calcularCovarianza(v1,v2)
	o13 = calcularCovarianza(v1,v3)
	o22 = calcularCovarianza(v2,v2)
	o23 = calcularCovarianza(v2,v3)
	o33 = calcularCovarianza(v3,v3)
	o1 = [[o11,o12,o13]]
	o2 = [[o12,o22,o23]]
	o3 = [[o13,o23,o33]]
	matrizCov = np.matrix(o1)
	matrizCov = np.concatenate((matrizCov,o2))
	matrizCov = np.concatenate((matrizCov,o3))
	return matrizCov


# Cuerpo principal del codigo
	# Lee los archivos dentro de la carpeta dir

archivos = leerCarpeta(ruta) # vector con el nombre de los archivos
numeroArchivos = len(archivos)

	# Matriz de trabajo: matrizParam
	# [gravedad, vox, voy, theta, ID]
matrizParam = np.matrix([[0,0,0,0,0]])

	# Parametros de la regresion
for ar in archivos:
	elem = ar.split("_")
	ID = elem[1]
	finalstr = elem[3].split(".")
	theta = '.'.join([finalstr[0],finalstr[1]])
	#Lee los datos
	matriz1 = leer(ar)
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
	salida = [[g.item(0,0),v0x.item(0,0),v0y.item(0,0),float(theta),float(ID)]]
	matrizParam = np.concatenate((matrizParam,salida))

matrizParam = np.delete(matrizParam,0,0)

	# Organiza los datos por la columna theta
matrizParam2 = np.sort(matrizParam.view('i8,i8,i8,i8,i8'), order=['f3','f4'], axis=0).view(np.double)


	# Guarda los datos de la regresion
np.savetxt("Regresion.txt",matrizParam2, fmt = "%10.5f") #header = "# [g, vox, voy, theta, ID]"

	# Calcula la matriz de covarianza de g, vox y voy
matrizParam3 = matrizParam2[:,0:3]
matrizCov = calcularMatrizCovarianza(matrizParam3)


	# Vectores y valores propios de la matriz de covarianza
valPropios, vecPropios = np.linalg.eig(matrizCov)


	# Archivo con los vectores y valores propios
nombreArchivoSalida = "VectoresValoresPropios.txt"
archivoSalida = open(nombreArchivoSalida,'w')

archivoSalida.write("Valores propios: \n")
lineaTexto = '%10.5f %10.5f %10.5f' % (valPropios[0], valPropios[1], valPropios[2])
archivoSalida.write(lineaTexto)
archivoSalida.write("\n\nVectores propios: \n")
lineaTexto = '%10.5f %10.5f %10.5f \n' % (vecPropios[0,0], vecPropios[1,0], vecPropios[2,0])
archivoSalida.write(lineaTexto)
lineaTexto = '%10.5f %10.5f %10.5f \n' % (vecPropios[0,1], vecPropios[1,1], vecPropios[2,1])
archivoSalida.write(lineaTexto)
lineaTexto = '%10.5f %10.5f %10.5f \n' % (vecPropios[0,2], vecPropios[1,2], vecPropios[2,2])
archivoSalida.write(lineaTexto)

archivoSalida.close()


	#Calcula los valores medios para la gravedad para cada angulo theta
filas = matrizParam2.shape[0]
suma = 0.0
gmedia = np.matrix(np.sum(matrizParam2[0:6,0])/6)
angulos = np.matrix(matrizParam2[0,3])
i = 6
while i <= filas-6:
	suma = [[np.sum(matrizParam2[i:i+6,0])/6]]
	gmedia = np.concatenate((gmedia,suma))
	angle = [[matrizParam2[i,3]]]
	angulos = np.concatenate((angulos,angle))
	i=i+6
	
	# Grafica de gmedia - theta
pylab.plot(angulos,gmedia,'.')
pylab.xlabel('angulo polar (grados)')
pylab.ylabel('gravedad media (m/s^2)')
pylab.title('Gravedad media vs. Angulo polar')
pylab.savefig('gmedia')
pylab.grid(True)

	#Calculo de las variaciones de la gravedad
F = np.matrix(1.0 - (gmedia[0]/9.81))
i = 1
for i in range ((filas/6)-1):
	calc = 1.0 - (gmedia[i]/9.81)
	F = np.concatenate((F,calc))

	# Regresion seno
from numpy import pi
sinTheta = np.sin(angulos*2*pi/360)
sinTheta = np.transpose(sinTheta)
v1 = np.array(sinTheta[0,:])[0,:]
f0,c0 = np.polyfit(v1,F,1)
print "f0\n", f0
print "c0\n", c0
fest = np.matrix(v1*f0+c0)
fest = np.transpose(fest)
error = F - fest

	# Grafica de salida
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(angulos,F)
ax.plot(angulos,fest)
ax.legend(['Datos','Estimado'])
ax.set_xlabel("$\\theta$",fontsize=20)
ax.set_ylabel("$F(\\theta)$",fontsize=20)
ax.set_title("$\mathrm{Funcion\ F\ real\ y\ estimada}$", fontsize=20)
filename = 'GraficaAjuste'
fig.savefig(filename + '.jpeg',format = 'jpeg', transparent=True)

pylab.plot(angulos,F,'.')
pylab.xlabel('angulo polar (grados)')
pylab.ylabel('fluctuacion de la gravedad')
pylab.title('Fluctuacion de la gravedad vs. Angulo polar')
pylab.savefig('Fluctuacion')
pylab.grid(True)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.bar(angulos,error)
ax2.set_xlabel("$\\theta$",fontsize=20)
ax2.set_ylabel("$E(\\theta)$",fontsize=20)
ax2.set_title("$\mathrm{Error\ de\ F}$", fontsize=20)
filename = 'GraficaResiduos'
fig2.savefig(filename + '.jpeg',format = 'jpeg', transparent=True)

pylab.plot(angulos,error,'.')
pylab.xlabel('angulo polar (grados)')
pylab.ylabel('error')
pylab.title('Error vs. Angulo polar')
pylab.savefig('Error')
pylab.grid(True)
