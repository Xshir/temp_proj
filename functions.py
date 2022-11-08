"""This is where all the functions are stored"""

from RPi import GPIO
from constants import (
                       U_TRIG, 
                       U_ECHO, 
                       LED_PIN, 
                       BUZZER_PIN, 
                       API_KEY, 
                       URL,
                       )
from constants import (
                      low_output_channels,
                      output_channels,
                      input_channels
                      )
import requests
import time

"""
Helper function to setup pins  
"""


def setup_rpi():
    print("Setting up Pins")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_channels, GPIO.IN)
    GPIO.setup(output_channels, GPIO.OUT)


"""
Helper functions to set default values
"""


def set_default_values():
    print("Initializing Default Values")
    GPIO.output(low_output_channels, False) 



"""
Helper function to send data to thingspeak
To edit this in Task 
"""

def send_data_to_thingspeak(calculated_distance):

    # JSON payload, send data to ThingSpeak
    payload = {
        "api_key": API_KEY,
        "field1": calculated_distance,
        "field2": "",
        "field3": "",
    }
    requests.get(URL, params=payload)


"""
Helper function to check if a object is near
"""


def check_for_object(calculated_distance):
    global led_status
    global buzzer_status
    if calculated_distance < 15:
        led_status = 1
        buzzer_status = 1
        print("Object is too close")
        GPIO.output(LED_PIN, led_status)
        GPIO.output(BUZZER_PIN, False)

    else:
        led_status = 0
        buzzer_status = 0
        print("No object detected")
        GPIO.output(LED_PIN, False)
        GPIO.output(BUZZER_PIN, True)


"""
Helper function to send data to thingspeak
"""


def estimate_distance():
    while 1:
        # send wave
        GPIO.output(U_TRIG, True)
        time.sleep(0.00001)  # 10 microsecond delay
        GPIO.output(U_TRIG, False)

        # read wave
        while GPIO.input(U_ECHO) == 0:
            start_of_wave = time.time()

        while GPIO.input(U_ECHO) == 1:
            end_of_wave = time.time()

        pulse_duration = end_of_wave - start_of_wave

        calculated_distance = 34300 * pulse_duration / 2

        calculated_distance = round(calculated_distance, 2)

        GPIO.output(U_TRIG, False)

        print("Distance: ", calculated_distance, "cm")

        check_for_object(calculated_distance)

        send_data_to_thingspeak(calculated_distance)

        time.sleep(1)
