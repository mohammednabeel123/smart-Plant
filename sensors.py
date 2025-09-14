import spidev
import time
 
spi = spidev.SpiDev()
spi.open(0,1)   

def read_channel(channel):
    #MCP3008 expects 3 bytes eg [start, diff+channel + 0 ]
    adc = spi.xfer2([1,(8 + channel) << 4, 0])
    data = ((adc[1] & 3 ) << 8) + adc[2]
    return data

try:
    while True:
        value = read_channel(1)
        voltage = (value / 1023.0) * 3.3
        print(f"MQ-2 Voltage: {voltage:.2f} v")
        time.sleep(0.5)
finally:
    spi.close()
