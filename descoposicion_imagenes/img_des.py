import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Cargar la imagen PNG
imagen = plt.imread('imagen.png')

# Obtener el tamaño de la imagen
alto, ancho, _ = imagen.shape

# Obtener los canales R, G y B de la imagen
red_channel = imagen[:, :, 0]
green_channel = imagen[:, :, 1]
blue_channel = imagen[:, :, 2]
print('color rojo')
print(red_channel)
print('color verde')
print(green_channel)
print('color azul')
print(blue_channel)

# Crear figuras y ejes para cada canal de color
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Graficar el canal rojo
axs[0, 0].imshow(red_channel, cmap='Reds')
axs[0, 0].set_title('Canal Rojo')

# Graficar el canal verde
axs[0, 1].imshow(green_channel, cmap='Greens')
axs[0, 1].set_title('Canal Verde')

# Graficar el canal azul
axs[1, 0].imshow(blue_channel, cmap='Blues')
axs[1, 0].set_title('Canal Azul')

# Crear una figura 3D
axs[1, 1] = fig.add_subplot(2, 2, 4, projection='3d')

# Generar las coordenadas X, Y y Z para la representación 3D
x, y = np.meshgrid(range(ancho), range(alto))
z = np.zeros_like(x)

# Graficar los canales R, G y B en la misma gráfica 3D
axs[1, 1].plot_surface(x, y, red_channel, cmap='Reds', label='Rojo', alpha=0.5)
axs[1, 1].plot_surface(x, y, green_channel, cmap='Greens', label='Verde', alpha=0.5)
axs[1, 1].plot_surface(x, y, blue_channel, cmap='Blues', label='Azul', alpha=0.5)

# Configurar etiquetas y títulos de los ejes
axs[1, 1].set_xlabel('X')
axs[1, 1].set_ylabel('Y')
axs[1, 1].set_zlabel('Altura')
axs[1, 1].set_title('Canales RGB')

# Ajustar los espacios entre las subfiguras
fig.tight_layout()

# Mostrar las gráficas
plt.show()
