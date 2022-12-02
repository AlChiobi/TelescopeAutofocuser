import time
from time import sleep
import RPi.GPIO as GPIO

DIR = 38 #direction gpio pin
STEP = 40 # step gpio pin
CW = 1 #clockwise rotation
CCW = 0 #counterclockwise rotation
SPR = 200 #eps per revolution (360 / 1.8)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR,CW)

step_count = SPR
delay = .0208

for x in range(step_count):
	print('in first loop')
	GPIO.output(STEP,GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP,GPIO.LOW)
	sleep(delay)

sleep(.5)
GPIO.output(DIR,CCW)
for x in range(step_count):
	print('in second loop')
	GPIO.output(STEP,GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP,GPIO.LOW)
	sleep(delay)
print('FINISHED')
GPIO.cleanup()
