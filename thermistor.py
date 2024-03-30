import RPi.GPIO as GPIO
import time
import math

# Set the GPIO pin number where the NTC thermistor is connected
NTC_PIN = 17

def read_adc():
    adc_value = 0
    GPIO.setup(NTC_PIN, GPIO.OUT)
    GPIO.output(NTC_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(NTC_PIN, GPIO.IN)

    while GPIO.input(NTC_PIN) == GPIO.LOW:
        continue
    while GPIO.input(NTC_PIN) == GPIO.HIGH:
        continue

    for i in range(8):
        GPIO.setup(NTC_PIN, GPIO.OUT)
        GPIO.output(NTC_PIN, GPIO.LOW)
        time.sleep(0.00001)
        GPIO.setup(NTC_PIN, GPIO.IN)
        adc_value <<= 1
        if GPIO.input(NTC_PIN) == GPIO.HIGH:
            adc_value |= 0x1
        time.sleep(0.00001)

    return adc_value

def convert_to_temperature(adc_value):
    try:
        R = 10 * 1000 * (1023 / adc_value - 1)
        T0 = 25
        R0 = 10 * 1000
        B = 3950
        T = 1 / (1 / (T0 + 273.15) + (1 / B) * math.log(R / R0))
        T -= 273.15
        return T
    except ZeroDivisionError:
        return -1  # Handle division by zero error

def main():
    GPIO.setmode(GPIO.BCM)
    try:
        while True:
            adc_value = read_adc()
            temperature = convert_to_temperature(adc_value)
            if temperature != -1:
                print("Temperature:", temperature, "°C")
            else:
                print("Error: Division by zero")
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
