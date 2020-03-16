import RPi.GPIO as GPIO
import time
import serial
import time
phone_num = input('Input your phone number: ')
ser = serial.Serial("/dev/ttyUSB0",115200)
W_buff = ["AT\r\n", "AT+CMGF=1\r\n", "AT+CSCA=\"+447785016005\"\r\n","AT+CMGS=\"XXXXXXXXXXXX\"\r\n","BIN IS FULL\x1a"]
ser.write(W_buff[0].encode())
ser.flushInput()
data = ""
num = 0
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
full = False
 
def distance():
    GPIO.output(GPIO_TRIGGER, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2 
    return distance
 
if __name__ == "__main__":
    while True:
        while ser.inWaiting() > 0:
            data += ser.read(ser.inWaiting()).decode()
        if data != "":
            print(data)
            if 'CMTI' in data:
                if 'STATUS' in data:
                    print(bin_height - distance()
            if num < 3:
                time.sleep(1)
                ser.write(W_buff[num+1].encode())
            if num == 3:
                if distance < 5:
                    full = True
                time.sleep(10)
                if distance < 5:
                    full = True
                else:
                    full = False
                if full == True:
                    ser.write(W_buff[4].encode())
            num += 1
            data = ""
                        
