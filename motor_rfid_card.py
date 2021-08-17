import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(13,GPIO.OUT)

servo = GPIO.PWM(13,50)
servo.start(0)
time.sleep(2)

try:
    id,text = reader.read()
    print(id)
    print(text)
    servo.start(0)
    time.sleep(0.5)
    servo.ChangeDutyCycle(7)
    time.sleep(0.5)
    
finally:
    servo.ChangeDutyCycle(2)
    time.sleep(1)
    servo.ChangeDutyCycle(0)
    servo.stop()
    GPIO.cleanup()
