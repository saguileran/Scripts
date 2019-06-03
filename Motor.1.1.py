import Adafruit_BBIO.GPIO as GPIO
import time

d="P8_8"
c="P8_10"
b="P8_12"
a="P8_14"

GPIO.setup("P8_8",GPIO.OUT)
GPIO.setup("P8_10",GPIO.OUT)
GPIO.setup("P8_12",GPIO.OUT)
GPIO.setup("P8_14",GPIO.OUT)

dt=1*10**-3
vueltas=5 #numero de vueltas
pasos=1
hold=2

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
#0001 =     a b c d
def seQ1():
       coilOff(d)
       coilOff(c)
       coilOff(b)
       coilOn(a)
       return
#0010
def seQ2():
       coilOff(d)
       coilOff(c)
       coilOn(b)
       coilOff(a)
       return

#0100
def seQ3():
       coilOff(a)
       coilOff(b)
       coilOn(c)
       coilOff(d)
       return

#1000
def seQ4():
       coilOn(d)
       coilOff(c)
       coilOff(b)
       coilOff(a)
       return

#Define Function for direction
#1-2-3- for anticlockwise direction
def antiClockW():
       seQ1()
       time.sleep(dt)
       seQ2()
       time.sleep(dt)
       seQ3()
       time.sleep(dt)
       seQ4()
       time.sleep(dt)
       return

#6-10-9-5 for clockwise direction
def clockW():
       seQ4()
       time.sleep(dt)
       seQ3()
       time.sleep(dt)
       seQ2()
       time.sleep(dt)
       seQ1()
       time.sleep(dt)
       return

#define Main program
print("Python Programa for Stepper Motor")
print(" ")
#alloff()
for p in range((516)*vueltas):
  antiClockW()
  if p%(516/pasos)==0: time.sleep(hold)

#clockW()
#i=0
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
#wait=0.007
#nVueltas=3

#for i in range(512*nVueltas):
 #       for j in range(4):
  #              GPIO.output("P8_8",GPIO.HIGH if (8+j*2)==8 else GPIO.LOW)
   #             GPIO.output("P8_10",GPIO.HIGH if (8+j*2)==10 else GPIO.LOW)
    #            GPIO.output("P8_12",GPIO.HIGH if (8+j*2)==12 else GPIO.LOW)
     #           GPIO.output("P8_14",GPIO.HIGH if (8+j*2)==14 else GPIO.LOW)
	#	time.sleep(wait)
