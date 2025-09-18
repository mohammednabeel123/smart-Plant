Smart Environment Monitor 🌱💡

Smart Environment Monitor is a full-stack IoT project designed to track and control environmental conditions using a Raspberry Pi. It collects real-time data from various sensors, displays it locally on an OLED, and can trigger actuators like pumps or fans automatically.

This project demonstrates practical embedded systems, IoT, SPI communication, and full-stack integration.

Project Overview

Monitoring the environment is important for plants, rooms, or labs. This project uses sensors to measure:

Light (LDR)

Air quality (MQ-2 gas sensor)

Temperature and humidity (DHT22)

Based on these readings, the system can automate actions like turning on a pump or fan and display live readings on an OLED screen.

#How It Works

Reading Analog Sensors with MCP3008 (SPI):

Sensors like the LDR and MQ-2 gas sensor produce analog voltages.

Raspberry Pi cannot read analog signals directly, so we use the MCP3008 ADC to convert analog signals to digital.

Communication happens over SPI (Serial Peripheral Interface) — imagine the Pi asking, “What’s the sensor value?” and the ADC replying with a number.

Temperature & Humidity (DHT22):

The DHT22 provides digital readings for temperature and humidity.

Python reads these values directly and updates the display and actuator logic.



OLED Display (I²C):

A small 128×64 OLED display shows live readings like light, gas, temperature, humidity, and pump status.

Using I²C communication, the Pi sends the data to the OLED screen so you can see sensor updates in real time.

Web Dashboard (Future Expansion):

Flask API already serves the sensor data at /data for remote monitoring.

You can connect this to a web dashboard or mobile app to view readings from anywhere.

#Hardware Components

Raspberry Pi 3B+

MCP3008 ADC

LDR (Light Dependent Resistor)

MQ-2 Gas Sensor

DHT22 Temperature & Humidity Sensor


LEDs for status indicators

OLED Display (128×64, I²C)

#Software Components

Python 3

Libraries: RPi.GPIO, spidev, adafruit_dht, adafruit_ssd1306, Pillow

Flask (for web API and future dashboard)


Setup Instructions

Clone the repository:

git clone https://github.com/mohammednabeel123/smart environment Monitor.git
cd smart environment Monitor


Install dependencies on Raspberry Pi:

sudo apt update
sudo apt install python3 python3-pip -y
pip3 install RPi.GPIO spidev adafruit-circuitpython-dht adafruit-circuitpython-ssd1306 Pillow flask


Run the project:

python3 app.py


Optional: Use VS Code Remote-SSH to edit and run code directly on the Pi.

Future Improvements