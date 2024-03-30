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

# Configure A4988 for high torque
# You might need to adjust these values based on your motor and driver
GPIO.output(dir_pin, GPIO.LOW)  # Set direction to counterclockwise
GPIO.output(step_pin, GPIO.LOW)  # Ensure step pin is initially low

# Initialize PWM
pwm = GPIO.PWM(step_pin, 50)  # 50 Hz frequency
pwm.start(0)  # Start PWM with duty cycle 0

def rotate_motor():
    # Generate pulses to rotate motor
    for _ in range(200):  # 200 steps for one revolution
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(0.005)  # Adjust delay for desired speed
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(0.005)  # Adjust delay for desired speed

try:
    while True:
        # Rotate motor counterclockwise
        rotate_motor()

except KeyboardInterrupt:
    pass

# Clean up GPIO
GPIO.cleanup()
