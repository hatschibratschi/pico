from machine import Pin, PWM
import utime 

led = Pin(27) # GP27
pwm = PWM(led)

pwm.freq(1000)

# fade the led
duty = 0
direction = 1
for repeat in range(2000):
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    utime.sleep(0.01)
