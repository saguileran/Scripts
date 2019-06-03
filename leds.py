import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()
GPIO.setup("P9_11", GPIO.OUT )
GPIO.setup("P9_13", GPIO.IN )
#GPIO.setup("")

value=ADC.read("P9_13")
for i in range(1000000):
   #print(GPIO.input("P9_13"))
   print(value*1.8)
   time.sleep(1)
#GPIO.output("P9_11",0)
