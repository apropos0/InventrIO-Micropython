import machine
import time

led = machine.Pin('LED', machine.Pin.OUT)

led.value(True)
time.sleep(1)
led.value(False)
time.sleep(1)
