import numpy as np
import random as rand


def Calculate(num1, operation, num2):

    switcher = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num1
    }

    result = switcher.get(operation, "Invalid operation")
    print(np.binary_repr(result))
    return np.binary_repr(result)


def RandomBinaryNum():
    # 31 in binary is 11111 which has 5 digits
    # Arduino currently has 5 LEDs connected to it
    return np.binary_repr(rand.randint(0, 31))


