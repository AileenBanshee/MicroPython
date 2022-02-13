import machine, neopixel
import time

# PIXEL_PIN   = machine.Pin(21, machine.Pin.OUT)
PIXEL_NUMBER = 24
rgb = neopixel.NeoPixel(machine.Pin(21), PIXEL_NUMBER)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gradient = [red, green, blue, black, white]

index = 0

while (True):
    color = gradient[index]
    rgb.fill(color)
    rgb.write()
    
    index += 1
    if index > len(gradient)-1:
        index = 0
        
    time.sleep(0.5)