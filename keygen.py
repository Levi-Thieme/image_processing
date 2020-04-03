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

def fto_bin(number, bits):
    return fractional_to_binary(get_fractional(number), bits);

def key_from_partitions(x0, y0, r, T, R):
    key = np.empty([256], dtype=np.uint8)
    key[0:52] = fto_bin(x0, 52)
    key[52:104] = fto_bin(y0, 52)
    key[104:156] = fto_bin(r, 52)
    key[156:208] = fto_bin(T, 52)
    key[208:256] = fto_bin(x0, 48)
    return key

def sum_and_divide(key, dividend):
    x = 0
    for i, k in enumerate(key, start=0):
        x += k * 2^(i-1)
    return x / dividend

def generate_key(x0, y0, r, T, iterations):
    x0 = get_fractional(x0)
    y0 = get_fractional(y0)
    r = get_fractional(r)
    T = get_fractional(T)
    return key_from_partitions(x0, y0, r, T, iterations)

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

def create_key_and_init_states(frequencies, x0=0.1, y0=0.2, r=1.12, system_constant=21):
    sum = sum_frequencies(frequencies)
    T = control_parameter(sum, system_constant, x0)
    R = int(round(iterations(sum)))
    x_init_states = initial_states(T, x0, R)
    y_init_states = initial_states(T, y0, R)
    r_init_states = initial_states_r(T, r, R)
    return [x_init_states, y_init_states, r_init_states, generate_key(x0, y0, r, T, R)]
