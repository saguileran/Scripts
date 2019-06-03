import Adafruit_BBIO.GPIO as GPIO
import time

#Pin Assignment with Variables
#Primeros pines
#d="P9_11"
#c="P8_7"
#b="P9_12"
#a="P8_8"

d="P8_8"
c="P8_10"
b="P8_12"
a="P8_14"
GPIO.setup("P8_8",GPIO.OUT)
GPIO.setup("P8_10",GPIO.OUT)
GPIO.setup("P8_12",GPIO.OUT)
GPIO.setup("P8_14",GPIO.OUT)

dt=1*10**-3

#Define function for making coil on and off 
def coilOn(pin):
      #GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, GPIO.HIGH)
      return

def coilOff(pin):
      #GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)
      return

def alloff():
 for i in range(4):
  j=i*2+8
  GPIO.output("P8_%d" % j, 0)
 return

#Define Function for Step Sequences
#0101 =     a b c d
def seQ5():
       coilOn(d)
     #time.sleep(dt)
       coilOff(c)
       #time.sleep(dt)
       coilOn(b)
       #time.sleep(dt)
       coilOff(a)
       #time.sleep(dt)
       return

#1001
def seQ9():
       coilOn(d)
       #time.sleep(dt)
       coilOff(c)
       #time.sleep(dt)
       coilOff(b)
       #time.sleep(dt)
       coilOn(a)
       #time.sleep(dt)
       return

#1010
def seQ10():
       coilOff(d)
       #time.sleep(dt)
       coilOn(c)
       #time.sleep(dt)
       coilOff(b)
       #time.sleep(dt)
       coilOn(a)
       #time.sleep(dt)
       return

#0110
def seQ6():
       coilOff(d)
       #time.sleep(dt)
       coilOn(c)
       #time.sleep(dt)
       coilOn(b)
       #time.sleep(dt)
       coilOff(a)
       #time.sleep(dt)
       return

#Define Function for direction
#5-9-10-6 for anticlockwise direction
def antiClockW():
       seQ5()
       time.sleep(dt)
       seQ9()
       time.sleep(dt)
       seQ10()
       time.sleep(dt)
       seQ6()
       time.sleep(dt)
       return

#6-10-9-5 for clockwise direction
def clockW():
       seQ6()
       time.sleep(dt)
       seQ10()
       time.sleep(dt)
       seQ9()
       time.sleep(dt)
       seQ5()
       time.sleep(dt)
       return

def run(dt):
  coilOn(a)
  time.sleep(dt)
  coilOn(b)
  time.sleep(dt)
  coilOn(c)
  time.sleep(dt)
  coilOn(d)
  time.sleep(dt)



#define Main program
print("Python Programa for Stepper Motor")
print(" ")
alloff()
#clockW()
i=0
#while i<10:
       #print("Stepper motor rotating in anticlockwise direction")
       #for i in range (0,12):
               #antiClockW()
       #time.sleep(0.2)

       #print("Stepper motor rotating in clockwise direction")
       #for i in range (0,12):
               #clockW()
       #time.sleep(0.2)
       #i+=1
wait=0.007
nVueltas=3

#for i in range(512*nVueltas):
 #       for j in range(4):
  #              GPIO.output("P8_8",GPIO.HIGH if (8+j*2)==8 else GPIO.LOW)
   #             GPIO.output("P8_10",GPIO.HIGH if (8+j*2)==10 else GPIO.LOW)
    #            GPIO.output("P8_12",GPIO.HIGH if (8+j*2)==12 else GPIO.LOW)
     #           GPIO.output("P8_14",GPIO.HIGH if (8+j*2)==14 else GPIO.LOW)
	#	time.sleep(wait)
