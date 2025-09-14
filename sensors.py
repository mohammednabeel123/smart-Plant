import spidev
import time

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # bus 0, device 0
spi.max_speed_hz = 1350000


