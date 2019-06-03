import Adafruit_BBIO.GPIO as GPIO
import time


GPIO.setup("P8_8",GPIO.OUT)
GPIO.setup("P8_10",GPIO.OUT)
GPIO.setup("P8_12",GPIO.OUT)
GPIO.setup("P8_14",GPIO.OUT)

#wait=1
wait=0.7*10**-3   #ms, funciona entren [0.7 - 10] ms  (despacio, rapido)
nVueltas=3

for i in range(512*nVueltas):
        for j in range(4):
                GPIO.output("P8_8",GPIO.HIGH if (8+j*2)==8 else GPIO.LOW)
                GPIO.output("P8_10",GPIO.HIGH if (8+j*2)==10 else GPIO.LOW)
                GPIO.output("P8_12",GPIO.HIGH if (8+j*2)==12 else GPIO.LOW)
                GPIO.output("P8_14",GPIO.HIGH if (8+j*2)==14 else GPIO.LOW)
		time.sleep(wait)



