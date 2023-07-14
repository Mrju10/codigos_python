import subprocess
import RPi.GPIO as GPIO

# Establecer el modo de BCM
GPIO.setmode(GPIO.BCM)

# Establecer los botones GPIO 12 y 25 como entradas
GPIO.setup(12, GPIO.IN)
GPIO.setup(25, GPIO.IN)

# Ruta del archivo compilado de C
ruta_archivo = "/home/pi/Desktop/tesis/vf"

while True:
    # Leer el estado de los botones GPIO 12 y 25
    estado_12 = GPIO.input(12)
    estado_25 = GPIO.input(25)

    # Si el botón GPIO 12 está presionado, ejecutar el archivo compilado de C
    if estado_12 == GPIO.HIGH:
        subprocess.call(ruta_archivo)

    # Si el botón GPIO 25 está presionado, ejecutar el archivo Python
    if estado_25 == GPIO.HIGH:
        subprocess.call(["python", "/home/pi/Desktop/tesis/reconocimiento/conversion_wav.py"])
