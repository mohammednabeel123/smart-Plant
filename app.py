print("welcome to  Smart Plant")
from flask import Flask, jsonify
import spidev
import time
from gpiozero import LED
from threading import Thread
import adafruit_dht
import board


app = Flask(__name__)


LED1 = LED(2)
LED2 = LED(3)
leds = [LED1, LED2]
for l in leds:
    l.off()


spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def convert_to_voltage(data, vref=3.3):
    return (data * vref) / 1023


dht_sensor = adafruit_dht.DHT22(board.D4)


sensor_data = {
    "ldr": 0,
    "voltage": 0,
    "temperature": 0,
    "humidity": 0,
    "pump": "OFF"
}


def read_sensors():
    while True:
        try:
            # LDR
            ldr_value = read_channel(0)
            sensor_data["ldr"] = ldr_value
            sensor_data["voltage"] = round(convert_to_voltage(ldr_value), 2)

            # LEDs control based on light
            if ldr_value > 550:
                LED1.on()
                LED2.off()
            else:
                LED1.off()
                LED2.on()

            # DHT22
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity
            sensor_data["temperature"] = round(temperature, 1) if temperature is not None else "--"
            sensor_data["humidity"] = round(humidity, 1) if humidity is not None else "--"

            # Pump status example
            sensor_data["pump"] = "ON" if ldr_value < 400 else "OFF"

        except RuntimeError as e:
            sensor_data["temperature"] = "--"
            sensor_data["humidity"] = "--"
            sensor_data["pump"] = "OFF"

        time.sleep(1)


@app.route("/")
def index():
    return app.send_static_file("index.html")  # Make sure index.html is in 'static/'

@app.route("/data")
def get_data():
    return jsonify(sensor_data)


if __name__ == "__main__":
    Thread(target=read_sensors, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, debug=False)
