from machine import Pin, PWM, ADC
from time import sleep_ms
from servo import Servo
import time

# sound_sensor functionality (sensor big sound):
adc = ADC (Pin (26)) #I don't need it but I set it
sound = Pin(27, Pin.IN, Pin.PULL_DOWN)

# servo
SERVO_PIN_NUMBER = 21
servo_pin = PWM(Pin(SERVO_PIN_NUMBER))
servo_motor = Servo(servo_pin,2500, 8600)

current_state = 0

def secret():
    global current_state, sound
    #digital sound
    q = 0
    for i in range(50000):
        q = q + sound.value()
    print(q)
    
    # snd_secret =  adc.read_u16() I don't need to read it
    
    if q > 500 and current_state == 0:
        print('Person speaking')
        current_state = 1
        
    if q < 50 and current_state == 1:
        print('No person')
        # SERVO: 0-256 = 45', 0-512 = 90', 0-1024 = 180'
        servo_motor.goto(0) 
        sleep_ms(1000)
        servo_motor.goto(256)
 
        current_state = 0

while(True):
    secret()