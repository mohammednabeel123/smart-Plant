print("I'm the sensors")

from flask import Flask
import adafruit_dht
import board

app = Flask(__name__)

# Initialize DHT22 once
dht_sensor = adafruit_dht.DHT22(board.D4)

@app.route("/")
def DHT22sensor():
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity

        if humidity is not None and temperature is not None:
            return f"<h1>🌱 Smart Plant Dashboard</h1><p>Temp={temperature:.1f}°C<br>Humidity={humidity:.1f}%</p>"
        else:
            return "<p>Sensor returned None values</p>"

    except RuntimeError as e:
        return f"<p>Error reading sensor: {e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
