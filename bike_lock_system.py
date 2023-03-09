'''
import RPi.GPIO as GPIO
import time

class BikeLockSystem:
    def __init__(self, relay_pin, lock_pin, buzzer_pin):
        self.relay_pin = relay_pin
        self.lock_pin = lock_pin
        self.buzzer_pin = buzzer_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.relay_pin, GPIO.OUT)
        GPIO.setup(self.lock_pin, GPIO.OUT)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)

    def lock(self):
        GPIO.output(self.buzzer_pin, GPIO.HIGH)
        GPIO.output(self.lock_pin, GPIO.HIGH)
        GPIO.output(self.relay_pin, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(self.relay_pin, GPIO.LOW)
        GPIO.output(self.lock_pin, GPIO.LOW)
        GPIO.output(self.buzzer_pin, GPIO.LOW)

    def unlock(self):
        GPIO.output(self.buzzer_pin, GPIO.HIGH)
        GPIO.output(self.lock_pin, GPIO.HIGH)
        GPIO.output(self.relay_pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(self.relay_pin, GPIO.LOW)
        GPIO.output(self.lock_pin, GPIO.LOW)
        time.sleep(2)
        GPIO.output(self.buzzer_pin, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()
'''