print("I'm the sensors")

import adafruit_dht

sDHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # BCM numbering, GPIO4

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

if humidity is not None and temperature is not None:
    print(f"Temp={temperature:.1f}C  Humidity={humidity:.1f}%")
else:
    print("Failed to retrieve data from DHT22 sensor")

