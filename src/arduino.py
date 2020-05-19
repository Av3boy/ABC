import serial
import time


def Connect(port, baud_rate):
    ard = serial.Serial(port, baud_rate, timeout=5)
    print("Connected on port: " + port + ", with baud rate of 9600.")
    time.sleep(2)
    return ard


def WriteTo(ard, output):
    binary = str(output)
    ard.write(binary.encode())
    time.sleep(1)


def ReadFrom(ard):
    msg = ard.read(ard.inWaiting())
    # read all characters in buffer
    print("Message from arduino: ")
    print(msg.decode())
