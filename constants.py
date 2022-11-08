"""This is where all the constants are stored"""

"""
Define program constants
"""
U_TRIG = 23         #connected to ultrasonic trig
U_ECHO = 24         #connected to ultrasonic echo
LED_PIN = 26         #connected to LED
BUZZER_PIN = 16    #connected to buzzer 

URL = "https://api.thingspeak.com/update"
API_KEY =  "HLIZQ7WOMYUXJIHG" 

led_status = 0 
buzzer_status = 0

low_output_channels = (U_TRIG, LED_PIN, BUZZER_PIN)
input_channels = (U_TRIG, U_ECHO)
output_channels = (LED_PIN, BUZZER_PIN, U_TRIG)
