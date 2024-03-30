import RPi.GPIO as GPIO
import time

# Define constants
R1 = 10000  # Resistance at 25°C, in ohms
B = 3950    # Beta value of the thermistor
T0 = 298.15 # Temperature at 25°C, in Kelvin

# Pin configuration
therm_pin = 18  # Assuming the thermistor is connected to GPIO 18

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(therm_pin, GPIO.IN)

def get_temp(R, B, T0, pin):
    # Read analog value from thermistor
    adc_value = GPIO.input(pin)
    
    # Convert ADC value to resistance
    R2 = R1 * (1023.0 / adc_value - 1.0)
    
    # Convert resistance to temperature using Steinhart-Hart equation
    temp = 1.0 / (1.0 / T0 + 1.0 / B * (1.0 / (R2 / R) - 1.0))
    
    # Convert temperature from Kelvin to Celsius
    temp -= 273.15
    
    return temp

try:
    while True:
        # Get temperature
        temp = get_temp(R1, B, T0, therm_pin)
        
        # Print temperature
        print("Thermistor temperature: {:.2f} °C".format(temp))
        print("----------------------")
        
        # Wait for next measurement
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
