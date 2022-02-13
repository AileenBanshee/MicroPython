from machine import Pin, ADC
from time import sleep_ms
import time

# sound_sensor functionality (sensor big sound):
adc = ADC (Pin (26))
sound = Pin(27, Pin.IN, Pin.PULL_DOWN)

while(True):
    q = 0
    for i in range(10000):
        q = q + sound.value()
        
    print(q)
    #print(snd_secret)

    #time.sleep(1)