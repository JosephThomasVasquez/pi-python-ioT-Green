import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        fahrenheit = (temperature * 9/5) + 32
        print("Temp={0:0.1f}F Humidity={1:0.1f}".format(fahrenheit, humidity))
    else:
        print("Sensor Error. Check wiring!")
    time.sleep(3)
