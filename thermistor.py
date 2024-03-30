import RPi.GPIO as GPIO
import time

# GPIO pin
therm_pin = 12  # Use GPIO18 (pin 12) for thermistor input

def get_analog_reading():
    # Setup GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(therm_pin, GPIO.IN)

    # Read analog value
    analog_value = GPIO.input(therm_pin)

    return analog_value

try:
    while True:
        analog_value = get_analog_reading()
        print("Raw analog reading:", analog_value)

        time.sleep(1)  # Wait 1 second before next measurement

except KeyboardInterrupt:
    GPIO.cleanup()
