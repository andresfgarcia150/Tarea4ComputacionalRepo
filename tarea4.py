# Universidad de los Andes
# Fisica computacional
# Tarea 4
# Autores
#	Andres Felipe Garcia Albarracin
#	Andrea Rozo Mendez

# Importa la librería numpay
import numpay as np

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
# @param: matriz con los datos
# @return: vector con [g, voy, vox]
def regresion 


matriz1 = leer("experimentID_0_theta_0.0.txt")
print matriz1
