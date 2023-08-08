import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

filas, columnas = 50, 50

tablero_inicial = np.random.choice([0, 1], size=(filas, columnas), p=[0.7, 0.3])

def siguiente_estado(tablero):
    nuevo_tablero = np.copy(tablero)
    for i in range(filas):
        for j in range(columnas):
            suma_vecinos = np.sum(tablero[max(0, i-1):min(filas, i+2), max(0, j-1):min(columnas, j+2)]) - tablero[i, j]
            if tablero[i, j] == 1 and (suma_vecinos < 2 or suma_vecinos > 3):
                nuevo_tablero[i, j] = 0
            elif tablero[i, j] == 0 and suma_vecinos == 3:
                nuevo_tablero[i, j] = 1
    return nuevo_tablero

fig, ax = plt.subplots()
img = ax.imshow(tablero_inicial, cmap='binary', interpolation='nearest')

def actualizar(frame):
    img.set_data(actualizar.tablero)
    actualizar.tablero = siguiente_estado(actualizar.tablero)
    return img,

actualizar.tablero = tablero_inicial

ani = animation.FuncAnimation(fig, actualizar, frames=200, interval=200, save_count=50)

plt.show()
