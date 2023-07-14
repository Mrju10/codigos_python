import machine
import time
import network
import urequests as requests

# Configurar la conexión WiFi
ssid = "SSID"
password = "password"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    time.sleep(1)

print("Conexión WiFi establecida")

pin_adc = machine.ADC(26)
reference_voltage = 3.3
SERVER_URL = 'http://URL.COM'
SERVER_ajax = SERVER_URL + '/historial_ajax'  # Reemplaza con la dirección IP de tu servidor

# Identificador único de la Raspberry Pi Pico
identificador = 'rp1'

led_pwm = machine.PWM(machine.Pin(2))
led_pwm.freq(1000)

while True:
    value = pin_adc.read_u16()
    voltage = (value / 65535) * reference_voltage

    # Crear una solicitud HTTP GET con el identificador y el valor
    url = SERVER_URL + "?valor=" + str(voltage) + "&id=" + identificador
    print(url)
    response = requests.get(url)
    response.close()

    # Obtener los promedios de los datos
    response = requests.get(SERVER_ajax)
    data = response.json()
    promedios = data['promedios']
    response.close()

    # Calcular el promedio general de todas las Raspberry Pi
    promedio_general = sum(promedios.values()) / len(promedios)

    # Escalar el valor del promedio general al rango del LED PWM
    duty_cycle = int((promedio_general / reference_voltage) * 1023)
    print(duty_cycle)
    # Actualizar la intensidad del LED PWM
    led_pwm.duty_u16(duty_cycle)

    time.sleep(0.5)
