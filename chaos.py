import numpy as np

def logistic_map_2d(r, x=.1, y=.1):
    x2 = r * (3*y + 1) * (x * (1 - x))
    y2 = r * (3*x + 1) * (y * (1 - y))
    return [x2, y2]

def log_map_sequences(r, x0, y0, length):
    x = np.zeros(length)
    y = np.zeros(length)
    xi = x0
    yi = y0
    for i in range(0, length):
        seq = logistic_map_2d(r, xi, yi)
        x[i] = seq[0]
        y[i] = seq[1]
        xi = x[i]
        yi = y[i]
    return np.array([x, y])

def sequence_to_int(sequence, max):
    sequence = np.round(sequence, decimals=0)
    print(sequence)
    integers = np.zeros((sequence.size,), dtype=int)
    for i in range(0, sequence.size-1):
        integers[i] = sequence[i] % (max + 1)
    return integers
