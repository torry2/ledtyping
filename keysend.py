import serial
import time

from pynput import keyboard


arduino = serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_558383233353512161A1-if00', 9600, timeout=1, parity=serial.PARITY_ODD)

print('Running...')
print('(Ctr+C to Exit)')

def on_press(key):
    try:
        arduino.write('o'.encode())
    except AttributeError:
        arduino.write('o'.encode())

def on_released(key):
    arduino.write('e'.encode())

with keyboard.Listener(
        on_press=on_press,
        on_released=on_released) as listener:
    listener.join()
