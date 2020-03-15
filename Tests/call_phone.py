import serial
import time
phone_num = input('Enter phone number: ')
ser = serial.Serial(port = "/dev/ttyUSB0", baudrate = 115200)
W_buf_logoin = "AT+CREG?\r\n"
W_buf_phone =  "ATD" + phone_num+ ";\r\n"
ser.write(W_buf_logoin.encode())
ser.flushInput()
data = ""
try:
    while True:
        while ser.inWaiting() > 0:
            data += (ser.read(ser.inWaiting())).decode()
            time.sleep(0.0001)
        if data != "":
            print(data)
            if "CREG" in data:
                print("call phone")
                ser.write(W_buf_phone.encode())
            data = ""
except KeyboardInterrupt:
    if ser != None:
        ser.close()
		
