import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

servo = GPIO.PWM(11,50)
servo.start(0)
time.sleep(2)

print("putar 90 derajat")
duty = 2
while duty<=7:
    servo.ChangeDutyCylce(duty)
    time.sleep(0.5)
    duty=duty+1

servo.ChangeDutyCycle(2)
time.sleep(1)
servo.ChangeDutyCycle(0)

servo.stop()

print("finish")
