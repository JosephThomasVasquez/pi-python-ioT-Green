import Adafruit_DHT
import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Set OLED Display size
oled_width = 128
oled_height = 32

# Set OLED display pins and configuration parameters
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
address = i2c.scan()[0]
oled = SSD1306_I2C(oled_width, oled_height, i2c, address)

oled.fill(0);
oled.text("Raspberry Pi", 5, 5)
oled.text("3 B+", 5, 15)
oled.show()

#Set DHT11 Humidity and Temperature sensor pins and library
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    fahrenheit = 0

    if humidity is not None and temperature is not None:
        fahrenheit = (temperature * 9 / 5) + 32
        print("Temp={0:0.1f}F° Humidity={1:0.1f}%".format(fahrenheit, humidity))
    time.sleep(3)
