print("Analog to Digital convertor")


import spidev   
import time     


spi = spidev.SpiDev()       
spi.open(0, 0)              
spi.max_speed_hz = 1350000   # this is always on the datasheet


def channel_readings(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data


def convert_to_voltage(data, vref=3.3):
    voltage = (data * vref) / 1023
    return voltage


try:
    print("Reading LDR on CH0...")
    while True:
        ldr_value = channel_readings(0)             
        ldr_voltage = convert_to_voltage(ldr_value)
        print(f"LDR digital: {ldr_value}, Voltage: {ldr_voltage:.2f} V")
        time.sleep(1)  

except KeyboardInterrupt:
    spi.close()  
    print("\nProgram stopped")
