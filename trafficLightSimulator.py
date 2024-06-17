import machine
import utime

#Init leds
red_led = machine.Pin(16, machine.Pin.OUT)
yellow_led = machine.Pin(17, machine.Pin.OUT)
green_led = machine.Pin(18, machine.Pin.OUT)

# function to turn all the LEDs off:
def all_off():
    red_led.value(False)
    yellow_led.value(False)
    green_led.value(False)

# turn the led on and sleep for the mentioned time
def turn_led_on_and_sleep(led, sleep):
    led.value(True)
    utime.sleep(sleep)
    all_off()
    
while True:
    all_off()
    turn_led_on_and_sleep(red_led, 5)
    turn_led_on_and_sleep(yellow_led, 1)
    turn_led_on_and_sleep(green_led, 4)