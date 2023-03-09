from flask import Flask, render_template, request
from Mock import MockBikeLockSystem
import time

app = Flask(__name__)
bike_lock = MockBikeLockSystem(18, 23, 24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lock', methods=['POST'])
def lock():
    bike_lock.lock()
    return 'Bike locked!'

@app.route('/unlock', methods=['POST'])
def unlock():
    bike_lock.unlock()
    return 'Bike unlocked!'

if __name__ == '__main__':
    app.run(debug=True)
