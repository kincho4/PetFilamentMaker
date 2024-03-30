import RPi.GPIO as GPIO
import time

# Thermistor parameters
R0 = 10000  # Resistance at 25 degrees Celsius
beta = 3950  # Beta value of the thermistor

# GPIO pin
therm_pin = 12  # Use GPIO18 (pin 12) for thermistor input

def get_temp():
    # Setup GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(therm_pin, GPIO.IN)

    # Read analog value
    analog_value = 0
    for i in range(10):
        analog_value += GPIO.input(therm_pin)
        time.sleep(0.01)
    analog_value /= 10.0

    # Calculate resistance of the thermistor
    R = (analog_value * R0) / (1023 - analog_value)

    # Calculate temperature in Celsius
    T = 1 / (1 / 298.15 + 1 / beta * (1 / (273.15 + 25) - 1 / (R / 1000)))
    T -= 273.15  # Convert Kelvin to Celsius

    return T

try:
    while True:
        temp = get_temp()
        print("Thermistor temperature:", temp)
        print("----------------------")
        time.sleep(1)  # Wait 1 second before next measurement

except KeyboardInterrupt:
    GPIO.cleanup()
