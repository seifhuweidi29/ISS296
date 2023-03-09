from components import BikeLockSystem
import time

relay_pin = 18
lock_pin = 23
buzzer_pin = 24

bike_lock = BikeLockSystem(relay_pin, lock_pin, buzzer_pin)

# lock the bike
bike_lock.lock()

# wait for 5 seconds
time.sleep(5)

# unlock the bike
bike_lock.unlock()

# clean up the GPIO pins
bike_lock.cleanup()
