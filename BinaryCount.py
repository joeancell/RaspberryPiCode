#import the GPIO and time package
import RPi.GPIO as GPIO
import time
import random

#use the Broadcom SOC channel
GPIO.setmode(GPIO.BCM)

leds = [17, 18, 27, 22, 23, 24, 25, 2, 3, 8];

for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, True)
for x in range(1, 32):
   randomNumber = x
   binaryString = bin(randomNumber)
   reverseString = binaryString[::-1]
   shortedString = reverseString[:-2]
   print "showing binary version of " + str(randomNumber)
   print binaryString
   print reverseString
   print reverseString.find('b')
   print reverseString[:-2]

   i = 0
   for x in shortedString:
      if x == '1':
         GPIO.output(leds[i], False)
      else:
         GPIO.output(leds[i], True)
      i = i + 1
   time.sleep(1)

#clean up GPIO
GPIO.cleanup()