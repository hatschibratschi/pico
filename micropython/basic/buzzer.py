from machine import Pin, PWM
from utime import sleep

led_onboard = machine.Pin(25, machine.Pin.OUT)
buzzer = PWM(Pin(15))

led_onboard.value(0)

s = 0.5

while True:
    try:
        led_onboard.toggle()
        buzzer.freq(600)
        buzzer.duty_u16(200)
        sleep(s)
        led_onboard.toggle()
        buzzer.duty_u16(0)
        sleep(s)
    except KeyboardInterrupt:
        print("exit")
        led_onboard.value(0)
        buzzer.duty_u16(0)
        raise Exception
