print("Analog to Digital convertor")

import spidev
import time
from gpiozero import LED
from flask import Flask, jsonify

# Setup LEDs
LED1 = LED(2)
LED2 = LED(3)
leds = [LED1, LED2]
for l in leds:
    l.off()

# Setup SPI
spi = spidev.SpiDev()
spi.open(0, 0)               # bus 0, device 0 (CE0)
spi.max_speed_hz = 1350000   # from MCP3008 datasheet

# Read channel (0–7)
def channel_readings(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])  # 3-byte transfer
    print(adc)                                   # raw bytes
    data = ((adc[1] & 3) << 8) + adc[2]          # 10-bit value (0–1023)
    print(data)
    return data

# Convert ADC to voltage
def convert_to_voltage(data, vref=3.3):
    voltage = (data * vref) / 1023
    return voltage

try:
    print("Reading LDR on CH0...")
    while True:
        ldr_value = channel_readings(0)             # digital 0–1023
        ldr_voltage = convert_to_voltage(ldr_value) # in volts

        # Control LEDs based on brightness
        if ldr_value > 550:      # threshold chosen in digital counts
            LED1.on()
            LED2.off()
        elif ldr_value < 550:
            LED1.off()
            LED2.on()
        else:  # exactly 550
            LED1.on()
            LED2.off()

        print(f"LDR digital: {ldr_value}, Voltage: {ldr_voltage:.2f} V")
        time.sleep(1)

except KeyboardInterrupt:
    spi.close()
    print("\nProgram stopped")
