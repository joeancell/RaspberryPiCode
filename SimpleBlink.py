#import the GPIO and time package
import RPi.GPIO as GPIO
import time

#use the Broadcom SOC channel
GPIO.setmode(GPIO.BCM)

//setup GPIO17 as an output
GPIO.setup(17, GPIO.OUT)

# loop through 50 times, on/off for 1 second
for i in range(50):
    GPIO.output(17,True)
    time.sleep(1)
    GPIO.output(17,False)
    time.sleep(1)

//clean up GPIO
GPIO.cleanup()