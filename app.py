print("Welcome to Smart Plant")

from flask import Flask, jsonify
import spidev
import time
from gpiozero import LED
from threading import Thread
import adafruit_dht
import board

app = Flask(__name__, static_folder="static")

# LEDs
LED1 = LED(2)
LED2 = LED(3)
leds = [LED1, LED2]
for l in leds:
    l.off()

# SPI setup
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def convert_to_voltage(data, vref=3.3):
    return (data * vref) / 1023

# DHT22
dht_sensor = adafruit_dht.DHT22(board.D4)

# Shared sensor data
sensor_data = {
    "ldr": 0,
    "ldr_voltage": 0,
    "mq2": 0,
    "mq2_voltage": 0,
    "temperature": "--",
    "humidity": "--",
    "pump": "OFF"
}

def read_sensors():
    while True:
        try:
            # LDR on CH0
            ldr_value = read_channel(0)
            sensor_data["ldr"] = ldr_value
            sensor_data["ldr_voltage"] = round(convert_to_voltage(ldr_value), 2)

            # MQ-2 on CH1
            mq2_value = read_channel(1)
            sensor_data["mq2"] = mq2_value
            sensor_data["mq2_voltage"] = round(convert_to_voltage(mq2_value), 2)

            # LEDs toggle based on light
            if ldr_value > 550:
                LED1.on()
                LED2.off()
            else:
                LED1.off()
                LED2.on()

            # DHT22
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity
            sensor_data["temperature"] = round(temperature, 1) if temperature else "--"
            sensor_data["humidity"] = round(humidity, 1) if humidity else "--"

            # Example pump logic
            sensor_data["pump"] = "ON" if ldr_value < 400 else "OFF"

        except RuntimeError:
            sensor_data["temperature"] = "--"
            sensor_data["humidity"] = "--"
            sensor_data["pump"] = "OFF"

        time.sleep(1)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/data")
def get_data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    Thread(target=read_sensors, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, debug=False)
