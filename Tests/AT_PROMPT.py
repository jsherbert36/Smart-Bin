import serial
import time
ser = serial.Serial("/dev/ttyUSB0",115200)
ser.flushInput()
data = ""
try:
    while True:
        temp_input = input("~")+"\r\n"
        ser.write(temp_input.encode())
        while data == "":
            while ser.inWaiting() > 0:
                data += ser.read(ser.inWaiting()).decode()
        print(data)
        data = ""
except KeyboardInterrupt:
    if ser != None:
        ser.close()
