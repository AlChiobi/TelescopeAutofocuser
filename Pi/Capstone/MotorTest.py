import motorControl
import math
from picamera import PiCamera
import time


mc = motorControl.MotorControl()

camera = PiCamera()
camera.start_preview()
totalStride = 1755
strideLength = -200
camera.start_recording('final_video8.h264')

for i in range(math.floor(abs(totalStride/strideLength))):
	mc.stride(strideLength)
	time.sleep(1)
camera.stop_recording()
camera.stop_preview()
 
camera.close()
