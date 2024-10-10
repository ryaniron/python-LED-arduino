import RPi.GPIO as GPIO #this library needs to be installed to the raspberry pi in order to work
import time

# LCD setup
# Define GPIO pin numbers for LCD control and data lines
LCD_RS = 7
LCD_E = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18

# LCD configuration constants
LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0
E_PULSE = 0.0005  # Pulse duration for enabling LCD
E_DELAY = 0.0005  # Delay between pulses

# APB sensor setup
APB_PIN = 14

# Define GPIO pin numbers for APB sensor (adjust as needed)
RED_PIN = 17
GREEN_PIN = 18
BLUE_PIN = 27


def setup_lcd():
    """Setup GPIO pins for LCD"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LCD_E, GPIO.OUT)
    GPIO.setup(LCD_RS, GPIO.OUT)
    GPIO.setup(LCD_D4, GPIO.OUT)
    GPIO.setup(LCD_D5, GPIO.OUT)
    GPIO.setup(LCD_D6, GPIO.OUT)
    GPIO.setup(LCD_D7, GPIO.OUT)

def lcd_init():
    """Initialize LCD"""
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)  # 4-bit mode, 2 lines, 5x8 font
    lcd_byte(0x0C, LCD_CMD)  # Display on, cursor off, blink off
    lcd_byte(0x06, LCD_CMD)  # Entry mode, increment cursor
    lcd_byte(0x01, LCD_CMD)  # Clear display

def lcd_byte(bits, mode):
    """Send byte to LCD"""
    GPIO.output(LCD_RS, mode)  # RS: High = character, Low = command
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    # Set data bits
    if bits & 0x10 == 0x10:
        GPIO.output(LCD_D4, True)
    if bits & 0x20 == 0x20:
        GPIO.output(LCD_D5, True)
    if bits & 0x40 == 0x40:
        GPIO.output(LCD_D6, True)
    if bits & 0x80 == 0x80:
        GPIO.output(LCD_D7, True)
    # Toggle enable
    lcd_toggle_enable()
    # Reset data bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x01 == 0x01:
        GPIO.output(LCD_D4, True)
    if bits & 0x02 == 0x02:
        GPIO.output(LCD_D5, True)
    if bits & 0x04 == 0x04:
        GPIO.output(LCD_D6, True)
    if bits & 0x08 == 0x08:
        GPIO.output(LCD_D7, True)
    lcd_toggle_enable()

def lcd_toggle_enable():
    """Toggle enable for transferring data to LCD"""
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)

def lcd_string(message, line):
    """Display string on LCD"""
    message = message.ljust(LCD_WIDTH, " ")  # Pad message to LCD width
    lcd_byte(line, LCD_CMD)  # Set LCD line
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)  # Send character to LCD

def setup_apb_sensor():
    """Setup GPIO pin for APB sensor"""
    GPIO.setup(APB_PIN, GPIO.IN)

def read_apb_concentration():
    """Read concentration from APB sensor"""
    # Read RGB values from the sensor (assuming separate pins for RGB)
    red = GPIO.input(RED_PIN)
    green = GPIO.input(GREEN_PIN)
    blue = GPIO.input(BLUE_PIN)
    # Check if the detected color is green (adjust thresholds as needed)
    if green > red and green > blue:
        return green
    else:
        return 0

def main():
    try:
        # Setup LCD and APB sensor
        setup_lcd()
        lcd_init()
        setup_apb_sensor()
        # Main loop
        while True:
            concentration = read_apb_concentration()
            lcd_string("Green: {}".format(concentration), LCD_LINE_1)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
