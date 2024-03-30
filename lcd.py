import smbus
import time

# Define I2C parameters
I2C_ADDR = 0x27  # I2C address of the LCD
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1  # Mode - Sending data
LCD_CMD = 0  # Mode - Sending command

LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

LCD_BACKLIGHT = 0x08  # On
ENABLE = 0b00000100  # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

# Open I2C interface
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = 1 for character
    #        0 for command

    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    # High bits
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    # Low bits
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    # Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)

def lcd_string(message, line):
    # Send string to display
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

def lcd_clear():
    # Clear the LCD display
    lcd_byte(0x01, LCD_CMD)

if __name__ == '__main__':
    try:
        # Main program block
        lcd_byte(0x33, LCD_CMD)  # Initialize
        lcd_byte(0x32, LCD_CMD)  # Set to 4-bit mode
        lcd_byte(0x06, LCD_CMD)  # Cursor move direction
        lcd_byte(0x0C, LCD_CMD)  # Turn cursor off
        lcd_byte(0x28, LCD_CMD)  # 2 lines, 5x8 character matrix

        lcd_clear()

        while True:
            lcd_string("Hello, World!", LCD_LINE_1)
            lcd_string("LCD with I2C", LCD_LINE_2)
            time.sleep(3)
            lcd_clear()
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    finally:
        lcd_clear()