import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

servo = GPIO.PWM(11,50)
servo.start(0)
time.sleep(1)

servo.ChangeDutyCycle(7)
time.sleep(1)
servo.ChangeDutyCycle(0)
