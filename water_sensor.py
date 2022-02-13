import machine 
import time
from machine import ADC 
from machine import Pin

adc = ADC(Pin(28))

while(True):
    waterpres =  adc.read_u16()
    _THRESHOLD = 13000
    print(waterpres)
    if waterpres < _THRESHOLD:
        print('Water detected!')
    else:
        print('No water')
    time.sleep(1)