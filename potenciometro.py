import Adafruit_BBIO.ADC as ADC
ADC.setup()
from time import sleep
analogPin="P9_39"
while(1):
        potVal=ADC.read(analogPin)
        potVolt=potVal*1.8
        print "The Potentiometer Voltage is: "+str(potVolt)+" V"
        sleep(.5)
