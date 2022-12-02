import RPi.GPIO as GPIO
import time 

#assigns driver output to pins on the pi 
out1 = 13   #assigns output 1 to pin 13 
out2 = 11   #assigns output 2 to pin 11
out3 = 15   #assigns output 3 to pin 15
out4 = 12   #assigns output 4 to pin 12 

i=0
positive=0
negative=0
y=0


#Declares pin numbering system
GPIO.setmode(GPIO.BOARD)
#Assigns pin type 
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)

print ("Enter step count:")


try:
   while(1):   #infinite loop
       #initially sets all outputs to 0 
      GPIO.output(out1,GPIO.LOW)
      GPIO.output(out2,GPIO.LOW)
      GPIO.output(out3,GPIO.LOW)
      GPIO.output(out4,GPIO.LOW)
      x = input()
      x = int(x)
      if x>0 and x<=400:   #sets range of input values to be 0 < x <= 400
          for y in range(x,0,-1):   #starts at value x, and returns to 0 in increments of -1 
              if negative==1:
                  if i==7:
                      i=0
                  else:
                      i=i+1
                  y=y+2
                  negative=0
              positive=1
              #print((x+1)-y)
              #if the value of i = 0 step = 1 
              if i==0:
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.03)   #suspends execution for .03 seconds 
                  #time.sleep(1)
              #if the value of i = 1 step = 2 
              elif i==1:
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.03)
                  #time.sleep(1)
              #if the value of i = 2 step = 3 
              elif i==2:  
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.03)
                  #time.sleep(1)
              #if the value of i = 3 step = 4 
              elif i==3:    
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.03)
                  #time.sleep(1)
              #if the value of i = 4 step = 5 
              elif i==4:  
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.03)
                  #time.sleep(1)
              #if the value of i = 5 step = 6  
              elif i==5:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.03)
                  #time.sleep(1)
              #if the value of i = 6 step = 7 
              elif i==6:    
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.03)
                  #time.sleep(1)
              #if the value of i = 7 step = 8 
              elif i==7:    
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.03)
                  #time.sleep(1)
              if i==7:
                  i=0
                  continue
              i=i+1
      
      
      elif x<0 and x>=-400:   #sets range of input values to be -400 <= x < 0
          x=x*-1
          for y in range(x,0,-1):
              if positive==1:
                  if i==0:
                      i=7
                  else:
                      i=i-1
                  y=y+3
                  positive=0
              negative=1
              #print((x+1)-y) 
              if i==0:
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.03)
                  #time.sleep(1)
              elif i==1:
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.03)
                  #time.sleep(1)
              elif i==2:  
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.03)
                  #time.sleep(1)
              elif i==3:    
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.03)
                  #time.sleep(1)
              elif i==4:  
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.03)
                  #time.sleep(1)
              elif i==5:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.03)
                  #time.sleep(1)
              elif i==6:    
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.03)
                  #time.sleep(1)
              elif i==7:    
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.03)
                  #time.sleep(1)
              if i==0:
                  i=7
                  continue
              i=i-1 

              
except KeyboardInterrupt:
    GPIO.cleanup()