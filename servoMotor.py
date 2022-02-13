from machine import Pin, PWM
from time import sleep_ms
from servo import Servo
from Button import Button

SERVO_PIN_NUMBER = 21
servo_pin = PWM(Pin(SERVO_PIN_NUMBER))
servo_motor = Servo(servo_pin)

def button_action(pin, event):
    print(f'Button connected to Pin {pin} has been {event}')
    
    if event == Button.PRESSED:
        servo_motor.goto(0)
        sleep_ms(500)
    if event == Button.RELEASED:
        servo_motor.goto(500)
        sleep_ms(0)

my_button = Button(18, internal_pulldown = True, callback = button_action)

while(True):
    my_button.update()










