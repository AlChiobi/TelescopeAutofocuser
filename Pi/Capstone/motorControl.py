import RPi.GPIO as GPIO   #Allows you to refer to the RPi.GPIO module as the shorter "GPIO" 
import time   #Importing a Python time module that provides various time-related functions
GPIO.setwarnings(False)
class MotorControl:
    
    
    def __init__(self):
        print("Initialized motor control")
    
    
    def stride(self, input):

        #assigns driver output to pins on the pi 
        out1 = 13   #assigns output 1 to pin 13 
        out2 = 11   #assigns output 2 to pin 11
        out3 = 15   #assigns output 3 to pin 15
        out4 = 12   #assigns output 4 to pin 12 

        i=0
        positive=0
        negative=0
        y=0
        delay=.005


        #Declares pin numbering system
        GPIO.setmode(GPIO.BOARD)
        #Assigns pin type 
        GPIO.setup(out1,GPIO.OUT)
        GPIO.setup(out2,GPIO.OUT)
        GPIO.setup(out3,GPIO.OUT)
        GPIO.setup(out4,GPIO.OUT)

        # print ("Enter step count between 0-800, where 800 = 360 degrees")
        

        try:
            #while(1):   #infinite loop
                #initially sets all outputs to 0 
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
    
                x = int(input)
                
                if x>0 and x<=2055:   #sets range of input values to be 0 < x <= 800
                    for y in range(x,0,-1):   #starts at value x, and returns to 0 in increments of -1 
                        if negative==1:
                            if i==3:
                                i=0
                            else:
                                i=i+1
                            y=y+2
                            negative=0
                        positive=1
                        
                        # This portion of the code is responsible for turning on the 4 outputs that energize the phases of the motor
                        #if the value of i = 0 step = 1 
                        if i==0:
                            GPIO.output(out1,GPIO.HIGH)
                            GPIO.output(out2,GPIO.LOW)
                            GPIO.output(out3,GPIO.LOW)
                            GPIO.output(out4,GPIO.LOW)
                            time.sleep(delay)   #suspends execution for .03 seconds 
                        #if the value of i = 1 step = 2 
                        elif i==1:
                            GPIO.output(out1,GPIO.LOW)
                            GPIO.output(out2,GPIO.HIGH)
                            GPIO.output(out3,GPIO.LOW)
                            GPIO.output(out4,GPIO.LOW)
                            time.sleep(delay)
                        #if the value of i = 2 step = 3 
                        elif i==2:  
                            GPIO.output(out1,GPIO.LOW)
                            GPIO.output(out2,GPIO.LOW)
                            GPIO.output(out3,GPIO.HIGH)
                            GPIO.output(out4,GPIO.LOW)
                            time.sleep(delay)
                        #if the value of i = 3 step = 4 
                        elif i==3:    
                            GPIO.output(out1,GPIO.LOW)
                            GPIO.output(out2,GPIO.LOW)
                            GPIO.output(out3,GPIO.LOW)
                            GPIO.output(out4,GPIO.HIGH)
                            time.sleep(delay)
                        #if the value of i = 4 step = 5 
                        if i==3:
                            i=0
                            continue
                        i=i+1
                
                #This portion of the code accounts for negative values   
                elif x<0 and x>=-2055:   #sets range of input values to be -800 <= x < 0
                    x=x*-1
                    for y in range(x,0,-1):
                        if positive==1:
                            if i==0:
                                i=3
                            else:
                                i=i-1
                            y=y+3
                            positive=0
                        negative=1
                        #print((x+1)-y)
                        #This portion of the code is responsible for turning on the 4 outputs that energize the phases of the motor
                        if i==0:
                            GPIO.output(out1,GPIO.HIGH)
                            GPIO.output(out2,GPIO.LOW)
                            GPIO.output(out3,GPIO.LOW)
                            GPIO.output(out4,GPIO.LOW)
                            time.sleep(delay)
                        elif i==1:
                            GPIO.output(out1,GPIO.LOW)
                            GPIO.output(out2,GPIO.HIGH)
                            GPIO.output(out3,GPIO.LOW)
                            GPIO.output(out4,GPIO.LOW)
                            time.sleep(delay)
                        elif i==2:  
                            GPIO.output(out1,GPIO.LOW)
                            GPIO.output(out2,GPIO.LOW)
                            GPIO.output(out3,GPIO.HIGH)
                            GPIO.output(out4,GPIO.LOW)
                            time.sleep(delay)
                        elif i==3:    
                            GPIO.output(out1,GPIO.LOW)
                            GPIO.output(out2,GPIO.LOW)
                            GPIO.output(out3,GPIO.LOW)
                            GPIO.output(out4,GPIO.HIGH)
                            time.sleep(delay)
                        if i==0:
                            i=3
                            continue
                        i=i-1 

                    
        except KeyboardInterrupt:
            GPIO.cleanup()
