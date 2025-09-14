from flask import Flask, jsonify
import spidev
import time
from gpiozero import LED
from threading import Thread

# Setup Flask
app = Flask(__name__)

# Setup LEDs
LED1 = LED(2)
LED2 = LED(3)
leds = [LED1, LED2]
for l in leds:
    l.off()

# Setup SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

# Shared sensor data
sensor_data = {"ldr": 0, "voltage": 0}

# Read channel
def channel_readings(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Convert to voltage
def convert_to_voltage(data, vref=3.3):
    return (data * vref) / 1023

# Background thread to read sensors
def read_sensors():
    while True:
        ldr_value = channel_readings(0)
        ldr_voltage = convert_to_voltage(ldr_value)

        # Update global data
        sensor_data["ldr"] = ldr_value
        sensor_data["voltage"] = round(ldr_voltage, 2)

        # Control LEDs
        if ldr_value > 550:
            LED1.on()
            LED2.off()
        else:
            LED1.off()
            LED2.on()

        time.sleep(1)

# Flask route to provide JSON data
@app.route("/data")
def get_data():
    return jsonify(sensor_data)

@app.route("/")
def index():
    return app.send_static_file("index.html")  # put your HTML in 'static' folder

if __name__ == "__main__":
    # Start sensor reading in a separate thread
    Thread(target=read_sensors, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, debug=False)
