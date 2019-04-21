import time
import sys
import RPi.GPIO as GPIO
import json

with open('config.json') as config_file:
    config = json.load(config_file)

short_delay = config['short_delay']
long_delay = config['long_delay']
extended_delay = config['extended_delay']
codes = config['codes']

NUM_ATTEMPTS = config['attempts'] 
TRANSMIT_PIN = config['transmit_pin']

def apply_state_to_one_outlet(outlet, state):
    transmit_code(codes[outlet][state])

def apply_state_to_all_outlets(state):
    for outlet in codes:
        transmit_code(codes[outlet][state])

def transmit_code(code):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in code:
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(short_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_delay)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(long_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(extended_delay)
    GPIO.output(TRANSMIT_PIN, 0)
    GPIO.cleanup()
