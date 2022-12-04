import machine, utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
  try:
      led_onboard.toggle()
      utime.sleep(0.1)
  except KeyboardInterrupt:
      led_onboard.value(0)
      print("exit")
      raise Exception
