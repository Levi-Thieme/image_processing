import numpy as np
import math

def sum_frequencies(data):
    return data.sum()

#T
def control_parameter(frequency_sum, system_constant, x0):
    return (frequency_sum / system_constant) * x0 % 1

#R
def iterations(frequency_sum):
    return (frequency_sum % 3.1) + 2

def initial_state(T, x0, i):
    return (T + x0 * i) % 1

def initial_state_r(T, r, i):
    return ((T * i * r) % 0.09) + 1.11

def get_fractional(number):
    return math.modf(number)[0]

def fractional_to_binary(number, max_bits):
    binary = np.zeros([max_bits], dtype=np.uint8)
    i = 0
    while(i < max_bits):
        number *= 2
        fractional_bit = int(number)
        if (fractional_bit == 1):
            number -= fractional_bit
            binary[i] = 1
        else:
            binary[i] = 0
        i += 1
    return binary

def key_from_partitions(x0, y0, r, T, R):
    key = np.empty([256], dtype=np.uint8)
    key[0:52] = x0
    key[52:104] = y0
    key[104:156] = r
    key[156:208] = T
    key[208:256] = R
    return key

def sum_and_divide(key, dividend):
    x = 0
    for i, k in enumerate(key, start=0):
        x += k * 2^(i-1)
    return x / dividend

def generate_key(x0, y0, r, T, R):
    iterations = int(round(R))
    dividend = 2^52
    x0 = key_partition(fractional_to_binary(get_fractional(x0), 52), dividend)
    y0 = key_partition(fractional_to_binary(get_fractional(y0), 52), dividend)
    r = key_partition(fractional_to_binary(get_fractional(r), 52), dividend)
    T = key_partition(fractional_to_binary(get_fractional(T), 52), dividend)
    dividend = 2^48
    R = key_partition(fractional_to_binary(get_fractional(R), 48), dividend)
    for i in range(1, iterations):
        x0[i] = initial_state_x(T, x0, i)
        y0[i] = initial_state_y(T, y0, i)
        r[i] = initial_state_y(T, r, i)
    return key_from_partitions(x0, y0, r, T, R)

def initial_states(T, x0, R):
    states = np.zeros(R)
    for i in range(1, R+1):
        states[i-1] = initial_state(T, x0, i)
    return states

def initial_states_r(T, r, R):
    states = np.zeros(R)
    for i in range(1, R+1):
        states[i-1] = initial_state_r(T, r, i)
    return states

def create_key(frequencies, x0=0.1, y0=0.2, r=1.12, system_constant=21):
    sum = sum_frequencies(frequencies)
    T = control_parameter(sum, system_constant, x0)
    R = iterations(sum)
    return generate_key(x0, y0, r, T, R)
