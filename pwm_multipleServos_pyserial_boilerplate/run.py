import serial
import time
import struct
# Assign Arduino's serial port address
#   Windows example
#     usbport = 'COM3'
#   Linux example
#     usbport = '/dev/ttyUSB0'
#   MacOSX example
#     usbport = '/dev/tty.usbserial-FTALLOK2'
# basically just see what ports are open  - >>> ls /dev/tty*

# Set up serial baud rate
usbport = '/dev/ttyS3'

ser = serial.Serial(usbport,9600,timeout=1)
# time.sleep is necessary - it takes some time to open serial port
time.sleep(2)

def write(i):
    ser.write(struct.pack('>BBB',255,0,i))

write(0)
time.sleep(1)
