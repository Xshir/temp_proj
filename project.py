"""
	Author: Prakash Divakaran
	Code for IoT Fundamentals Project Scenario, turns on LED and buzz the buzzer
	
	Instructions:
	 -There are 15 blanks in this code. Fill them up with the appropriate value/code and run this code to get the 
	- The blanks are at lines 18, 19, 20, 21, 23, 35, 38, 45, 47, 66, 68, 70, 71, 74, 78
"""

#import RPi.GPIO as GPIO
from RPi import GPIO
import time
import requests
from functions import setup_rpi, set_default_values, estimate_distance




if __name__ == '__main__':
        setup_rpi()
        set_default_values()
        print("Prepare sensor")
        time.sleep(1)
        estimate_distance() #this runs forever, unless crash or CTRL + C
