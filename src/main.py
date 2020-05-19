from Arudino.Test.BinaryClac import *
from Arudino.Test.arduino import *
import serial


def Input():
    _input = input("Please give a number between 0-31: ")
    num1 = int(_input)

    num_error = 'input was too high. Please give another input between 0-31 '
    '(31 in binary is 11111 where each number represents an Arduino LED).'
    operation_error = 'Invalid operation. Please try again.'

    if num1 > 31:
        print(num_error)

    _input = input("Please give a number between 0-31: ")
    num2 = int(_input)

    if num2 > 31:
        print(num_error)

    operation = input("Please give a operation ('+', '-', '*', '/'): ")

    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print(operation_error)

    return num1, operation, num2


port = 'COM3'
baud_rate = 9600

ard = Connect(port, baud_rate)
# Connect to port
list = Input()
WriteTo(ard, Calculate(list[0], list[1], list[2]))
# Write to serial

ReadFrom(ard)
# Read incoming data from Arduino
