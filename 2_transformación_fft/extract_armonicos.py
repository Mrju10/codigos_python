import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import numpy as np

filename = input("Ingrese el nombre del archivo: ")
filepath = f"C:/Users/pc/.../{filename}"

data = pd.read_csv(filepath, sep=',', header=None)
y = data.values.reshape(-1)

midpoint = len(y)

# Number of sample points
N = 125000
# sample spacing
T = 1.0 / 48000.0
x = np.linspace(0.0, N*T, N, endpoint=False)

# Generate filter
filter_size = 101 # adjust this to change the filter size
filter = np.ones(filter_size) / filter_size

# Apply filter to signal
filtered_y = np.convolve(y, filter, mode='same')

# Plot results
fig, axs = plt.subplots(3)
fig.suptitle('Frecuencias de datos obtenidas ')
axs[0].grid()
axs[0].set_title('muestra base ')
axs[0].plot(x, y)

axs[1].grid()
axs[1].set_title('FFT ')
yf = fft(y)
xf = fftfreq(N, T)[:N//2]
axs[1].plot(xf, 2.0/N * np.abs(yf[0:N//2]))

axs[2].grid()
axs[2].set_title('Filtro de media móvil')
axs[2].plot(x, filtered_y)

plt.show()
