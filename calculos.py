import math

def delta(a: float, b: float, c: float):
    return b ** 2 - 4 * a * c

def raizSoma(a: float, b: float, c: float):
    deltaResult = delta(a, b, c)
    return (-b + math.sqrt(deltaResult)) / (2 * a)

def raizSubtracao(a: float, b: float, c: float):
    deltaResult = delta(a, b, c)
    return (-b - math.sqrt(deltaResult)) / (2 * a)

def bhaskara(a: float, b: float, c: float):
    if a == 0:
        raise ValueError("Coeficiente 'a' não pode ser zero em uma equação quadrática.")
    deltaResult = delta(a, b, c)

    if deltaResult < 0:
        raise ValueError("Delta é negativo. Não existem raízes reais.")

    raiz1 = raizSoma(a, b, c)
    raiz2 = raizSubtracao(a, b, c)

    return (raiz1, raiz2)