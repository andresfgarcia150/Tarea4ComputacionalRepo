# Regresion seno
import numpy as np
angulos = np.matrix([[-3.14/2],[0],[3.14]])
sinTheta = np.sin(angulos)
sinTheta = np.transpose(sinTheta)
v1 = np.array(sinTheta[0,:])[0,:]
f = np.matrix([[2],[4],[6]])
f0,c0 = np.polyfit(v1,f,1)
print "f0 = ", f0
print "c0 = ", c0
fest = np.matrix(v1*f0+c0)
fest = np.transpose(fest)

# Grafica de salida
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

plt.plot(angulos,f)
plt.plot(angulos,fest)
plt.legend(['Datos','Estimado'])
ax = plt.axes()
ax.set_xlabel("$\\theta$",fontsize=20)
ax.set_ylabel("$F(\\theta)$",fontsize=20)
ax.set_title("$\mathrm{Funcion\ F\ real\ y\ estimada}$", fontsize=20)
filename = 'GraficaResiduos'
plt.savefig(filename + '.jpeg',format = 'jpeg', transparent=True)
