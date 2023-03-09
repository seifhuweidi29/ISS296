class MockBikeLockSystem:
    def __init__(self, relay_pin, lock_pin, buzzer_pin):
        pass

    def lock(self):
        print('Mock bike locked!')

    def unlock(self):
        print('Mock bike unlocked!')

    def cleanup(self):
        pass
