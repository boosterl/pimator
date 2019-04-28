import time
import RPi.GPIO as GPIO


class Transmitter:
    def __init__(self, config):
        self._config = config
        self._short_delay = self._config.short_delay
        self._long_delay = self._config.long_delay
        self._extended_delay = self._config.extended_delay
        self._codes = self._config.codes
        self._attempts = self._config.attempts
        self._transmit_pin = self._config.transmit_pin

    def apply_state_to_one_outlet(self, outlet, state):
        self.transmit_code(self._codes[outlet][state])

    def apply_state_to_all_outlets(self, state):
        for outlet in self._codes:
            self.transmit_code(self._codes[outlet][state])

    def transmit_code(self, code):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._transmit_pin, GPIO.OUT)
        for t in range(self._attempts):
            for i in code:
                if i == '1':
                    GPIO.output(self._transmit_pin, 1)
                    time.sleep(self._short_delay)
                    GPIO.output(self._transmit_pin, 0)
                    time.sleep(self._long_delay)
                elif i == '0':
                    GPIO.output(self._transmit_pin, 1)
                    time.sleep(self._long_delay)
                    GPIO.output(self._transmit_pin, 0)
                    time.sleep(self._short_delay)
                else:
                    continue
            GPIO.output(self._transmit_pin, 0)
            time.sleep(self._extended_delay)
        GPIO.output(self._transmit_pin, 0)
        GPIO.cleanup()
