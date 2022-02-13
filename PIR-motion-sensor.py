from machine import Pin, PWM, ADC
from time import sleep_ms
from servo import Servo
import time

# sound_sensor functionality:
# NO: adc = ADC (Pin (28))
adc = ADC (Pin (26))

# motion sensor
motion_sensor = Pin(06, Pin.IN, Pin.PULL_UP)

# servo
SERVO_PIN_NUMBER = 21
servo_pin = PWM(Pin(SERVO_PIN_NUMBER))
servo_motor = Servo(servo_pin,2500, 8600)

def sound():
    snd_secret =  adc.read_u16()
    _THRESHOLD = 13000
    
    if motion_sensor.value()==1:
        print('there is a person')
    
        if snd_secret > _THRESHOLD:
            print('Yes')
            print(snd_secret)
            # 0-512 = 90', 0-1024 = 180'
            servo_motor.goto(0) 
            sleep_ms(1200)
            
        else:
            servo_motor.goto(512)
            
            
                
            
    else:
        print('Nobody')
        print(snd_secret)
  

while(True):
    sound()
    