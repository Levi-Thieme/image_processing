import numpy as np
import math

def sum_frequencies(data):
    return data.sum()

def control_parameter(frequency_sum, system_constant, x0):
    return (frequency_sum / system_constant) * x0 % 1

def iterations(frequency_sum):
    return (frequency_sum % 3.1) + 2

def get_fractional(number):
    return math.modf(number)[0]

def fractional_to_binary(number, max_bits):
    binary = ""
    while(max_bits):
        number *= 2
        fractional_bit = int(number)
        if (fractional_bit == 1):
            number -= fractional_bit
            binary += '1'
        else:
            binary += '0'
        max_bits -= 1
    return binary
