import Adafruit_DHT
import time

import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Set busio I2C with SCL and SDA connections
i2c = busio.I2C(board.SCL, board.SDA)

# Set OLED Display size
oled_width = 128
oled_height = 32
BORDER = 1

oled = adafruit_ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Set OLED display pins and configuration parameters
oled.fill(0)
oled.show()

#Set DHT11 Humidity and Temperature sensor pins and library
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def readHumidityTemperature():

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new("1", (oled.width, oled.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a white background
    draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

    # Draw a smaller inner rectangle
    draw.rectangle(
        (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
        outline=0,
        fill=0,
    )

    # Load default font.
    font = ImageFont.load_default()


    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    fahrenheit = 0

    if humidity is not None and temperature is not None:

        # Draw Some Text
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * 9 / 5) + 32
        
        text = "T:" + str(fahrenheit) + "F°" + " H:" + str(humidity) + "%"
        
        print("Temp={0:0.1f}F° Humidity={1:0.1f}%".format(fahrenheit, humidity))
        (font_width, font_height) = font.getsize(text)
        
        draw.text(
            (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
            text,
            font=font,
            fill=200,
        )

        # Display image
        oled.image(image)
        oled.show()
        
    time.sleep(3)

while True:
    readHumidityTemperature()
