print("I'm the sensors")

import time
import adafruit_dht
import board  # Needed for pin definitions

# Initialize DHT22 on GPIO4
dht_sensor = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity

        if humidity is not None and temperature is not None:
            print(f"Temp={temperature:.1f}°C  Humidity={humidity:.1f}%")
        else:
            print("Sensor returned None values")

    except RuntimeError as e:
        # DHT sensors are a bit finicky, they often throw errors — ignore and retry
        print(f"Error reading sensor: {e}")

    time.sleep(2)  # Wait before retrying
