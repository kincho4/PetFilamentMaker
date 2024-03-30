import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define GPIO pins for A4988
step_pin = 11
dir_pin = 13

# Set GPIO pins as output
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)

# Initialize PWM
pwm = GPIO.PWM(step_pin, 50)  # 50 Hz frequency
pwm.start(0)  # Start PWM with duty cycle 0

def rotate_motor(direction):
    # Set direction
    GPIO.output(dir_pin, direction)

    # Generate pulses to rotate motor
    for _ in range(200):  # 200 steps for one revolution
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(0.005)  # Adjust delay for desired speed
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(0.005)  # Adjust delay for desired speed

try:
    while True:
        # Rotate motor clockwise
        rotate_motor(GPIO.HIGH)

        # Rotate motor counterclockwise
        rotate_motor(GPIO.LOW)

except KeyboardInterrupt:
    pass

# Clean up GPIO
GPIO.cleanup()
