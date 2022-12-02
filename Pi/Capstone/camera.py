from picamera import PiCamera
import time

camera = PiCamera()
camera.shutter_speed = 6000000
camera.iso = 300
camera.start_preview()
#for i in range (10):
    #sleep(2)
#camera.start_recording('star10_vid.h264')
time.sleep(15)
#camera.exposure_mode = 'off'
camera.capture('/home/pi/Pictures/PRACTICE.png')
#sleep(60)
#camera.stop_recording()
camera.stop_preview()
 
camera.close()

