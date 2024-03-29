import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np


#todas las unidades de acuerdo al sistema internacional
N_p = 100 #numero de cargas positivas
N_n = 100 #numero de cargas negativas
D = 0.05 #diametro de las placas
Q = 10**(-6) #cargas
R = 1 #separación de las placas

#permitividad de los materiales
e_0 = 8.8541878176*(10**(-12)) #permitividad en el vacio
e_a = 1.00058986*e_0 #permitividad en el aire
e_c = 4.5*e_0 #permitividad en el cuarzo
e_al = 9.34*e_0 #permitividad en el alumina
e_FR4 = 4.4*e_0  #permitividad en el FR4

#calculo de campo electrico
def E(q, r0, x, y, z):
    den = (np.sqrt((x-r[0])**2 + (y-r[1])**2 + (z-r[2])**2))**3
    fac = 1/(4*np.pi*e_a)
    return fac*q*(x-r0[0])/den, fac*q*(y-r0[1])/den, fac*q*(z-r0[2])/den

#potencial electrico
def V(q, r, x, y, z):
    den = np.sqrt((x-r[0])**2 + (y-r[1])**2 + (z-r[2])**2)
    fac = 1/(4*np.pi*e_a)
    return fac*q/(den)

nx, ny, nz = 100, 100, 100

x = np.linspace(-0.025, 0.025, nx)
y = np.linspace(-0.025, 0.025, ny)
z = np.linspace(0, 1, nz)

X,Y,Z = np.meshgrid(x, y, z)

cargas = []
for i in range(N_p):
    q = Q
    for j in x:
        for k in y:
            r = np.sqrt(x**2 + y**2)
            theta = np.arctan(y/x)
    cargas.append((q, (r, theta, 1)))

cargas
for i in range(N_n):
    q = -Q
    for j in x:
        for k in y:
            r = np.sqrt(x**2 + y**2)
            theta = np.arctan(y/x)
    cargas.append((q, (r, theta, 0)))

Ex, Ey, Ez = np.zeros((ny, nx, nz)), np.zeros((ny, nx, nz)), np.zeros((nx,ny,nz))


for carga in cargas:
    ex, ey, ez = E(*carga, x=X, y=Y, z=Z)
    Ex += ex
    Ey += ey
    Ez += ez
#plot
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.quiver(x, y, z, Ex, Ey, Ez)

plt.show()
