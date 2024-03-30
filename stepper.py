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

def set_angle(angle):
    # Convert angle to duty cycle
    duty_cycle = angle / 18.0 + 2.5
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Give time for the servo to reach the desired position

try:
    while True:
        # Move servo to 0 degrees
        set_angle(0)
        time.sleep(1)

        # Move servo to 90 degrees
        set_angle(90)
        time.sleep(1)

        # Move servo to 180 degrees
        set_angle(180)
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Clean up GPIO
GPIO.cleanup()
