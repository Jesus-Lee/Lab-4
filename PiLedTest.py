from hal import hal_led as led
from hal import hal_input_switch as switch
import time

def main():
    switch.init()
    a=switch.read_slide_switch()
    if a==1:
        blink_led()
        print("on")
    else:
        print("not on")



def blink_led():
    led.init()

    led.set_output(0, 1)
    time.sleep(0.5)

    led.set_output(0, 0)
    time.sleep(0.5)

    led.set_output(0, 1)
    time.sleep(0.5)

    led.set_output(0, 0)
    time.sleep(0.5)

if _name_ == "_main_":
    main()