import RPi.GPIO as GPIO 
import time 
import requests

GPIO.setmode(GPIO.BCM)

TRIG=23
ECHO=24
ledPin=26

url ="https://api.thingspeak.com/update"
api_key = "OPVW4075974IKI71" 

print("Distance Measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(TRIG, False) 
GPIO.output(ledPin, GPIO.LOW)
ledStatus = False

print("Preparing sensor")
time.sleep(2)

while 1:
        #send wave
        GPIO.output(TRIG, True)
        time.sleep(0.00001) #10 microsecond delay
        GPIO.output(TRIG, False)

        #read wave
        while GPIO.input(ECHO)==0:
                pulse_start = time.time()

        while GPIO.input(ECHO)==1:
                pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = 34300 * pulse_duration/2

        distance = round(distance,2)

        print "Distance: ",distance, "cm"
        if distance < 20:
                ledStatus = 1
                GPIO.output(ledPin, GPIO.HIGH)
                print("Object too near")
        else:
                ledStatus = 0
                GPIO.output(ledPin, GPIO.LOW)
                print("Object not near")

        payload = {'api_key':api_key, 'field1': distance, 'field2': ledStatus}
        requests.get(url, params=payload)
        GPIO.output(TRIG, False)

        time.sleep(2)
