import numpy as np
import matplotlib.pyplot as plt

A = np.loadtxt('inCanion.csv')

angulo = A[0]
velocidad = A[1]

angulo = np.pi * angulo / 180;

altura = ((velocidad ** 2) * (np.sin(angulo) ** 2)) / (2 * 9.8)
alcance = ((velocidad ** 2) * np.sin(2 * angulo)) / 9.8
tiempo = (2 * velocidad * np.sin(angulo)) / 9.8

salida = np.array([[altura, alcance]])
np.savetxt("outCanion.csv", salida, fmt="%.2f")
print(f"El resultado grabado en el archivo es: {altura}, {alcance}")

tiempo = np.linspace(0, tiempo, 50)

px = velocidad * np.cos(angulo) * tiempo
py = velocidad * np.sin(angulo) * tiempo - 0.5 * 9.8 * tiempo ** 2

plt.plot(px, py)
plt.grid()
plt.title("Tiro parabolico")
plt.xlabel("Alcance en mts.")
plt.ylabel("Altura en mts")
plt.show()