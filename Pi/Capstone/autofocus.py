import cv2 #sudo apt-get install python-opencv
import numpy as py
import os
import time
import smbus


import motorControl

bus = smbus.SMBus(1)
mc = motorControl.MotorControl()

try:
	import picamera
	from picamera.array import PiRGBArray
except:
	sys.exit(0)

def SNR(a, axis=None, ddof=0):
    a = py.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return py.where(sd == 0, 0, m/sd)
    
def resetMotor():
    print("resetting motor")
    # reset motor function
    mc.stride(-400)
    time.sleep(3)

def scanImages():
    # reseting camera
    resetMotor()
    
    print("initiating stride")
    # assumes a total stride of 8:
    # -400, -300, -200, -100, 0, 100, 200, 300, 400 
    idx = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    images = []
    for i in range(9):
        # incrementing strides by 100
        mc.stride(100)
        time.sleep(0.3)
        # taking image arrays
        rawCapture = PiRGBArray(camera) 
        camera.capture(rawCapture,format="bgr", use_video_port=True)
        image = rawCapture.array
        rawCapture.truncate(0)
        images.append(image)
    
    # returning index and image array set
    return zip(idx, images)

def findBestFocus(images):
    print("Finding best image")
    result = [None, None]
    maxSNR = 0
    for idx, image in images:
        snr = SNR(image)
        print (image) 
        print (snr) 
        if snr > maxSNR:
            maxSNR = snr
            result = [idx, image]

    # returning image and its corresponding index
    return result

def setFinalFocus(idx):
    # reverse adjustment to optimal setting
    stride = (idx - 8)  * 100
    mc.stride(stride)
    time.sleep(3)

'''
def focusing(val):
    value = (val << 4) & 0x3ff0
    data1 = (value >> 8) & 0x3f
    data2 = value & 0xf0
    # time.sleep(0.5)
    print("focus value: {}".format(val))
    # bus.write_byte_data(0x0c,data1,data2)
    os.system("i2cset -y 0 0x0c %d %d" % (data1,data2))
	
def sobel(img):
	img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	img_sobel = cv2.Sobel(img_gray,cv2.CV_16U,1,1)
	return cv2.mean(img_sobel)[0]

def laplacian(img):
	img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	img_sobel = cv2.Laplacian(img_gray,cv2.CV_16U)
	return cv2.mean(img_sobel)[0]
	

def calculation(camera):
	rawCapture = PiRGBArray(camera) 
	camera.capture(rawCapture,format="bgr", use_video_port=True)
	image = rawCapture.array
	rawCapture.truncate(0)
	return laplacian(image)
'''
	
if __name__ == "__main__":
    #open camera
    camera = picamera.PiCamera()
    camera.iso = 800
    camera.shutter_speed = 6000000
    #camera.awb_gains=4
    #camera.exposure_mode='off'	
    #camera.awb_mode='fluorescent'
    #open camera preview
    camera.start_preview(fullscreen = False, window = (100,20,640,480))
    #set camera resolution to 640x480(Small resolution for faster speeds.)
    camera.resolution = (640, 480)
    time.sleep(0.1)
    
    # initalizing course tune adjustment

    # getting scanned image set
    # returns zip of position (relative to restart)
    images = scanImages()
    

    # find best focus
    idx, image = findBestFocus(images)
    
    
    # sets course point adjsutment
    # assumes furthest end is reached.
    setFinalFocus(idx)

    '''
    # fine tune image adjustmet
    print("Starting Fine Focusing...")
    
    max_index = 10
    max_value = 0.0
    last_value = 0.0
    dec_count = 0
    focal_distance = 10

    while True:
        #Adjust focus
        focusing(focal_distance)
        #Take image and calculate image clarity
        val = calculation(camera)
        #Find the maximum image clarity
        if val > max_value:
            max_index = focal_distance
            max_value = val
            
        #If the image clarity starts to decrease
        if val < last_value:
            dec_count += 1
        else:
            dec_count = 0
        #Image clarity is reduced by six consecutive frames
        if dec_count > 6:
            break
        last_value = val
        
        #Increase the focal distance
        focal_distance += 15
        if focal_distance > 1000:
            break

    #Adjust focus to the best
    focusing(max_index)
    '''
    time.sleep(1)
    #set camera resolution to 2592x1944
    camera.resolution = (1920,1080)
    #save image to file.
    camera.capture("TelescopeImage.png")
    # print("max index = %d,max value = %lf" % (max_index,max_value))
    #while True:
    #	time.sleep(1)
        
    camera.stop_preview()
    camera.close()
