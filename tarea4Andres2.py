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
error = f - fest
print error

# Grafica de salida
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(angulos,f)
ax.plot(angulos,fest)
ax.legend(['Datos','Estimado'])
ax.set_xlabel("$\\theta$",fontsize=20)
ax.set_ylabel("$F(\\theta)$",fontsize=20)
ax.set_title("$\mathrm{Funcion\ F\ real\ y\ estimada}$", fontsize=20)
filename = 'GraficaAjuste'
fig.savefig(filename + '.jpeg',format = 'jpeg', transparent=True)


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.bar(angulos,error)
ax2.set_xlabel("$\\theta$",fontsize=20)
ax2.set_ylabel("$E(\\theta)$",fontsize=20)
ax2.set_title("$\mathrm{Error\ de\ F}$", fontsize=20)
filename = 'GraficaResiduos'
fig2.savefig(filename + '.jpeg',format = 'jpeg', transparent=True)
