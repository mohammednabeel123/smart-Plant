import spidev
import time

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # bus 0, device 0
spi.max_speed_hz = 1350000

def read_channel(channel):
    # MCP3008 expects 3 bytes: start bit, single/diff + channel, 0
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    while True:
        value = read_channel(0)       # CH0 where MQ-2 is connected
        voltage = (value / 1023.0) * 3.3  # Convert to voltage (MCP3008 Vref = 3.3V)
        print(f"MQ-2 Voltage: {voltage:.2f} V")
        time.sleep(0.5)
finally:
    spi.close()
