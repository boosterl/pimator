import json


class Config:
    def __init__(self):
        with open('config.json') as config_file:
            config = json.load(config_file)

        self._short_delay = config['short_delay']
        self._long_delay = config['long_delay']
        self._extended_delay = config['extended_delay']
        self._codes = config['codes']
        self._num_attempts = config['attempts']
        self._transmit_pin = config['transmit_pin']

    @property
    def short_delay(self):
        return self._short_delay

    @property
    def long_delay(self):
        return self._long_delay

    @property
    def extended_delay(self):
        return self._extended_delay

    @property
    def codes(self):
        return self._codes

    @property
    def attempts(self):
        return self._num_attempts

    @property
    def transmit_pin(self):
        return self._transmit_pin
