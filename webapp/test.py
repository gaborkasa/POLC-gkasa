import time

import devices


# Create the pi thing.
pi_devices = devices.PiDevices()
print ('start')
# Print the current switch state.
while True:
    switch = pi_devices.read_button()
    #print('Switch status: {0}'.format(switch))
    if switch == 1:
        pi_devices.set_led(True)
        pi_devices.set_buzzer(True)
    elif switch == 0:
        pi_devices.set_led(False)
        pi_devices.set_buzzer(False)


# Now loop forever blinking the LED.
"""print('Looping with LED blinking (Ctrl-C to quit)...')
while True:
    pi_devices.set_led(True)
    time.sleep(0.5)
    pi_devices.set_led(False)
    time.sleep(0.5)
"""
