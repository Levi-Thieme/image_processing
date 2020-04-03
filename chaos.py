import numpy as np

def logistic_map_2d(r, x, y):
    x2 = r * (3*y + 1) * x * (1 - x)
    y2 = r * (3*x2 + 1) * y * (1 - y)
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
    for i in range(0, length):
        x[i] = int(x[i] * length)
        y[i] = int(y[i] * length)
    return np.array([x.astype(int), y.astype(int)])

def henon_map(x, y, a, b):
    x1 = 1 - a * (x * x) + y
    y1 = b * y
    return np.array([x1, y1])

def sequence_to_int(sequence, max):
    sequence = np.round(sequence, decimals=0)
    integers = np.zeros((sequence.size,), dtype=int)
    for i in range(0, sequence.size-1):
        integers[i] = sequence[i] % (max + 1)
    return integers
