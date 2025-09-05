Smart Plant 🌱

Smart Plant is a full-stack IoT project designed to monitor and automate the care of your plants. Using sensors and actuators connected to a Raspberry Pi, it provides real-time monitoring of soil moisture, ambient light, and environmental conditions, and automatically waters the plant or triggers alerts when needed.

Features

Soil Moisture Monitoring: Tracks soil moisture levels using a sensor and logs readings.

Automated Watering: Activates a small pump to water the plant when soil is dry.

Light Monitoring: Uses an LDR to detect ambient light.

Fan Control: Turns on a fan when environmental conditions require it.

Motion Detection: Stops watering or activates safety protocols if motion is detected via a PIR sensor.

Modular Code: Sensors, actuators, and configuration separated into multiple Python files for easy maintenance.

Full Stack Ready: Designed to connect with web dashboards or cloud platforms in future expansions.

Hardware Components

Raspberry Pi 3B+

MCP3008 ADC

Soil Moisture Sensor

LDR (Light Dependent Resistor)

Small Water Pump (6V, 120L/H)

Fan

PIR Motion Sensor (HC-SR501)

Software Components

Python 3

Libraries: RPi.GPIO, spidev (for MCP3008), others as needed

VS Code (with Remote-SSH for Raspberry Pi development)

Project Structure
smart-Plant/
│
├── main.py            # Main program
├── sensors.py         # Sensor reading functions
├── actuators.py       # Actuator control functions
├── mcp3008.py         # ADC interfacing
├── config.py          # Configuration for pins and thresholds
└── README.md          # Project description

Setup Instructions

Clone the repository:

git clone https://github.com/mohammednabeel123/smart-Plant.git
cd smart-Plant


Install dependencies on Raspberry Pi:

sudo apt update
sudo apt install python3 python3-pip -y
pip3 install RPi.GPIO spidev


Run the project:

python3 main.py


Connect via VS Code (optional): Use the Remote-SSH extension to edit and run code directly on the Pi.

Future Improvements

Add web dashboard for real-time monitoring

Multilingual support for global use

Integration with AI for plant care recommendations

Logging data to cloud for analytics

License

This project is open-source and free to use under the MIT License.
