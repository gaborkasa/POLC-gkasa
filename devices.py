import RPi.GPIO as GPIO


LED_PIN     = 21
BUTTON_PIN  = 20
BUZZER_PIN  = 16

class PiDevices(object):
    """Internet 'thing' that can control GPIO on a Raspberry Pi."""

    def __init__(self):
        """Initialize the 'thing'."""
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.setup(BUTTON_PIN, GPIO.IN)
        GPIO.setup(BUZZER_PIN, GPIO.OUT)

    def read_button(self):
        """Read the button state and return its current value.
        """
        return GPIO.input(BUTTON_PIN)

    def set_led(self, value):
        """Set the LED to the provided value (True = on, False = off).
        """
        GPIO.output(LED_PIN, value)

    def set_buzzer(self, value):
        """Set the buzzer to the provided value (True = on, False = off).
        """
        GPIO.output(BUZZER_PIN, value)
