from bike_lock_system import BikeLockSystem
import time

def main():
    relay_pin = 8
    lock_pin = 10
    buzzer_pin = 12

    bike_lock = BikeLockSystem(relay_pin, lock_pin, buzzer_pin)

    # lock the bike
    bike_lock.lock()

    # wait for 5 seconds
    time.sleep(5)

    # unlock the bike
    bike_lock.unlock()

    # clean up the GPIO pins
    bike_lock.cleanup()

if __name__ == "__main__":
    main()
