import Adafruit_BBIO.GPIO as GPIO
import time

#Pin Assignment with Variables
w1="P9_11"
w2="P8_7"
w3="P9_12"
w4="P8_8"
dt=0.0001

#Define function for making coil on and off 
def coilOn(pin):
      GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, GPIO.HIGH)
      return

def coilOff(pin):
      GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)
      return

#Define Function for Step Sequences
#0101 =     w4 w3 w2 w1
def seQ5():
       coilOn(w1)
       time.sleep(dt)
       coilOff(w2)
       time.sleep(dt)
       coilOn(w3)
       time.sleep(dt)
       coilOff(w4)
       time.sleep(dt)
       return

#1001
def seQ9():
       coilOn(w1)
       time.sleep(dt)
       coilOff(w2)
       time.sleep(dt)
       coilOff(w3)
       time.sleep(dt)
       coilOn(w4)
       time.sleep(dt)
       return

#1010
def seQ10():
       coilOff(w1)
       time.sleep(dt)
       coilOn(w2)
       time.sleep(dt)
       coilOff(w3)
       time.sleep(dt)
       coilOn(w4)
       time.sleep(dt)
       return

#0110
def seQ6():
       coilOff(w1)
       time.sleep(dt)
       coilOn(w2)
       time.sleep(dt)
       coilOn(w3)
       time.sleep(dt)
       coilOff(w4)
       time.sleep(dt)
       return

#Define Function for direction
#5-9-10-6 for anticlockwise direction
def antiClockW():
       seQ5()
       time.sleep(0.01)
       seQ9()
       time.sleep(0.01)
       seQ10()
       time.sleep(0.01)
       seQ6()
       time.sleep(0.01)
       return


#6-10-9-5 for clockwise direction
def clockW():
       seQ6()
       time.sleep(0.01)
       seQ10()
       time.sleep(0.01)
       seQ9()
       time.sleep(0.01)
       seQ5()
       time.sleep(0.01)
       return

#define Main program
print("Python Programa for Stepper Motor")
print(" ")
i=0
while i<10:
       print("Stepper motor rotating in anticlockwise direction")
       for i in range (0,12):
               antiClockW()
       time.sleep(0.2)

       print("Stepper motor rotating in clockwise direction")
       for i in range (0,12):
               clockW()
       time.sleep(0.2)
       i+=1
