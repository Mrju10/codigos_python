import machine
import time

# Configurar el pin del ADC
pin_adc = machine.ADC(26)

# Configurar el pin del PWM
pin_pwm = machine.PWM(machine.Pin(12))

# Configurar la frecuencia del PWM a 5 kHz
pwm_frequency = 5000
pin_pwm.freq(pwm_frequency)

# Configurar voltaje de referencia a 3.3V
reference_voltage = 3.3

# Rango máximo del ADC
adc_range = 65535

# Rango máximo del PWM
pwm_range = 1023

# Variables para almacenar el último valor del ADC y el PWM
last_adc_value = 0
last_pwm_value = 0

while True:
    # Leer el valor del ADC
    adc_value = pin_adc.read_u16()

    # Si el valor del ADC ha cambiado, actualizar la intensidad
    if adc_value != last_adc_value:
        # Convertir el valor del ADC a un porcentaje
        percentage = (adc_value / adc_range) * 100

        # Convertir el porcentaje al valor del PWM
        pwm_value = int((percentage / 100) * pwm_range)

        # Configurar el valor del PWM
        pin_pwm.duty_u16(pwm_value)

        # Actualizar el último valor del ADC y el PWM
        last_adc_value = adc_value
        last_pwm_value = pwm_value

    # Imprimir los valores del ADC y el último valor del PWM
    print("Valor analógico:", adc_value)
    print("Último valor PWM:", last_pwm_value)

    # Esperar 1 segundo
    time.sleep(1)
