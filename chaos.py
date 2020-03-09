def logistic_map_2d(r, x=0, y=1):
    x2 = r * (3*y + 1) * (x * (1 - x))
    y2 = r * (3*x + 1) * (y * (1 - y))
    return [x2, y2]
