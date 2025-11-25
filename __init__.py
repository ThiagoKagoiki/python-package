import math

def delta(a: float, b: float, c: float):
    return b ** 2 - 4 * a * c

def raizSoma(a: float, b: float, c: float):
    deltaResult = delta(a, b, c)
    return (-b + math.sqrt(deltaResult)) / (2 * a)

def raizSubtracao(a: float, b: float, c: float):
    deltaResult = delta(a, b, c)
    return (-b - math.sqrt(deltaResult)) / (2 * a)