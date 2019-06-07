import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Circle

np.seterr(divide='ignore', invalid='ignore')
#datos
e_0 = 8.8541878176*(10**(-12)) #permitividad en el vacio
e_a = 1.00058986*e_0 #permitividad en el aire

#campo electrico
def E(q, r0, x, y):
    den = np.hypot(x-r0[0], y-r0[1])**3
    fac = 1/(4*np.pi*e_a)
    return fac*q*(x-r0[0])/den, fac*q*(y-r0[1])/den

#potencial electrico
def V(q, r, x, y):
    den = np.hypot(x-r[0], y-r[1])
    fac = 1/(4*np.pi*e_a)
    return fac*q/(den)


nx, ny = 100, 100
x = np.linspace(0, 10, nx)
y = np.linspace(0, 10, ny)
X, Y = np.meshgrid(x, y)


valor_cargas = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n_cargas = 10 #numero de cargas
cargas = []
#agrega las cargas a una lista
for i in range(n_cargas):
    q = random.choice(valor_cargas)*(10**-6)
    cargas.append((q, (random.choice(x), random.choice(y))))

#crea listas con los valores coordenados del campo electrico
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
Vx, Vy = np.zeros((ny, nx)), np.zeros((ny, nx))
for carga in cargas:
    ex, ey = E(*carga, x=X, y=Y)
    Ex += ex
    Ey += ey

#establece un valor maximo para el voltaje
V_max = 1000
Volt = np.zeros((ny, nx))
for carga in cargas:
    volt = V(*carga, x=X, y=Y)
    Volt += volt
    if np.any(Volt) >= V_max:
        volt = V_max
    if np.any(Volt) <= -V_max:
        volt = -V_max

fig = plt.figure(figsize = (9,4.5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

color = np.log(np.hypot(Ex, Ey))
ax1.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)
ax2.contourf(x, y, Volt, levels = 14)
cont = ax2.contourf(x, y, Volt, levels = 14, cmap = 'bwr')
fig.colorbar(cont, ax=ax2)
colores_de_cargas = {True: '#aa0000', False: '#0000aa'}
for q, pos in cargas:
    ax1.add_artist(Circle(pos, 0.1, color = colores_de_cargas[q>0]))
    ax2.add_artist(Circle(pos, 0.1, color = colores_de_cargas[q>0]))



ax1.set_xlabel('$x [m]$')
ax1.set_ylabel('$y [m]$')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_title('Campo Electrico $[V/m]$')
ax1.set_aspect('equal')

ax2.set_xlabel('$x [m]$')
ax2.set_ylabel('$y [m]$')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_title('Potencial Electrico $[V]$')
ax2.set_aspect('equal')

plt.show()
