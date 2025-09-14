print("I'm the sensors")

from flask import Flask, jsonify
import adafruit_dht
import board

app = Flask(__name__)

# Initialize DHT22 once
dht_sensor = adafruit_dht.DHT22(board.D4)

# Simulated values for LDR and pump (replace with real sensor readings later)
ldr_value = 450        # Example light level (0–1023)
pump_status = "OFF"    # Example pump status

@app.route("/")
def index():
    return app.send_static_file("index.html")  # Place this file in 'static/' folder

@app.route("/data")
def get_sensor_data():
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity

        return jsonify({
            "ldr": ldr_value,
            "temperature": round(temperature, 1) if temperature is not None else "--",
            "humidity": round(humidity, 1) if humidity is not None else "--",
            "pump": pump_status
        })

    except RuntimeError as e:
        return jsonify({
            "ldr": ldr_value,
            "temperature": "--",
            "humidity": "--",
            "pump": pump_status,
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
