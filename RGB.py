import RPi.GPIO as GPIO
import threading
import time
import random

R = 17
G = 18
B = 27

PINS = [R, G, B]

def initialize():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)

def color(channel, frequency, speed, step):
   p = GPIO.PWM(channel, frequency)
   p.start(0)
   while True:
	for dutyCycle in range(0, 101, step):
	   p.ChangeDutyCycle(dutyCycle)
	   time.sleep(speed)
	for dutyCycle in range(100, -1, -step):
	   p.ChangeDutyCycle(dutyCycle)
	   time.sleep(speed)


def color_thread():
   threads = []
   threads.append(threading.Thread(target=color, args=(R, 300, 0.02, 5)))
   threads.append(threading.Thread(target=color, args=(G, 300, 0.035, 5)))
   threads.append(threading.Thread(target=color, args=(B, 300, 0.045, 5)))
   for t in threads:
	t.daemon = True
	t.start()
   for t in threads:
	t.join()

def main():
   try:
	initialize()
        color_thread()
   except KeyboardInterrupt:
	pass
   finally:
	GPIO.cleanup()


if __name__ == '__main__':
   main()