#import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time, math
from decimal import *

ADC.setup()
analogPin="P9_41"
suma0,suma=0,0
N=10
for i in range(N):
#   GPIO.output("P9_25",1)
   thermistor=ADC.read(analogPin)
   print(thermistor)
#   print(round(soundVolt,3))
   #time.sleep(0.5)
   #GPIO.output("P9_25",0)
   suma+=thermistor
   #suma0+=decibel
   time.sleep(0.1)
print("Promedio")
print(str(suma/N))

