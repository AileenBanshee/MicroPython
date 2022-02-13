from machine import Pin
from time import sleep_ms
import time

touch_sensor = Pin(17, Pin.IN, Pin.PULL_UP)

while True :
	time.sleep_ms(500)
	if touch_sensor.value() == 1:
		print('ON')
	else: # Autrement
		print('OFF')