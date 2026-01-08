import serial
import time

# !!! IMPORTANT: Replace 'COM4' with your actual port name !!!
# !!! Ensure the baud rate matches the Arduino sketch (e.g., 9600) !!!

ser = serial.Serial('COM6',115200, timeout=1) 
time.sleep(2) # Give the Arduino time to reset after the port is opened

ser.write(b'2') # Send an encoded string to the Arduino

while True:
    if ser.in_waiting:
        # Read the line, decode it from bytes to string, and remove whitespace
        data = ser.readline().decode('utf-8').strip()
        print(f"Received from Arduino: {data}")

