import serial
import time
phone_num = input('Input your phone number: ')
ser = serial.Serial("/dev/ttyUSB0",115200)
W_buff = ["AT\r\n", "AT+CMGF=1\r\n", "AT+CSCA=\"+447785016005\"\r\n","AT+CMGS=\"+447864906108\"\r\n","helloworld3\x1a"]
ser.write(W_buff[0].encode())
ser.flushInput()
data = ""
num = 0
try:
	while True:
		while ser.inWaiting() > 0:
			data += ser.read(ser.inWaiting()).decode()
		if data != "":
			print(data)
			if num < 3:
				time.sleep(1)
				ser.write(W_buff[num+1].encode())
			if num == 3:
				#print W_buff[4]
				time.sleep(0.5)
				ser.write(W_buff[4].encode())
				time.sleep(0.5)
				#ser.write("\x1a\r\n".encode())# 0x1a : send   0x1b : Cancel send
			num += 1
			data = ""
			
except KeyboardInterrupt:
	if ser != None:
		ser.close()
