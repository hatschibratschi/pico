# sonic:
# wire vbux to vcc
# trigger gp13
# gp14

from machine import Pin, PWM
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

led_onboard = machine.Pin(25, machine.Pin.OUT)
buzzer = PWM(Pin(15))
buzzer.duty_u16(0)

def getMappedValue(dist, int1low, int1up, int2low, int2up):
    int1 = int1up - int1low
    int2 = int2up - int2low
    part1 = dist / int1
    freq = int(part1 * int2 + int2low)
    #print("freq ", freq)
    return(freq)

def ultra():
    trigger.low()
    utime.sleep_us(2) # Delay for given number of microseconds
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    #print("distance ", int(distance),"cm")
    return(distance)

while True:
    sleep = 0.2
    d = int(ultra())
    utime.sleep(sleep)
    print(d)
    t = 30 # threshold
    if d <= t:
        buzzer.freq(getMappedValue(d, 0, t, 900, 200))
        buzzer.duty_u16(getMappedValue(d, 0, t, 100, 900))
    if d > t:
        buzzer.duty_u16(0)
