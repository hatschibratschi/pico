# light up led for 5 sec after motion

from machine import ADC, Pin, PWM
from time import sleep, time

# vars
reading_interval_photoResistor = 0.1
wait_time_to_sleep = 5 # sec
motion = False

# GPIOs
photoPIN = 26    # GP28
ledPIN = Pin(27) # GP27
pirPIN = 28

# gear
pwm = PWM(ledPIN)
pwm.freq(1000)
led_onboard = machine.Pin(25, machine.Pin.OUT)

pir = Pin(pirPIN, Pin.IN)

# functions #######################
def handle_interrupt(pin):
    global motion
    motion = True
    global interrupt_pin
    interrupt_pin = pin 

def readLight(photoGP, pt = True):
    photoRes = ADC(Pin(photoGP))
    light = photoRes.read_u16()
    if not pt:
        return light
    light = round(light/65535*100,2)
    return light


# program ######################

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
    try:
        if motion:
            print('Motion detected! Interrupt caused by:', interrupt_pin)
            led_onboard.value(1) # turn LED on
            # do somethins for x secs
            t_end = time() + 60 * 10 # stay on for 10 min
            while time() < t_end:
                l = readLight(photoPIN, False)
                v = 0
                # light goes below 4000
                if (l < 4000):
                    v = 65535
                if (l < 4000 / 2):
                    v = int(65535 / 3) * 2
                if (l < 4000 / 4):
                    v = int(65535 / 2)
                #print('light: ' + str(l) + ' ' + str(v))
                pwm.duty_u16(v)
                sleep(0.1)
            print('Motion stopped!')
            led_onboard.value(0) # turn LED off
            pwm.duty_u16(0) # turn LIGHT off
            motion = False
    except KeyboardInterrupt:
        led_onboard.value(0)
        print("exit")
        raise Exception

