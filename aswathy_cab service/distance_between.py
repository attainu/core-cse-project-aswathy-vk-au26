import math
def distance(x1, x2, y1, y2):
    x = x2 - x1
    y = y2 - y1
    return math.sqrt((x ** 2) + (y ** 2))
