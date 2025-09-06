print("Im  the ADC")

# smart_plant_ldr.py
# Read LDR value via MCP3008 and convert to voltage
# Raspberry Pi + MCP3008 + LDR Voltage Divider

import spidev   # SPI communication
import time     # Delay

# ------------------------
# SPI Setup
# ------------------------
spi = spidev.SpiDev()       # Create SPI object
spi.open(0, 0)              # Open bus 0, device CE0
spi.max_speed_hz = 1350000  # Set SPI speed

# ------------------------
# Function to read MCP3008 channel
# ------------------------
def read_channel(channel):
    """
    Read data from MCP3008 ADC channel (0-7)
    Returns integer value 0-1023
    """
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# ------------------------
# Convert digital value to voltage
# ------------------------
def convert_to_voltage(data, vref=3.3):
    """
    Convert 10-bit ADC value to voltage
    """
    voltage = (data * vref) / 1023
    return voltage

# ------------------------
# Main loop
# ------------------------
try:
    print("Reading LDR on CH0...")
    while True:
        ldr_value = read_channel(0)             # Read CH0
        ldr_voltage = convert_to_voltage(ldr_value)
        print(f"LDR digital: {ldr_value}, Voltage: {ldr_voltage:.2f} V")
        time.sleep(1)  # Delay 1 second

except KeyboardInterrupt:
    spi.close()  # Close SPI safely on Ctrl+C
    print("\nProgram stopped")
