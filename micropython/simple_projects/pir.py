import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_onboard = machine.Pin(25, machine.Pin.OUT)

def pir_handler(pin):
    utime.sleep_ms(100)
    alarmNo = 1
    if pin.value():
        print("ALARM! Motion detected! ")
        led_onboard.toggle()

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

